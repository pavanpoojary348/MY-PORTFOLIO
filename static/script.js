// ===== TYPED.JS TEXT ANIMATION =====
if (document.querySelector("#typed")) {
  new Typed("#typed", {
    strings: [
      "💻 Web Developer",
      "⚛️ React Learner",
      "🎨 Front-End Designer",
      "📚 Tech Enthusiast",
    ],
    typeSpeed: 70,
    backSpeed: 40,
    loop: true,
  });
}

// ===== SKILL BAR ANIMATION ON SCROLL =====
const skillBars = document.querySelectorAll(".fill");
let skillAnimated = false;

window.addEventListener("scroll", () => {
  if (skillAnimated) return; // Run only once

  skillBars.forEach((bar) => {
    const barTop = bar.getBoundingClientRect().top;
    const windowHeight = window.innerHeight;

    if (barTop < windowHeight - 50) {
      bar.style.animationPlayState = "running";
      skillAnimated = true;
    }
  });
});

// ===== CONTACT FORM ALERT =====
const contactForm = document.querySelector(".contact-form");
if (contactForm) {
  contactForm.addEventListener("submit", (event) => {
    event.preventDefault(); // Stop page reload
    alert("✅ Thank you! Pavan will get back to you soon.");
    contactForm.reset(); // Clears the form
  });
}
