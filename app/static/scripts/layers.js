import styles from './styles.js';


var groupedOverlays = {
    "Rok 1827": {}, 
    "Rok 1884": {}, 
    "Rok 2009": {}
}




var groupedLayerControl = L.control.groupedLayers(baseMaps, groupedOverlays, { 
    groupCheckboxes: true
}).addTo(map);

// Dodanie komunikatu o ładowaniu
const loadingMessage = document.createElement("div");
loadingMessage.id = "loadingMessage";
loadingMessage.style.position = "fixed";
loadingMessage.style.top = "50%";
loadingMessage.style.left = "50%";
loadingMessage.style.transform = "translate(-50%, -50%)";
loadingMessage.style.background = "rgba(0, 0, 0, 0.8)";
loadingMessage.style.color = "white";
loadingMessage.style.padding = "15px 20px";
loadingMessage.style.fontSize = "18px";
loadingMessage.style.borderRadius = "5px";
loadingMessage.style.zIndex = "1000";
loadingMessage.style.display = "none"; // Ukryty na start
document.body.appendChild(loadingMessage);

// Licznik aktywnych zapytań
let activeRequests = 0;

function fetchAndAddLayer(type, url, style, group, name, zoom) {
    activeRequests++; // Zwiększamy licznik przed zapytaniem

    // Pokazujemy komunikat, jeśli to pierwsze żądanie
    if (activeRequests === 1) {
        loadingMessage.innerText = `Wczytywanie danych...`;
        loadingMessage.style.display = "block";
    }

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
                return;
            }

            if (group === "Rok 1827") {
                layer.addTo(map);
            }

            groupedLayerControl.addOverlay(layer, name, group);
        })
        .catch(error => console.error("Błąd ładowania warstwy:", error))
        .finally(() => {
            activeRequests--; // Zmniejszamy licznik po zakończeniu zapytania

            // Ukrywamy komunikat, gdy wszystkie warstwy się wczytają
            if (activeRequests === 0) {
                // Pokazujemy nowy komunikat po zakończeniu ładowania
                loadingMessage.innerText = "Mapa przedstawia zagospodarowanie w roku 1827, użyj menu po prawej stronie, aby sprawdzić inne lata";
                setTimeout(() => {
                    loadingMessage.style.display = "none"; // Ukrywamy komunikat po 5 sekundach
                }, 5000);
            }
        });
}

// Funkcja do renderowania punktów
function createPointLayer(data, style) {
    return L.geoJSON(data, {
        pointToLayer: function (feature, latlng) {
            return L.circle(latlng, {
                radius: 8,
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


const legendCategories = {
    roads: "Drogi",
    buildings: "Budynki",
    forests: "Lasy",
    lakes_ponds: "Jeziora, stawy",
    settlements: "Zabudowa",
    meadows_pastures: "Łąki, pastwiska",
    other_types: "Pozostałe",
    rivers: "Rzeki",
    highway_fields: "Grunty pod autostradą"
};

// Wybierz najnowszy rok (możesz to zmieniać dynamicznie, jeśli potrzeba)
const latestYear = 2009;

// Tworzenie legendy
var legend = L.control({ position: 'topleft' });

legend.onAdd = function (map) {
    var div = L.DomUtil.create('div', 'legend');
    div.innerHTML += '<h4>Legenda</h4>';

    Object.entries(legendCategories).forEach(([key, label]) => {
        let style = styles.generateStyle(key, latestYear); // Pobierz styl dynamicznie
        let color = style.color; // Pobierz kolor w formacie rgba()

        div.innerHTML += `<i style="background: ${color}"></i> ${label}<br>`;
    });

    return div;
};

// Dodanie legendy do mapy
legend.addTo(map);


setTimeout(() => {
    document.querySelector(".leaflet-control-layers-toggle").click();
}, 500);

fetchAndAddLayer("Polygon", '/api/multi-other-types/1827', styles.generateStyle('other_types', 1827), "Rok 1827", "Pozostałe");
fetchAndAddLayer("Polygon", '/api/multi-other-types/1884', styles.generateStyle('other_types', 1884), "Rok 1884", "Pozostałe");
fetchAndAddLayer("Polygon", '/api/multi-other-types/2009', styles.generateStyle('other_types', 2009), "Rok 2009", "Pozostałe");

fetchAndAddLayer("Polygon", '/api/meadows-pastures/1827', styles.generateStyle('meadows_pastures', 1827), "Rok 1827", "Łąki, pastwiska");
fetchAndAddLayer("Polygon", '/api/meadows-pastures/1884', styles.generateStyle('meadows_pastures', 1884), "Rok 1884", "Łąki, pastwiska");
fetchAndAddLayer("Polygon", '/api/meadows-pastures/2009', styles.generateStyle('meadows_pastures', 2009), "Rok 2009", "Łąki, pastwiska");

fetchAndAddLayer("Polygon", '/api/forests/1827', styles.generateStyle('forests', 1827), "Rok 1827", "Lasy");
fetchAndAddLayer("Polygon", '/api/forests/1884', styles.generateStyle('forests', 1884), "Rok 1884", "Lasy");
fetchAndAddLayer("Polygon", '/api/forests/2009', styles.generateStyle('forests', 2009), "Rok 2009", "Lasy");

fetchAndAddLayer("Polygon", '/api/highway/', styles.generateStyle('highway_fields', 2009), "Rok 2009", "Grunty pod autostradą");

fetchAndAddLayer("Polygon", '/api/lakes-ponds/1827', styles.generateStyle('lakes_ponds', 1827), "Rok 1827", "Jeziora, stawy");
fetchAndAddLayer("Polygon", '/api/lakes-ponds/1884', styles.generateStyle('lakes_ponds', 1884), "Rok 1884", "Jeziora, stawy");
fetchAndAddLayer("Polygon", '/api/lakes-ponds/2009', styles.generateStyle('lakes_ponds', 2009), "Rok 2009", "Jeziora, stawy");

fetchAndAddLayer("Polygon", '/api/settlements/1827', styles.generateStyle('settlements', 1827), "Rok 1827", "Zabudowa");
fetchAndAddLayer("Polygon", '/api/settlements/1884', styles.generateStyle('settlements', 1884), "Rok 1884", "Zabudowa");
fetchAndAddLayer("Polygon", '/api/settlements/2009', styles.generateStyle('settlements', 2009), "Rok 2009", "Zabudowa");

fetchAndAddLayer("Polyline", '/api/rivers/1827', styles.generateStyle('rivers', 1827), "Rok 1827", "Rzeki");
fetchAndAddLayer("Polyline", '/api/rivers/1884', styles.generateStyle('rivers', 1884), "Rok 1884", "Rzeki");
fetchAndAddLayer("Polyline", '/api/rivers/2009', styles.generateStyle('rivers', 2009), "Rok 2009", "Rzeki");

fetchAndAddLayer("Polyline", '/api/roads/1827', styles.generateStyle('roads', 1827), "Rok 1827", "Drogi");
fetchAndAddLayer("Polyline", '/api/roads/1884', styles.generateStyle('roads', 1884), "Rok 1884", "Drogi");
fetchAndAddLayer("Polyline", '/api/roads/2009', styles.generateStyle('roads', 2009), "Rok 2009", "Drogi");

fetchAndAddLayer("Point", '/api/buildings/1827', styles.generateStyle('buildings', 1827), "Rok 1827", "Budynki", 10);
fetchAndAddLayer("Point", '/api/buildings/1884', styles.generateStyle('buildings', 1884), "Rok 1884", "Budynki", 10);
fetchAndAddLayer("Point", '/api/buildings/2009', styles.generateStyle('buildings', 2009), "Rok 2009", "Budynki", 10);

