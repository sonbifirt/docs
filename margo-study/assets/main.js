(function () {
  var doc = document.documentElement;
  doc.classList.remove('no-js');

  // Sticky header
  var header = document.querySelector('.header');
  var onScroll = function () { header.classList.toggle('is-scrolled', window.scrollY > 30); };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // Mobile nav
  var burger = document.querySelector('.burger');
  burger.addEventListener('click', function () {
    var open = doc.classList.toggle('nav-open');
    burger.setAttribute('aria-expanded', open);
  });
  document.querySelectorAll('.nav__links a').forEach(function (a) {
    a.addEventListener('click', function () {
      doc.classList.remove('nav-open');
      burger.setAttribute('aria-expanded', 'false');
    });
  });

  // Reveal on scroll
  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('is-in'); });
  }

  // Reviews slider
  var slider = document.querySelector('.slider');
  document.querySelectorAll('[data-slide]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var card = slider.querySelector('.review');
      var step = card ? card.getBoundingClientRect().width + 20 : 320;
      slider.scrollBy({ left: step * Number(btn.dataset.slide), behavior: 'smooth' });
    });
  });

  // Lead form -> WhatsApp (prefilled message)
  var form = document.querySelector('.form');
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!form.reportValidity()) return;
    var d = new FormData(form);
    var msg = form.dataset.msg + '\n\n' +
      form.dataset.lName + ': ' + d.get('name') + '\n' +
      form.dataset.lPhone + ': ' + d.get('phone') + '\n' +
      form.dataset.lEmail + ': ' + d.get('email');
    window.open('https://wa.me/' + form.dataset.wa + '?text=' + encodeURIComponent(msg), '_blank', 'noopener');
    form.classList.add('is-sent');
    form.reset();
  });

  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
