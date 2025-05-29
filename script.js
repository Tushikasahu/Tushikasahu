// Light/Dark mode toggle
const toggleBtn = document.getElementById('theme-toggle');
toggleBtn.addEventListener('click', () => {
  if (document.body.getAttribute('data-theme') === 'dark') {
    document.body.removeAttribute('data-theme');
    localStorage.setItem('theme', 'light');
  } else {
    document.body.setAttribute('data-theme', 'dark');
    localStorage.setItem('theme', 'dark');
  }
});

// Load theme from storage
(function() {
  const theme = localStorage.getItem('theme');
  if (theme === 'dark') {
    document.body.setAttribute('data-theme', 'dark');
  }
})();

// Year auto-update
document.getElementById('year').textContent = new Date().getFullYear();