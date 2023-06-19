const textareaFrom = document.querySelector("#text-area-From");
const textareaTo = document.querySelector("#text-area-To");
const btnTranslate = document.querySelector("#button-Translate");
const selects = document.querySelectorAll("select");

const countries = {
  "en-GB": "Inglês",
  "es-ES": "Espanhol",
  "it-IT": "Italiano",
  "ja-JP": "Japonês",
  "pt-BR": "Português",
};

selects.forEach((tag) => {
  for (let country in countries) {
    let selected;
    if (tag.className.includes("select-From") && country == "pt-BR") {
      selected = "selected";
    } else if (tag.className.includes("select-To") && country == "en-GB") {
      selected = "selected";
    }

    const option = `<option value="${country}" ${selected}>${countries[country]}</option>`;

    tag.insertAdjacentHTML("beforeend", option);
  }
});

btnTranslate.addEventListener("click", () => {
  if (textareaFrom.value) {
    loadTranslation();
  } else {
    textareaTo.value = "";
  }
});

function loadTranslation() {
  fetch(
    `https://api.mymemory.translated.net/get?q=${textareaFrom.value}&langpair=${selects[0].value}|${selects[1].value}`
  )
    .then((res) => res.json())
    .then((data) => {
      textareaTo.value = data.responseData.translatedText;
    });
}