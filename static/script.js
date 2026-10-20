// ===== PARTICLE BACKGROUND =====
(function() {
  const canvas = document.getElementById('particles-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  let W, H;
  const particles = [];

  function resize() {
    W = canvas.width  = window.innerWidth;
    H = canvas.height = window.innerHeight;
  }
  resize();
  window.addEventListener('resize', resize);

  const COLORS = ['#00f0ff', '#9b66ff', '#ff4dd2'];
  for (let i = 0; i < 70; i++) {
    particles.push({
      x:     Math.random() * window.innerWidth,
      y:     Math.random() * window.innerHeight,
      r:     Math.random() * 1.5 + 0.3,
      dx:    (Math.random() - 0.5) * 0.3,
      dy:    (Math.random() - 0.5) * 0.3,
      color: COLORS[Math.floor(Math.random() * COLORS.length)],
      alpha: Math.random() * 0.5 + 0.2
    });
  }

  function draw() {
    ctx.clearRect(0, 0, W, H);
    particles.forEach(p => {
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = p.color;
      ctx.globalAlpha = p.alpha;
      ctx.fill();

      p.x += p.dx;
      p.y += p.dy;
      if (p.x < 0) p.x = W;
      if (p.x > W) p.x = 0;
      if (p.y < 0) p.y = H;
      if (p.y > H) p.y = 0;
    });

    ctx.globalAlpha = 1;
    // Connecting lines
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const d = Math.hypot(particles[i].x - particles[j].x, particles[i].y - particles[j].y);
        if (d < 100) {
          ctx.beginPath();
          ctx.strokeStyle = '#00f0ff';
          ctx.globalAlpha = (1 - d / 100) * 0.06;
          ctx.lineWidth = 0.5;
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.stroke();
        }
      }
    }
    ctx.globalAlpha = 1;
    requestAnimationFrame(draw);
  }
  draw();
})();

// ===== NAVBAR SCROLL =====
const navbar = document.querySelector('.navbar');
if (navbar) {
  window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 20);
  });
}

// ===== HAMBURGER MENU =====
const hamburger = document.getElementById('hamburger');
const navLinks   = document.querySelector('.nav-links');
if (hamburger && navLinks) {
  hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('open');
    navLinks.classList.toggle('open');
  });
  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      hamburger.classList.remove('open');
      navLinks.classList.remove('open');
    });
  });

  // Close menu when tapping outside on mobile
  document.addEventListener('click', (e) => {
    if (navLinks.classList.contains('open') && !navLinks.contains(e.target) && !hamburger.contains(e.target)) {
      hamburger.classList.remove('open');
      navLinks.classList.remove('open');
    }
  });
}

// ===== SCROLL REVEAL =====
const fadeEls = document.querySelectorAll('.fade-up');
if (fadeEls.length > 0) {
  const observer = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('visible');
        observer.unobserve(e.target);
      }
    });
  }, { threshold: 0.08 });
  fadeEls.forEach(el => observer.observe(el));
}

// ===== TYPED.JS INIT =====
if (document.getElementById('typed') && typeof Typed !== 'undefined') {
  new Typed('#typed', {
    strings: ['Web Developer', 'Python Enthusiast', 'ML Explorer', 'UI/UX Lover', 'Open Source Fan'],
    typeSpeed: 60,
    backSpeed: 35,
    backDelay: 1800,
    loop: true
  });
}

// ===== CONTACT FORM & CHARACTER COUNTER =====
const form         = document.getElementById('contactForm');
const popup        = document.getElementById('popup');
const popupMessage = document.getElementById('popup-message');
const messageInput = document.getElementById('message');
const charCounter  = document.getElementById('msgCharCount');
const charWrap     = document.querySelector('.char-count-wrap');

if (messageInput && charCounter) {
  messageInput.addEventListener('input', () => {
    const len = messageInput.value.length;
    charCounter.textContent = len;
    if (charWrap) {
      charWrap.classList.toggle('limit-near', len >= 480);
    }
  });
}

if (form) {
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const submitBtn = form.querySelector('button[type="submit"]');
    const originalBtnHtml = submitBtn ? submitBtn.innerHTML : '';
    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
    }

    const data = Object.fromEntries(new FormData(form));
    try {
      const res = await fetch('/contact', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams(data).toString()
      });
      if (res.ok) {
        popupMessage.textContent = '✅ Message sent! Pavan will get back to you soon.';
        if (submitBtn) submitBtn.innerHTML = '<i class="fas fa-check"></i> Message Sent!';
        form.reset();
        if (charCounter) charCounter.textContent = '0';
        if (charWrap) charWrap.classList.remove('limit-near');
      } else {
        popupMessage.textContent = '❌ Message not sent. Please try again.';
        if (submitBtn) submitBtn.innerHTML = originalBtnHtml;
      }
      popup.classList.add('show');
      setTimeout(() => popup.classList.remove('show'), 4000);
    } catch (err) {
      popupMessage.textContent = '❌ Something went wrong!';
      popup.classList.add('show');
      setTimeout(() => popup.classList.remove('show'), 4000);
      if (submitBtn) submitBtn.innerHTML = originalBtnHtml;
    } finally {
      setTimeout(() => {
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = originalBtnHtml;
        }
      }, 2500);
    }
  });
}

// ===== COPY EMAIL TO CLIPBOARD =====
const copyEmailBtn = document.getElementById('copyEmailBtn');
if (copyEmailBtn) {
  copyEmailBtn.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText('poojaryp379@gmail.com');
      const text = document.getElementById('copyEmailText');
      const icon = copyEmailBtn.querySelector('i');
      copyEmailBtn.classList.add('copied');
      if (text) text.textContent = 'Copied!';
      if (icon) icon.className = 'fas fa-check';
      setTimeout(() => {
        copyEmailBtn.classList.remove('copied');
        if (text) text.textContent = 'Copy';
        if (icon) icon.className = 'far fa-copy';
      }, 2000);
    } catch (err) {
      console.error('Failed to copy email:', err);
    }
  });
}

// ===== FLOATING SCROLL TO TOP ROCKET BUTTON =====
(function initScrollTop() {
  let btn = document.getElementById('scrollTopBtn');
  if (!btn) {
    btn = document.createElement('button');
    btn.id = 'scrollTopBtn';
    btn.className = 'scroll-top-btn';
    btn.setAttribute('aria-label', 'Scroll to top');
    btn.setAttribute('title', 'Back to top');
    btn.innerHTML = '<i class="fas fa-arrow-up"></i>';
    document.body.appendChild(btn);
  }

  window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
      btn.classList.add('visible');
    } else {
      btn.classList.remove('visible');
    }
  });

  btn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
})();

// ===== DEVELOPER COMMAND PALETTE (CTRL + K) =====
(function initCommandPalette() {
  if (!document.getElementById('cmdPaletteOverlay')) {
    const overlay = document.createElement('div');
    overlay.id = 'cmdPaletteOverlay';
    overlay.className = 'cmd-palette-overlay';
    overlay.innerHTML = `
      <div class="cmd-palette" role="dialog" aria-modal="true" aria-label="Command Palette">
        <div class="cmd-header">
          <i class="fas fa-terminal"></i>
          <input type="text" id="cmdInput" class="cmd-input" placeholder="Type a command or jump to page... (e.g. projects, resume)" autocomplete="off" />
          <span class="cmd-badge">ESC</span>
        </div>
        <div class="cmd-results" id="cmdResults">
          <a href="/" class="cmd-item" data-keywords="home main hero">
            <div class="cmd-item-left"><i class="fas fa-home"></i> <span>Home</span></div>
            <span class="cmd-item-hint">Go to Home</span>
          </a>
          <a href="/about" class="cmd-item" data-keywords="about who am i education experience bio nmamit">
            <div class="cmd-item-left"><i class="fas fa-user"></i> <span>About Me</span></div>
            <span class="cmd-item-hint">Education &amp; Experience</span>
          </a>
          <a href="/projects" class="cmd-item" data-keywords="projects chainsentinel spam flask web ml code">
            <div class="cmd-item-left"><i class="fas fa-rocket"></i> <span>Projects</span></div>
            <span class="cmd-item-hint">Featured Web &amp; AI Builds</span>
          </a>
          <a href="/skills" class="cmd-item" data-keywords="skills stack python c++ java react flask ml tools">
            <div class="cmd-item-left"><i class="fas fa-code"></i> <span>Skills &amp; Tech Stack</span></div>
            <span class="cmd-item-hint">Languages &amp; Frameworks</span>
          </a>
          <a href="/certificates" class="cmd-item" data-keywords="certificates resume achievements credly ibm coursera">
            <div class="cmd-item-left"><i class="fas fa-award"></i> <span>Certificates &amp; Achievements</span></div>
            <span class="cmd-item-hint">Verified Credentials</span>
          </a>
          <a href="/contact" class="cmd-item" data-keywords="contact hire email connect message">
            <div class="cmd-item-left"><i class="fas fa-envelope"></i> <span>Contact</span></div>
            <span class="cmd-item-hint">Get in Touch</span>
          </a>
          <a href="/static/Pavan_Poojary_Resume.pdf" class="cmd-item" download="Pavan_Poojary_Resume.pdf" data-keywords="resume cv pdf download">
            <div class="cmd-item-left"><i class="fas fa-file-pdf"></i> <span>Download Resume (PDF)</span></div>
            <span class="cmd-item-hint">PDF Download</span>
          </a>
          <a href="https://github.com/pavanpoojary348" target="_blank" class="cmd-item" data-keywords="github code repos source">
            <div class="cmd-item-left"><i class="fab fa-github"></i> <span>GitHub Profile</span></div>
            <span class="cmd-item-hint">External Link &rarr;</span>
          </a>
          <a href="https://www.linkedin.com/in/pavanlpoojary/" target="_blank" class="cmd-item" data-keywords="linkedin network social connect">
            <div class="cmd-item-left"><i class="fab fa-linkedin"></i> <span>LinkedIn Profile</span></div>
            <span class="cmd-item-hint">External Link &rarr;</span>
          </a>
          <a href="https://leetcode.com/u/pavanlpoojary/" target="_blank" class="cmd-item" data-keywords="leetcode dsa algorithms problems coding">
            <div class="cmd-item-left"><svg class="leetcode-icon-svg" viewBox="0 0 24 24" width="16" height="16"><path d="M13.483 0a1.374 1.374 0 0 0-.961.438L7.116 6.226l-3.854 4.126a5.266 5.266 0 0 0-1.209 2.104 5.35 5.35 0 0 0-.125.513 5.527 5.527 0 0 0 .062 2.362 5.83 5.83 0 0 0 .349 1.017 5.938 5.938 0 0 0 1.271 1.818l4.277 4.193.039.038c2.248 2.165 5.852 2.133 8.063-.074l2.396-2.392c.54-.54.54-1.414.003-1.955a1.378 1.378 0 0 0-1.951-.003l-2.396 2.392a3.021 3.021 0 0 1-4.205.038l-.02-.019-4.276-4.193c-.652-.64-.972-1.469-.948-2.263a2.68 2.68 0 0 1 .066-.523 2.545 2.545 0 0 1 .619-1.164L9.13 8.114c1.058-1.134 3.204-1.27 4.43-.278l3.501 2.831c.593.48 1.461.387 1.94-.207a1.384 1.384 0 0 0-.207-1.943l-3.5-2.831c-.8-.647-1.766-1.045-2.774-1.202l2.015-2.158A1.384 1.384 0 0 0 13.483 0zm-2.866 12.815a1.38 1.38 0 0 0-1.38 1.382 1.38 1.38 0 0 0 1.38 1.382H20.79a1.38 1.38 0 0 0 1.38-1.382 1.38 1.38 0 0 0-1.38-1.382z"/></svg> <span>LeetCode Profile</span></div>
            <span class="cmd-item-hint">External Link &rarr;</span>
          </a>
          <div class="cmd-item" id="cmdCopyEmail" data-keywords="copy email poojary mail address">
            <div class="cmd-item-left"><i class="far fa-copy"></i> <span>Copy Email Address</span></div>
            <span class="cmd-item-hint" id="cmdCopyHint">poojaryp379@gmail.com</span>
          </div>
        </div>
        <div class="cmd-footer">
          <span>Navigate with <kbd>Ctrl</kbd> + <kbd>K</kbd></span>
          <span>Pavan Poojary &bull; Portfolio</span>
        </div>
      </div>
    `;
    document.body.appendChild(overlay);
  }

  const overlay = document.getElementById('cmdPaletteOverlay');
  const input = document.getElementById('cmdInput');
  const results = document.getElementById('cmdResults');
  const items = Array.from(results.querySelectorAll('.cmd-item'));

  function openPalette() {
    overlay.classList.add('open');
    input.value = '';
    filterItems('');
    setTimeout(() => input.focus(), 60);
  }

  function closePalette() {
    overlay.classList.remove('open');
  }

  function filterItems(query) {
    const q = query.toLowerCase().trim();
    items.forEach(item => {
      const text = (item.textContent + ' ' + (item.getAttribute('data-keywords') || '')).toLowerCase();
      if (!q || text.includes(q)) {
        item.style.display = 'flex';
      } else {
        item.style.display = 'none';
      }
    });
  }

  document.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      if (overlay.classList.contains('open')) {
        closePalette();
      } else {
        openPalette();
      }
    } else if (e.key === 'Escape' && overlay.classList.contains('open')) {
      closePalette();
    }
  });

  overlay.addEventListener('click', (e) => {
    if (e.target === overlay) closePalette();
  });

  input.addEventListener('input', (e) => {
    filterItems(e.target.value);
  });

  const cmdCopy = document.getElementById('cmdCopyEmail');
  if (cmdCopy) {
    cmdCopy.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText('poojaryp379@gmail.com');
        const hint = document.getElementById('cmdCopyHint');
        if (hint) hint.textContent = 'Copied to clipboard!';
        setTimeout(() => {
          if (hint) hint.textContent = 'poojaryp379@gmail.com';
          closePalette();
        }, 1200);
      } catch (err) {
        console.error(err);
      }
    });
  }

  // Also bind any buttons with [data-open-cmd]
  document.querySelectorAll('[data-open-cmd]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      openPalette();
    });
  });
})();

// ===== TOP SCROLL PROGRESS BAR =====
(function initScrollProgress() {
  let bar = document.getElementById('scroll-progress-bar');
  if (!bar) {
    bar = document.createElement('div');
    bar.id = 'scroll-progress-bar';
    document.body.prepend(bar);
  }

  window.addEventListener('scroll', () => {
    const winScroll = document.documentElement.scrollTop || document.body.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = height > 0 ? (winScroll / height) * 100 : 0;
    if (bar) bar.style.width = scrolled + '%';
  }, { passive: true });
})();

// ===== RESUME PREVIEW MODAL =====
(function initResumeModal() {
  const openBtn  = document.getElementById('openResumeModalBtn');
  const modal    = document.getElementById('resumeModal');
  const closeBtn = document.getElementById('closeResumeModalBtn');

  if (!modal) return;

  const openModal = () => {
    modal.classList.add('open');
    document.body.style.overflow = 'hidden';
  };

  const closeModal = () => {
    modal.classList.remove('open');
    document.body.style.overflow = '';
  };

  if (openBtn) {
    openBtn.addEventListener('click', (e) => {
      e.preventDefault();
      openModal();
    });
  }

  if (closeBtn) {
    closeBtn.addEventListener('click', (e) => {
      e.preventDefault();
      closeModal();
    });
  }

  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeModal();
  });

  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.classList.contains('open')) {
      closeModal();
    }
  });
})();

