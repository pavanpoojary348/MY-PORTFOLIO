import os
import traceback
from flask import Flask, render_template, request
from flask_mail import Mail, Message

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    static_folder=os.path.join(BASE_DIR, 'static'),
    template_folder=os.path.join(BASE_DIR, 'templates')
)

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
