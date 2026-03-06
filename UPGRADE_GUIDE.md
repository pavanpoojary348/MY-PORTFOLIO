# 🚀 Portfolio Upgrade Guide — 2026

## What Changed (Summary)

### ✅ TASK 1 — Contact Form Fixed
**Root cause:** The form was sending `application/x-www-form-urlencoded` via fetch, but the success
response was an HTML page (not JSON), causing the JS to fail silently.

**Fix applied:**
- `app.py` now supports both **JSON** and form-encoded POST requests
- `contact.html` sends JSON via fetch and reads a JSON response
- Proper loading state, error messages, and field-level validation added
- **Security fix:** Mail credentials moved to environment variables (set `MAIL_USERNAME` and `MAIL_PASSWORD` in Render dashboard → Environment)

---

### ✅ TASK 2 — Certificate Section Added
- New page: `/certificates` → `templates/certificates.html`
- Filter by category: All / Python / Web Dev / ML & Data / Other
- Quick View modal with skills, description, and verify link
- Add your real certificates by editing the `cert-card` blocks — update `data-*` attributes

---

### ✅ TASK 3 — Fully Responsive
**Mobile-first CSS:**
- `320px+` — Single column, hamburger drawer menu, full-width inputs (min 44px touch targets)
- `600px+` — 2-column grids for projects, certificates
- `768px+` — Desktop nav shown, about section side-by-side, contact layout side-by-side
- `1024px+` — 3-column grids, larger spacing
- `1200px+` — Max-width containers, generous padding

---

### ✅ TASK 4 — Design & UX Upgrades
- **New fonts:** Space Mono (code/mono) + Outfit (body) — distinctive pairing
- **Noise texture overlay** for visual depth
- **CSS Grid background** on hero section
- **Animated badge** with pulsing green dot ("Available")
- **Scroll reveal** on all cards and sections (IntersectionObserver)
- **Skill bars** only animate when scrolled into view
- **Problem → Solution → Result** framework on all project cards
- **Timeline** added to About page
- **Hero stats** block (Projects / Certs / Year)
- **Navbar** auto-hides hamburger on desktop, adds scroll shadow
- **Base template** (`base.html`) — single source of truth for navbar, footer

---

## File Structure

```
portfolio/
├── app.py                  ← Flask backend (UPDATED)
├── requirements.txt        ← Dependencies
├── Procfile                ← gunicorn web: ... (unchanged)
├── templates/
│   ├── base.html           ← NEW: shared layout (navbar + footer)
│   ├── index.html          ← UPDATED: hero redesign
│   ├── about.html          ← UPDATED: timeline, tags
│   ├── projects.html       ← UPDATED: problem/solution/result cards
│   ├── skills.html         ← UPDATED: tool grid, learning tags
│   ├── certificates.html   ← NEW: certs with modal
│   └── contact.html        ← UPDATED: fixed form
└── static/
    ├── style.css           ← UPDATED: complete redesign
    ├── script.js           ← UPDATED: hamburger, scroll reveal
    └── Pavan.jpg           ← (your photo, unchanged)
```

---

## Deployment Steps (Render)

1. **Copy** all files into your existing project, replacing old ones
2. **Move** HTML files to `templates/` folder, photo + CSS + JS to `static/`
3. In Render dashboard → **Environment** → Add variables:
   - `MAIL_USERNAME` = `poojaryp379@gmail.com`
   - `MAIL_PASSWORD` = `your-16-char-app-password`
4. Push to GitHub → Render auto-deploys

> ⚠️ Never commit your email password to Git. The new `app.py` reads it from env vars.

---

## Adding Real Certificates

In `certificates.html`, each cert card looks like:

```html
<div class="cert-card" data-category="web">
  <div class="cert-org-badge udemy">Udemy</div>
  <div class="cert-body">
    <h3>Your Certificate Name</h3>
    <p class="cert-org"><i class="fas fa-building"></i> Issuing Organization</p>
    <p class="cert-date"><i class="fas fa-calendar-alt"></i> 2025</p>
    <div class="cert-skills">
      <span>Skill 1</span><span>Skill 2</span>
    </div>
  </div>
  <div class="cert-footer">
    <button class="btn btn-sm" onclick="openCertModal(this)"
      data-title="Certificate Name"
      data-org="Organization"
      data-date="2025"
      data-skills="Skill 1, Skill 2, Skill 3"
      data-desc="Description of what you learned."
      data-link="https://verify.url">
      <i class="fas fa-eye"></i> Quick View
    </button>
    <a href="https://verify.url" target="_blank" class="btn btn-outline btn-sm">
      <i class="fas fa-external-link-alt"></i> Verify
    </a>
  </div>
</div>
```

**Category options:** `python` | `web` | `ml` | `other`
**Badge colors:** `ibm` | `coursera` | `udemy` | `nptel` | `github`

---

## Testing Checklist

- [ ] Mobile (375px): hamburger opens/closes, form inputs are full width
- [ ] Tablet (768px): desktop nav visible, about section side-by-side
- [ ] Desktop (1200px): 3-column project grid, generous spacing
- [ ] Contact form: sends, shows success, resets
- [ ] Contact form: validates (empty name, bad email, short message)
- [ ] Certificate modal: opens, closes with X and Escape key
- [ ] Certificate filters work
- [ ] Skill bars animate on scroll into view
- [ ] Cards reveal on scroll
- [ ] Footer social links open in new tab
