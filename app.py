import os
import re
import time
import traceback
import urllib.parse
from collections import defaultdict
from flask import Flask, render_template, request, send_from_directory
from flask_mail import Mail, Message

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    static_folder=os.path.join(BASE_DIR, 'static'),
    template_folder=os.path.join(BASE_DIR, 'templates')
)

# ===== SECURITY CONFIGURATION =====
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or os.urandom(32).hex()
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024  # Max 500 KB payload to prevent memory exhaustion / DoS
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['SESSION_COOKIE_SECURE'] = os.environ.get('SESSION_COOKIE_SECURE', 'false').lower() in ('true', '1')

# ===== VERCEL SERVERLESS WSGI PATH REWRITE MIDDLEWARE =====
class VercelPathMiddleware:
    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, environ, start_response):
        qs = environ.get('QUERY_STRING', '')
        if '__vercel_route__' in qs:
            params = urllib.parse.parse_qs(qs, keep_blank_values=True)
            routes = params.pop('__vercel_route__', ['/'])
            target_route = routes[0] if routes else '/'

            while target_route.startswith('//'):
                target_route = target_route[1:]
            if not target_route.startswith('/'):
                target_route = '/' + target_route
            if len(target_route) > 1 and target_route.endswith('/'):
                target_route = target_route.rstrip('/')

            environ['PATH_INFO'] = target_route

            # Reconstruct clean query string without __vercel_route__
            pairs = []
            for k, vs in params.items():
                for v in vs:
                    pairs.append((k, v))
            environ['QUERY_STRING'] = urllib.parse.urlencode(pairs)
        elif environ.get('PATH_INFO') in ('/api/index', '/api/index.py'):
            environ['PATH_INFO'] = '/'

        return self.wsgi_app(environ, start_response)

app.wsgi_app = VercelPathMiddleware(app.wsgi_app)

# ===== LOAD .ENV FILE IF PRESENT =====
env_path = os.path.join(BASE_DIR, '.env')
if os.path.exists(env_path):
    with open(env_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, val = line.split('=', 1)
                os.environ.setdefault(key.strip(), val.strip().strip('"').strip("'"))

# ===== FLASK-MAIL CONFIGURATION =====
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', '1', 'yes']
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME', 'poojaryp379@gmail.com')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', '')
app.config['MAIL_DEFAULT_SENDER'] = (
    os.environ.get('MAIL_SENDER_NAME', 'Portfolio Contact'),
    app.config['MAIL_USERNAME']
)

mail = Mail(app)

# ===== SECURITY RESPONSE HEADERS =====
@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    response.headers['Permissions-Policy'] = 'camera=(), microphone=(), geolocation=(), payment=()'
    response.headers['Content-Security-Policy'] = (
        "default-src 'self'; "
        "script-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com https://cdn.jsdelivr.net https://unpkg.com https://api.emailjs.com; "
        "style-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com https://fonts.googleapis.com; "
        "font-src 'self' https://cdnjs.cloudflare.com https://fonts.gstatic.com; "
        "img-src 'self' data: https:; "
        "connect-src 'self' https://api.emailjs.com; "
        "frame-ancestors 'self';"
    )
    response.headers['Server'] = 'Web'
    return response

# ===== ANTI-SPAM & RATE LIMITING =====
_contact_rate_limit = defaultdict(list)
RATE_LIMIT_WINDOW_SECS = 600  # 10 minutes
RATE_LIMIT_MAX_ATTEMPTS = 5
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

def get_client_ip():
    forwarded = request.headers.get('X-Forwarded-For')
    if forwarded:
        return forwarded.split(',')[0].strip()
    return request.remote_addr or '127.0.0.1'

def is_rate_limited(ip):
    now = time.time()
    recent = [t for t in _contact_rate_limit[ip] if now - t < RATE_LIMIT_WINDOW_SECS]
    _contact_rate_limit[ip] = recent
    if len(recent) >= RATE_LIMIT_MAX_ATTEMPTS:
        return True
    _contact_rate_limit[ip].append(now)
    return False

# ===== ROUTES =====
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/index')
@app.route('/api/index.py')
def api_index():
    return home()

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.path.join(BASE_DIR, 'static'), filename)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/certificates')
def certificates():
    return render_template('certificates.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        client_ip = get_client_ip()

        # 1. Rate limiting check (prevents email spam flooding / bot attacks)
        if is_rate_limited(client_ip):
            return render_template(
                'contact.html',
                success_message='Too many requests. Please wait a few minutes before trying again.'
            ), 429

        # 2. Honeypot check for automated bot scrapers
        bot_trap = request.form.get('honeypot') or request.form.get('website') or request.form.get('phone_number')
        if bot_trap:
            # Silently discard spam submission while acknowledging
            return render_template(
                'contact.html',
                success_message='Message sent successfully! Pavan will get back to you soon!'
            )

        # 3. Input extraction and sanitization
        raw_name = request.form.get('name', '')
        raw_email = request.form.get('email', '')
        raw_message = request.form.get('message', '')

        # Strip newline characters to prevent SMTP / HTTP header injection attacks
        name = ''.join(c for c in raw_name if c not in '\r\n').strip()
        email = ''.join(c for c in raw_email if c not in '\r\n').strip()
        message = raw_message.strip()

        # 4. Strict input length & validation checks
        if not name or len(name) > 100:
            return render_template('contact.html', success_message='Invalid name provided. Please enter 1-100 characters.'), 400

        if not email or len(email) > 120 or not EMAIL_REGEX.match(email):
            return render_template('contact.html', success_message='Invalid email address. Please provide a valid email.'), 400

        if not message or len(message) > 3000:
            return render_template('contact.html', success_message='Invalid message length (1-3000 characters).'), 400

        try:
            # Graceful fallback when mail password is not configured
            if not app.config.get('MAIL_PASSWORD'):
                print(f"[Contact Form] Demo submission from {name} ({email}) [IP: {client_ip}]: {message[:80]}...")
                return render_template(
                    'contact.html',
                    success_message='Message sent successfully! Pavan will get back to you soon!'
                )

            msg = Message(
                subject=f'New Message from {name}',
                recipients=[app.config.get('MAIL_USERNAME', 'poojaryp379@gmail.com')],
                body=f'''New Contact Form Submission

Name: {name}
Email: {email}
IP: {client_ip}

Message:
{message}''',
                reply_to=email
            )
            mail.send(msg)
            return render_template(
                'contact.html',
                success_message='Message sent successfully! Pavan will get back to you soon!'
            )
        except Exception as e:
            traceback.print_exc()
            return render_template(
                'contact.html',
                success_message='Message not sent. Please try again later.'
            ), 500

    return render_template('contact.html')

# ===== ERROR HANDLERS =====
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(413)
def request_too_large(e):
    return render_template('404.html'), 413

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    is_debug = os.environ.get('FLASK_DEBUG', 'False').lower() in ('true', '1')
    print(f'Flask Portfolio Server Starting (debug={is_debug})...')
    app.run(debug=is_debug)
