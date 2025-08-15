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

document.querySelectorAll('.theme-toggle button').forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('onclick') === `setTheme('${theme}')`);
  });

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


// dashboard_extra.js
document.addEventListener('DOMContentLoaded', function(){
  // --- Quotes (fallback). If you already have a script that sets #quote-text/#quote-author, remove this block.
  const quotes = [
    { text: "Small steps every day lead to bigger results.", author: "PolyRise" },
    { text: "Practice more. Worry less. Learn faster.", author: "PolyRise" },
    { text: "Knowledge grows when you teach it.", author: "PolyRise" }
  ];
  // Show quote of the day based on day index
  const dayIndex = new Date().getDate() % quotes.length;
  const q = quotes[dayIndex];
  const quoteText = document.getElementById('quote-text');
  const quoteAuthor = document.getElementById('quote-author');
  if (quoteText) quoteText.textContent = q.text;
  if (quoteAuthor) quoteAuthor.textContent = q.author;

  // --- News rotation (simple)
  const newsItems = [
    { title: "AI Revolution in Engineering", body: "How artificial intelligence is transforming engineering practices.", link: "#" },
    { title: "MSBTE Updates: Exam Dates", body: "New exam dates published for K-Scheme students.", link: "#" },
    { title: "Top Internship Tips 2025", body: "How to prepare for campus drives and virtual interviews.", link: "#" }
  ];
  let newsIndex = 0;
  const newsTitle = document.getElementById('news-title');
  const newsBody = document.getElementById('news-body');
  const newsLink = document.getElementById('news-link');
  function showNews(i){
    const item = newsItems[i % newsItems.length];
    if (newsTitle) newsTitle.textContent = item.title;
    if (newsBody) newsBody.textContent = item.body;
    if (newsLink) newsLink.href = item.link;
  }
  showNews(newsIndex);
  setInterval(function(){
    newsIndex++;
    showNews(newsIndex);
  }, 8000);

  // small UI nicety: animate quote fade
  if (quoteText) {
    quoteText.style.opacity = 0;
    setTimeout(()=> quoteText.style.transition = "opacity .4s", 100);
    setTimeout(()=> quoteText.style.opacity = 1, 120);
  }
});


$(document).ready(function(){
    $('.tab-btn').click(function(){
        var tab = $(this).data('tab');
        $('.tab-btn').removeClass('active');
        $(this).addClass('active');
        $('.tab-section').removeClass('active');
        $('#' + tab).addClass('active');
    });

    $('#add-note-btn').click(function(){
        $('#add-note-form').toggle();
    });
});



