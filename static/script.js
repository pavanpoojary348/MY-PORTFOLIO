// ===== CONTACT FORM POPUP =====
const form = document.getElementById("contactForm");
const popup = document.getElementById("popup");
const popupMessage = document.getElementById("popup-message");

if (form) {
  form.addEventListener("submit", async (event) => {
    event.preventDefault(); // stop page reload

    const formData = new FormData(form);
    const data = Object.fromEntries(formData);

    try {
      const response = await fetch("/contact", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams(data).toString(),
      });

      const text = await response.text();
      if (response.ok) {
        popupMessage.textContent = "✅ Message sent successfully! Pavan will get back to you soon.";
      } else {
        popupMessage.textContent = "⚠️ Message not sent. Please try again later.";
      }

      popup.classList.add("show");
      setTimeout(() => popup.classList.remove("show"), 4000);
      form.reset();
    } catch (err) {
      popupMessage.textContent = "⚠️ Something went wrong!";
      popup.classList.add("show");
      setTimeout(() => popup.classList.remove("show"), 4000);
      console.error(err);
    }
  });
}
