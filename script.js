document.getElementById("button-Translate").addEventListener("click", function() {
  var textToTranslate = document.getElementById("text-area-From").value;

  // Enviar o texto para o servidor Flask
  fetch("/translate", {
      method: "POST",
      headers: {
          "Content-Type": "application/x-www-form-urlencoded"
      },
      body: "text=" + encodeURIComponent(textToTranslate)
  })
  .then(function(response) {
      return response.text();
  })
  .then(function(data) {
      // Exibir a tradução no campo de texto
      document.getElementById("text-area-To").value = data;
  })
  .catch(function(error) {
      console.log("Ocorreu um erro:", error);
  });
});
