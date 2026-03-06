from flask import Flask, render_template, request, jsonify
import os

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

@app.route('/certificates')
def certificates():
    return render_template('certificates.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    # EmailJS handles email sending from browser directly
    # Flask just serves the page
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
