<!doctype html>
<html lang="nl">

<head>
    <meta charset="utf-8">
    <title>Fair play in de VOORBEELD-DIVISIE</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="stylesheet" href="css/normalize.css">
    <link rel="stylesheet" href="css/main.css">
    <link rel="icon" href="favicon.ico" type="image/x-icon" />
    <link rel="preconnect" href="https://fonts.gstatic.com">

    <!-- Hier worden de fonts al voor je ingeladen! -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Faster+One&display=swap" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
        href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap"
        rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto+Mono:ital,wght@0,100..700;1,100..700&display=swap"
        rel="stylesheet">
</head>

<body>

    <div class="container">
        <header>
            <h1>Voorbeeld Divisie</h1>
            <p class="subtitle">Fair-play website</p>
        </header>

        <main>
            <p>De SPORT-bond ziet toe op een eerlijk verloop van de competitie. Onze topsporters dienen een voorbeeld te
                zijn voor de vele amateurs in de sport. Daarom streven we naar <em>fair play</em>; een sportieve omgang
                met elkaar. Daar hoort ook bij dat er weinig overtredingen plaatsvinden tijdens een wedstrijd. Op deze
                website geven we inzicht in het verloop van de competitie tot nu toe. U ziet de wedstrijden met de
                minste overtredingen, maar voor bewustwording brengen we ook de wedstrijden met de <em>meeste</em>
                overtredingen in beeld.</p>
            <div class="row">
                <div class="box half">
                    <h2>Aantal overtredingen:</h2>
                    <p class="number"><?php require_once("./files/total.txt") ?></p>
                </div>
                <div class="box half">
                    <h2>Gemiddelde per wedstrijd</h2>
                    <p class="number"><?php require_once("./files/average.txt") ?></p>
                </div>
            </div>
            <div class="row">
                <div class="box">
                    <h2>Wedstrijden met de meeste overtredingen:</h2>
                    <pre><?php require_once("./files/zwartboek.txt") ?></pre>
                </div>
            </div>
            <div class="row">
                <div class="box">
                    <h2>Wedstrijden met minder dan twee overtredingen(laatste 14 dagen)</h2>
                    <pre><?php require_once("./files/eregalerij.txt") ?></pre>
                </div>
            </div>
        </main>

        <footer>
            <p>Deze website is gemaakt in het kader van een praktijkopdracht bij de opleiding Software Developer, Curio
                Breda.</p>
            <p>&copy; Freek Voermans en Babita Alting.</p>
        </footer>

    </div>

</body>

</html>