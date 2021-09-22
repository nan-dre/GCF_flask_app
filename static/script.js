function showHide(event) {
  event.preventDefault();

  let form = event.target;
  let loadingDiv = getDocByClass('loading-container');
  let loadingQuoteDiv = getDocByClass('loading-quote');
  loadingQuoteDiv.innerHTML = generateRandomQuote(); // Generate random quote

  toggle(loadingDiv, form); // Toggling to loading state

  // Sending async form...
  fetch(form.action, {
    method: form.method,
    body: new FormData(form)
  }).then((res) => {
    // Parsing the response
    res.text().then((res) => {
      let resultContainer = getDocByClass('result-state');
      let responseContainer = getDocByClass('response');
      let tryAgainButton = getDocByClass('try-again');

      toggle(resultContainer, loadingDiv);

      responseContainer.innerHTML = res; // Add response to HTML
      tryAgainButton.addEventListener('click', () => toggle(form, resultContainer)) // Go back to first state
    });
  });
}

function getDocByClass(className) {
  const _ = document.getElementsByClassName(className)
  return _ ? _[0] : undefined;
}

function toggle(toDisplay, toHide, display = 'flex') {
  toDisplay.style.display = display;
  toHide.style.display = 'none';
}

// Random quote. feel free to add more
const loadingQuotes = [
  'Making the best Manea out there...',
  'Wait a bit, Florin Salam doesn\'t work for free...',
  'Boti Mocanu is thinking...'
]

function generateRandomQuote() {
  return loadingQuotes[Math.floor(Math.random() * loadingQuotes.length)];
}