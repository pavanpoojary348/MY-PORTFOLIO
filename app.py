from flask import Flask, render_template, request
from flask_mail import Mail, Message
import traceback

app = Flask(__name__)

# ===== FLASK-MAIL CONFIGURATION =====
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'poojaryp379@gmail.com'   # ✅ your Gmail ID
app.config['MAIL_PASSWORD'] = 'remxsxtxrpvoisnn'        # ✅ your 16-character app password (no spaces)
app.config['MAIL_DEFAULT_SENDER'] = ('Portfolio Contact', 'poojaryp379@gmail.com')  # ✅ same Gmail ID

mail = Mail(app)

# ===== STATIC / TEMPLATE FOLDERS =====
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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    print("🚀 /contact route called")   # <=== DEBUG CHECK

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        print("=====================================")
        print(f"📩 New Message Received:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Message: {message}")
        print("=====================================")

        try:
            msg = Message(
                subject=f"📩 New Message from {name}",
                recipients=['poojaryp379@gmail.com'],  # ✅ Receiver (your inbox)
                body=f"""
📨 New Contact Form Submission

Name: {name}
Email: {email}

Message:
{message}
                """,
                reply_to=email
            )

            mail.send(msg)
            print("✅ Email sent successfully!")
            print("📨 Check your Gmail 'Sent Mail' folder.")

            return render_template(
                'contact.html',
                success_message="✅ Message sent successfully! Pavan will get back to you soon!"
            )

        except Exception as e:
            print("❌ Error sending email:")
            traceback.print_exc()
            return render_template(
                'contact.html',
                success_message="⚠️ Message not sent. Please try again later."
            )

    return render_template('contact.html')

# ===== MAIN =====
if __name__ == '__main__':
    print("🚀 Flask Portfolio Server Starting...")
    app.run(debug=True)
