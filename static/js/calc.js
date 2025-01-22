const display = document.getElementById('display');

// Dodaj wartość do wyświetlacza
function appendToDisplay(value) {
    display.value += value;
}

// Wyczyść wyświetlacz
function clearDisplay() {
    display.value = '';
}

// Usuń ostatni znak
function backspace() {
    display.value = display.value.slice(0, -1);
}

// Wykonaj obliczenia
function calculate() {
    try {
        // Zamień √ na funkcję sqrt() math.js
        const expression = display.value.replace(/√/g, 'sqrt');
        const result = math.evaluate(expression);
        display.value = result;
    } catch (error) {
        display.value = 'Error';
    }
}
