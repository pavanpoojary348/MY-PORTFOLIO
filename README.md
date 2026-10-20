# Pavan Poojary &mdash; Developer Portfolio

A responsive, cyberpunk-inspired personal portfolio web application built with **Flask (Python)** and vanilla **JavaScript / CSS**, featuring an interactive canvas particle background, `Ctrl+K` Command Palette, category-filtered project showcase, verified credentials, and optimized for instant **Vercel Serverless** deployment.

---

## ⚡ Highlights & Key Features

- **Cyberpunk Dark Aesthetic**: Custom neon glassmorphism design with cyan (`#00f0ff`) and purple gradient accents.
- **Interactive Command Palette (`Ctrl + K`)**: Quick fuzzy navigation across all pages, external profiles (GitHub, LinkedIn, LeetCode), and 1-click email copy.
- **Interactive Project Filtering**: Instant client-side filtering across AI/ML & Multi-Agent systems, Web Applications, and Data/ETL pipelines with terminal-style headers.
- **Verified Credentials & Quick Resume Preview**: Verified certificates from IBM, Coursera, and Credly, with an in-browser PDF reader modal and direct download.
- **Coding Profiles Matrix**: Integrated GitHub repositories and LeetCode algorithmic problem-solving showcase (`@pavanlpoojary`) with DSA focus areas.
- **Working Contact Form**: Flask-Mail integration with live character counter, loading spinner, and safe demo fallback.
- **Top Scroll Progress Bar**: Smooth 2px gradient line tracking page scroll depth.
- **Custom Cyberpunk 404 Page**: Themed fallback with return-to-base navigation.
- **Vercel Serverless Ready**: Native `api/index.py` and `vercel.json` rewrite configuration for sub-second global edge response times.

---

## 🛠️ Tech Stack

- **Backend**: Python 3, Flask, Flask-Mail, Gunicorn
- **Frontend**: Semantic HTML5, Vanilla Modern CSS, JavaScript (ES6+), Canvas API
- **Icons & Fonts**: Font Awesome 6, Google Fonts (Outfit, Fira Code)
- **Deployment**: Vercel Serverless Functions (`@vercel/python`)

---

## 🚀 Quick Start (Local Development)

### 1. Clone the repository
```bash
git clone https://github.com/pavanpoojary348/MY-PORTFOLIO.git
cd MY-PORTFOLIO
```

### 2. Set up a virtual environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. (Optional) Configure environment variables
Copy `.env.example` to `.env` if you want to test live email delivery:
```bash
cp .env.example .env
```
Fill in your Gmail address and 16-character Google App Password:
```env
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

### 5. Run the application
```bash
python app.py
```
Open [http://localhost:5000](http://localhost:5000) in your browser.

---

## 🌐 Deploying to Vercel (Fast & Free)

This repository is pre-configured with `vercel.json` and `api/index.py` for automatic Vercel deployment:

1. Go to [vercel.com](https://vercel.com) and log in with your **GitHub** account.
2. Click **Add New...** &rarr; **Project**.
3. Select and import `pavanpoojary348/MY-PORTFOLIO`.
4. In **Project Settings**:
   - **Framework Preset**: *Other* (detected automatically).
   - **Root Directory**: `./` (leave default).
5. (Optional) In **Environment Variables**, add:
   - `MAIL_USERNAME` = `poojaryp379@gmail.com`
   - `MAIL_PASSWORD` = `your-16-char-gmail-app-password`
6. Click **Deploy**! Your site will be live on a global fast CDN in under 60 seconds with automatic HTTPS.

---

## 📬 Connect

- **Portfolio**: [pavanpoojary.vercel.app](https://pavanpoojary.vercel.app)
- **GitHub**: [github.com/pavanpoojary348](https://github.com/pavanpoojary348)
- **LeetCode**: [leetcode.com/u/pavanlpoojary](https://leetcode.com/u/pavanlpoojary/)
- **LinkedIn**: [linkedin.com/in/pavanlpoojary](https://www.linkedin.com/in/pavanlpoojary/)
- **Email**: [poojaryp379@gmail.com](mailto:poojaryp379@gmail.com)

---

&copy; 2025 Pavan Poojary &mdash; Built with &#10084;&#65039; and dedication.