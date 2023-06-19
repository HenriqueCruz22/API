document.getElementById("button-Translate").addEventListener("click", function() {
    var textToTranslate = document.getElementById("text-area-From").value;
  
    // Enviar o texto para o código Python
    fetch("/translate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ text: textToTranslate })
    })
    .then(function(response) {
      return response.json();
    })
    .then(function(data) {
      // Exibir a tradução no campo de texto
      document.getElementById("text-area-To").value = data.translation;
    })
    .catch(function(error) {
      console.log("Ocorreu um erro:", error);
    });
  });
  