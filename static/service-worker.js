self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open('estres-cache-v1').then((cache) => {
      return cache.addAll([
        '/',
        '/static/js/script.js',
        '/static/css/style.css'
      ]);
    })
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => response || fetch(event.request))
  );
});
