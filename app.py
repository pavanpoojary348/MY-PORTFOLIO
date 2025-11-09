from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ===== ROUTES =====
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

app.static_folder = 'static'
app.template_folder = 'templates'

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
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        print("=====================================")
        print(f"📩 New Message Received:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Message: {message}")
        print("=====================================")

        # You can show a success message too:
        return render_template('contact.html', success_message="✅ Message sent successfully!")

    return render_template('contact.html')

# ===== MAIN =====
if __name__ == '__main__':
    app.run(debug=True)
