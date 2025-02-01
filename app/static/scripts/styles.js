const baseColors = {
    roads: [204, 0, 0],      // Czerwony
    buildings: [0, 0, 0],    // Czarny
    forests: [0, 102, 0],     // Zielony
    // lakes_ponds: [0, 0, 255], // Niebieski
    lakes_ponds: [0, 0, 255], // Niebieski
    settlements: [102, 0, 0], // brązowy
    meadows_pastures: [0, 255, 128], // Fioletowy
    other_types: [204, 204, 0], // Żółty lekki
    rivers: [0, 0, 255],  // Niebieski
    highway_fields: [170, 0, 0]
};

const colorOpacity = [0.75, 0.875, 1]; // Stałe nasycenia dla kolejnych lat
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
