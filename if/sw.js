const CACHE_NAME = 'taxtifly-v1';
const urlsToCache = [
  '/',
  '/index.html',
  '/if-tool.html',
  '/manifest.json'
];

// Service Worker Install ho raha hai aur files ko cache kar raha hai
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        return cache.addAll(urlsToCache);
      })
  );
});

// Network se files fetch karne ke liye (Offline support ke liye)
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        // Agar file cache mein hai toh wahan se do, warna network se lo
        return response || fetch(event.request);
      })
  );
});

// Purane cache ko saaf karne ke liye
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cache => {
          if (cache !== CACHE_NAME) {
            return caches.delete(cache);
          }
        })
      );
    })
  );
});