// ========== POLYRISE GLOBAL SCRIPT ==========

// 💡 DAILY QUOTE FUNCTIONALITY
const quotes = [
  {
    text: "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    author: "Winston Churchill"
  },
  {
    text: "Don’t watch the clock; do what it does. Keep going.",
    author: "Sam Levenson"
  },
  {
    text: "The best way to predict the future is to create it.",
    author: "Peter Drucker"
  },
  {
    text: "Believe you can and you're halfway there.",
    author: "Theodore Roosevelt"
  },
  {
    text: "Start where you are. Use what you have. Do what you can.",
    author: "Arthur Ashe"
  }
];

window.addEventListener("DOMContentLoaded", function () {
  const today = new Date();
  const index = today.getDate() % quotes.length;
  const dailyQuote = quotes[index];

  const quoteText = document.getElementById("quote-text");
  const quoteAuthor = document.getElementById("quote-author");

  if (quoteText && quoteAuthor) {
    quoteText.innerText = "“" + dailyQuote.text + "”";
    quoteAuthor.innerText = "— " + dailyQuote.author;
  }

  // 🌗 Apply saved theme
  const savedTheme = localStorage.getItem("theme");
  if (savedTheme) {
    setTheme(savedTheme);
  }
});

// 🌗 Theme Switcher
function setTheme(theme) {
  document.body.classList.remove("theme-light", "theme-dark", "theme-neon");
  document.body.classList.add("theme-" + theme);
  localStorage.setItem("theme", theme);
}

// 📁 Sidebar Collapse/Expand Logic
document.addEventListener("DOMContentLoaded", function () {
  const collapseBtn = document.querySelector(".collapse-btn");
  const mainWrapper = document.querySelector(".main-wrapper");
  const sidebar = document.querySelector(".sidebar");
  const contentArea = document.querySelector(".content-area");

  if (collapseBtn && sidebar && mainWrapper && contentArea) {
    collapseBtn.addEventListener("click", function () {
      sidebar.classList.toggle("collapsed");

      if (sidebar.classList.contains("collapsed")) {
        contentArea.style.marginLeft = "70px";
      } else {
        contentArea.style.marginLeft = "260px";
      }
    });
  }
});
