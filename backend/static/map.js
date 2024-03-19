var map = L.map('map', {
    center: [51.505, -0.09],
    zoom: 11
});
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);
L.marker([51.5666, -0.09]).addTo(map);
L.marker([51.5122, -0.09]).addTo(map);

// var points = JSON.parse(document.getElementById('coord_data').textContent)