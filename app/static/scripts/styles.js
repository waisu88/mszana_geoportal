const baseColors = {
    roads: [255, 50, 0],      // Czerwony
    buildings: [0, 0, 0],    // Czarny
    forests: [0, 128, 0],     // Zielony
    // lakes_ponds: [0, 0, 255], // Niebieski
    lakes_ponds: [135, 206, 235], // Błękitny
    settlements: [165, 42, 42], // brązowo-czerwony
    meadows_pastures: [255, 192, 203], // Różowy
    other_types: [150, 75, 0], // Brązowy
    rivers: [135, 206, 235],  // Błękitny
};

const colorOpacity = [0.5, 0.75, 1]; // Stałe nasycenia dla kolejnych lat
const years = [1827, 1884, 2009]; // Lata obsługiwane

const baseWeights = {
    roads: 3,
    rivers: 5
}

const zIndexes = {
    buildings: 200,
    roads: 200,
    rivers: 200,
}

const styles = {
    generateStyle: (type, year) => ({
        color: `rgba(${baseColors[type].join(',')},${colorOpacity[years.indexOf(year)]})`,
        weight: baseWeights[type] || 2, // pobierz wagę z baseWeights lub przypisz 2
        zIndex: zIndexes[type] || 400,
        opacity: 1
    })
};

// Eksportuj obiekt styles
export default styles;
