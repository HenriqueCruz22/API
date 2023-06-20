<?php

require_once 'vendor/autoload.php'; // Certifique-se de ter executado o comando "composer install" para instalar as dependências

use Stichoza\GoogleTranslate\GoogleTranslate;

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Obtenha o texto da solicitação POST
    $text = $_POST['text'];

    // Crie uma instância do GoogleTranslate
    $translator = new GoogleTranslate();

    // Defina o idioma de origem e o idioma de destino
    $translator->setSource('pt');
    $translator->setTarget('en');

    // Traduza o texto
    $translation = $translator->translate($text);

    // Retorne a resposta como JSON
    header('Content-Type: application/json');
    echo json_encode(['translation' => $translation]);
}
