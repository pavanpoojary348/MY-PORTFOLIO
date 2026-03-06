from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
import traceback
import os

app = Flask(__name__)

# ===== FLASK-MAIL CONFIGURATION (uses env vars for security) =====
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME', 'poojaryp379@gmail.com')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', '')   # Set in Render dashboard
app.config['MAIL_DEFAULT_SENDER'] = ('Portfolio Contact', os.environ.get('MAIL_USERNAME', 'poojaryp379@gmail.com'))

mail = Mail(app)

app.static_folder = 'static'
app.template_folder = 'templates'

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
        # Support both JSON (fetch) and form-encoded submissions
        if request.is_json:
            data = request.get_json()
            name = data.get('name', '')
            email = data.get('email', '')
            message = data.get('message', '')
        else:
            name = request.form.get('name', '')
            email = request.form.get('email', '')
            message = request.form.get('message', '')

        # Basic validation
        if not name or not email or not message:
            if request.is_json:
                return jsonify({'status': 'error', 'message': 'All fields are required.'}), 400
            return render_template('contact.html', error_message='All fields are required.')

        try:
            msg = Message(
                subject=f"📩 New Portfolio Message from {name}",
                recipients=['poojaryp379@gmail.com'],
                body=f"""
📨 New Contact Form Submission
================================
Name: {name}
Email: {email}

Message:
{message}
================================
                """,
                reply_to=email
            )
            mail.send(msg)

            if request.is_json:
                return jsonify({'status': 'success', 'message': '✅ Message sent! I\'ll get back to you soon.'})
            return render_template('contact.html', success_message="✅ Message sent successfully!")

        except Exception as e:
            traceback.print_exc()
            if request.is_json:
                return jsonify({'status': 'error', 'message': '⚠️ Could not send message. Please try again.'}), 500
            return render_template('contact.html', error_message="⚠️ Message not sent. Please try again later.")

    return render_template('contact.html')

# ===== MAIN =====
if __name__ == '__main__':
    app.run(debug=True)
