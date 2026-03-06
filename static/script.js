/* ============================================
   PAVAN POOJARY PORTFOLIO — script.js
   ============================================ */

// ===== MOBILE HAMBURGER MENU =====
const hamburger     = document.getElementById('hamburger');
const mobileDrawer  = document.getElementById('mobileDrawer');
const mobileOverlay = document.getElementById('mobileOverlay');

function openMenu() {
  hamburger.classList.add('open');
  hamburger.setAttribute('aria-expanded', 'true');
  mobileDrawer.classList.add('open');
  mobileOverlay.classList.add('show');
  document.body.style.overflow = 'hidden';
}

function closeMenu() {
  hamburger.classList.remove('open');
  hamburger.setAttribute('aria-expanded', 'false');
  mobileDrawer.classList.remove('open');
  mobileOverlay.classList.remove('show');
  document.body.style.overflow = '';
}

if (hamburger) {
  hamburger.addEventListener('click', () => {
    if (mobileDrawer.classList.contains('open')) closeMenu();
    else openMenu();
  });
}
if (mobileOverlay) mobileOverlay.addEventListener('click', closeMenu);

// Close drawer on link click
document.querySelectorAll('.mobile-drawer a').forEach(link => {
  link.addEventListener('click', closeMenu);
});

// ===== NAVBAR SCROLL SHADOW =====
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  if (!navbar) return;
  if (window.scrollY > 10) {
    navbar.style.boxShadow = '0 4px 30px rgba(0,0,0,0.3)';
  } else {
    navbar.style.boxShadow = 'none';
  }
}, { passive: true });

// ===== SCROLL REVEAL =====
const revealEls = document.querySelectorAll(
  '.project-card, .skill, .tool-card, .cert-card, .tl-item, .about-img-wrap, .about-text, .contact-form-wrap, .contact-info'
);

const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = '1';
      entry.target.style.transform = 'translateY(0)';
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

revealEls.forEach(el => {
  el.style.opacity = '0';
  el.style.transform = 'translateY(24px)';
  el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
  revealObserver.observe(el);
});

// ===== SKILL BAR ANIMATION =====
// Triggered once bars enter viewport
const skillBars = document.querySelectorAll('.bar .fill');
if (skillBars.length) {
  const barObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.animationPlayState = 'running';
        barObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.3 });

  skillBars.forEach(bar => {
    bar.style.animationPlayState = 'paused';
    barObserver.observe(bar);
  });
}

// ===== CONTACT FORM (handled inline in contact.html) =====
// Kept here for reference only — actual logic is in the template
