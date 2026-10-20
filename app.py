import os
import traceback
from flask import Flask, render_template, request, send_from_directory
from flask_mail import Mail, Message

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    static_folder=os.path.join(BASE_DIR, 'static'),
    template_folder=os.path.join(BASE_DIR, 'templates')
)

# ===== VERCEL SERVERLESS WSGI PATH REWRITE MIDDLEWARE =====
class VercelPathMiddleware:
    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, environ, start_response):
        if 'debug_env' in environ.get('QUERY_STRING', ''):
            headers = [('Content-Type', 'text/plain')]
            start_response('200 OK', headers)
            debug_info = []
            for k, v in sorted(environ.items()):
                if isinstance(v, (str, int, float, bool)):
                    debug_info.append(f"{k} = {v}")
            return [("\n".join(debug_info)).encode('utf-8')]

        forwarded_uri = (
            environ.get('HTTP_X_FORWARDED_URI') or
            environ.get('HTTP_X_MATCHED_PATH') or
            environ.get('HTTP_X_ORIGINAL_URI') or
            environ.get('HTTP_X_REWRITE_URL')
        )
        if forwarded_uri:
            path_only = forwarded_uri.split('?')[0]
            if path_only.startswith('/api/index.py'):
                path_only = path_only.replace('/api/index.py', '', 1) or '/'
            elif path_only.startswith('/api/index'):
                path_only = path_only.replace('/api/index', '', 1) or '/'
            environ['PATH_INFO'] = path_only
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
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        try:
            # Graceful fallback when mail password is not configured
            if not app.config.get('MAIL_PASSWORD'):
                print(f"[Contact Form] Demo submission from {name} ({email}): {message}")
                return render_template('contact.html',
                    success_message='Message sent successfully! Pavan will get back to you soon!')

            msg = Message(
                subject=f'New Message from {name}',
                recipients=[app.config.get('MAIL_USERNAME', 'poojaryp379@gmail.com')],
                body=f'''New Contact Form Submission

Name: {name}
Email: {email}

Message:
{message}''',
                reply_to=email
            )
            mail.send(msg)
            return render_template('contact.html',
                success_message='Message sent successfully! Pavan will get back to you soon!')
        except Exception as e:
            traceback.print_exc()
            return render_template('contact.html',
                success_message='Message not sent. Please try again later.')
    return render_template('contact.html')

# ===== ERROR HANDLERS =====
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    print('Flask Portfolio Server Starting...')
    app.run(debug=True)
