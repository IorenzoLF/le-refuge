const CACHE_NAME = 'le-refuge-cache-v1';
const urlsToCache = [
  '/',
  '/index.html',
  '/styles.css',
  '/images/cerisier.jpg',
  // Ajoute d'autres ressources à mettre en cache
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
}); 