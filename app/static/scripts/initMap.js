var map = L.map('map', { maxZoom: 30, minZoom: 12}).setView([49.98, 18.55], 13);

// Definicja warstw bazowych
var baseMaps = {
    "OpenStreetMap": L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 18,
        attribution: '&copy; OpenStreetMap contributors'
    }),
    "Ortofoto": L.tileLayer('https://mapy.geoportal.gov.pl/wss/service/PZGIK/ORTO/WMTS/StandardResolution?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&TILEMATRIXSET=EPSG:3857&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}&FORMAT=image/jpeg&LAYERS=ORTOFOTOMAPA', {
        attribution: '&copy; Geoportal',
        maxZoom: 40
    })
};

// Ustaw warstwę domyślną
baseMaps["Ortofoto"].addTo(map);

// Eksport mapy jako zmiennej globalnej
window.map = map;