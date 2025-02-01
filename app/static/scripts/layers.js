
import styles from './styles.js';


var groupedOverlays = {
    "Rok 1827": {}, 
    "Rok 1884": {}, 
    "Rok 2009": {}
}

map.on('click', function(e) {
    // Pobranie aktualnego poziomu zoomu
    var currentZoom = map.getZoom();
    
    // Wyświetlenie poziomu zoomu w konsoli
    console.log('Aktualny poziom zoomu:', currentZoom);
});



var groupedLayerControl = L.control.groupedLayers(baseMaps, groupedOverlays, { 
    groupCheckboxes: true
}).addTo(map);

function fetchAndAddLayer(type, url, style, group, name, zoom) {
    fetch(url)
        .then(response => response.json())
        .then(data => {
            let layer;

            // Wybór odpowiedniej funkcji do renderowania w zależności od typu
            if (type === 'Point') {
                layer = createPointLayer(data, style);
            } else if (type === 'Polyline') {
                layer = createLineLayer(data, style);
            } else if (type === 'Polygon') {
                layer = createPolygonLayer(data, style);
            } else {
                console.warn(`Nieobsługiwany typ geometrii: ${type}`);
                return; // Zakończ, jeśli typ nie jest obsługiwany
            }

            // Dodanie warstwy do kontrolki grupowania
            groupedLayerControl.addOverlay(layer, name, group);
        });
}

// Funkcja do renderowania punktów
function createPointLayer(data, style) {
    return L.geoJSON(data, {
        pointToLayer: function (feature, latlng) {
            return L.circleMarker(latlng, {
                radius: 6,
                fillColor: style.color,
                color: style.color,
                weight: style.weight,
                opacity: style.opacity,
                fillOpacity: style.opacity*0.75,
                zIndex: style.zIndex
            });
        }
    });
}

// Funkcja do renderowania linii
function createLineLayer(data, style) {
    return L.geoJSON(data, {
        style: function (feature) {
            return {
                color: style.color,
                weight: style.weight,
                opacity: style.opacity,
                zIndex: style.zIndex
            };
        }
    });
}

// Funkcja do renderowania poligonów
function createPolygonLayer(data, style) {
    return L.geoJSON(data, {
        style: function (feature) {
            return {
                color: style.color,
                fillColor: style.color,
                weight: style.weight,
                opacity: style.opacity,
                fillOpacity: style.opacity*0.75,
                zIndex: style.zIndex
            };
        }
    });
}



const imageUrl = '/static/static/messtishblatter.png';

// Zakładam, że wynikowe współrzędne to (pomiń jeśli używasz rzeczywistych danych)
const bounds = [[50.0147123, 18.4950524], [49.9463421, 18.6120258]];

// Dodanie nakładki na mapę
var mess = L.imageOverlay(imageUrl, bounds);

const mszana1827 = '/static/static/urmesstishblatter.png';

const bounds1827 = [[50.0147105, 18.4950581], [49.9463596, 18.6120213]];

var urm = L.imageOverlay(mszana1827, bounds1827);

groupedLayerControl.addOverlay(urm, "<span class='podklad'>Urmesstischblatter</span>", "Rok 1827")
groupedLayerControl.addOverlay(mess, "<span class='podklad'>Messtischblatter</span>", "Rok 1884")


fetchAndAddLayer("Point", '/api/buildings/1827', styles.generateStyle('buildings', 1827), "Rok 1827", "Budynki", 10);
fetchAndAddLayer("Point", '/api/buildings/1884', styles.generateStyle('buildings', 1884), "Rok 1884", "Budynki", 10);
fetchAndAddLayer("Point", '/api/buildings/2009', styles.generateStyle('buildings', 2009), "Rok 2009", "Budynki", 10);

fetchAndAddLayer("Polygon", '/api/lakes-ponds/1827', styles.generateStyle('lakes_ponds', 1827), "Rok 1827", "Jeziora, stawy");
fetchAndAddLayer("Polygon", '/api/lakes-ponds/1884', styles.generateStyle('lakes_ponds', 1884), "Rok 1884", "Jeziora, stawy");
fetchAndAddLayer("Polygon", '/api/lakes-ponds/2009', styles.generateStyle('lakes_ponds', 2009), "Rok 2009", "Jeziora, stawy");

fetchAndAddLayer("Polygon", '/api/settlements/1827', styles.generateStyle('settlements', 1827), "Rok 1827", "Zabudowa");
fetchAndAddLayer("Polygon", '/api/settlements/1884', styles.generateStyle('settlements', 1884), "Rok 1884", "Zabudowa");
fetchAndAddLayer("Polygon", '/api/settlements/2009', styles.generateStyle('settlements', 2009), "Rok 2009", "Zabudowa");

fetchAndAddLayer("Polygon", '/api/forests/1827', styles.generateStyle('forests', 1827), "Rok 1827", "Lasy");
fetchAndAddLayer("Polygon", '/api/forests/1884', styles.generateStyle('forests', 1884), "Rok 1884", "Lasy");
fetchAndAddLayer("Polygon", '/api/forests/2009', styles.generateStyle('forests', 2009), "Rok 2009", "Lasy");

fetchAndAddLayer("Polygon", '/api/meadows-pastures/1827', styles.generateStyle('meadows_pastures', 1827), "Rok 1827", "Łąki, pastwiska");
fetchAndAddLayer("Polygon", '/api/meadows-pastures/1884', styles.generateStyle('meadows_pastures', 1884), "Rok 1884", "Łąki, pastwiska");
fetchAndAddLayer("Polygon", '/api/meadows-pastures/2009', styles.generateStyle('meadows_pastures', 2009), "Rok 2009", "Łąki, pastwiska");

fetchAndAddLayer("Polygon", '/api/multi-other-types/1827', styles.generateStyle('other_types', 1827), "Rok 1827", "Pozostałe");
fetchAndAddLayer("Polygon", '/api/multi-other-types/1884', styles.generateStyle('other_types', 1884), "Rok 1884", "Pozostałe");
fetchAndAddLayer("Polygon", '/api/multi-other-types/2009', styles.generateStyle('other_types', 2009), "Rok 2009", "Pozostałe");

fetchAndAddLayer("Polyline", '/api/rivers/1827', styles.generateStyle('rivers', 1827), "Rok 1827", "Rzeki");
fetchAndAddLayer("Polyline", '/api/rivers/1884', styles.generateStyle('rivers', 1884), "Rok 1884", "Rzeki");
fetchAndAddLayer("Polyline", '/api/rivers/2009', styles.generateStyle('rivers', 2009), "Rok 2009", "Rzeki");

fetchAndAddLayer("Polyline", '/api/roads/1827', styles.generateStyle('roads', 1827), "Rok 1827", "Drogi");
fetchAndAddLayer("Polyline", '/api/roads/1884', styles.generateStyle('roads', 1884), "Rok 1884", "Drogi");
fetchAndAddLayer("Polyline", '/api/roads/2009', styles.generateStyle('roads', 2009), "Rok 2009", "Drogi");

