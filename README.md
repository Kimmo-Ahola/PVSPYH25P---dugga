# Flask-Dugga – Övningstentamen

## Klona projektet

1. Gör en fork av repot
2. Skapa en virtuell miljö
    - python -m venv venv
3. Installera beroenden från requirements.txt
    - pip install -r requirements.txt

Applikationen saknar funktionalitet och innehåller avsiktliga fel.
Dessa ska identifieras och rättas. Ingen databas ska installeras.

Lycka till!

Uppskattad tidsåtgång: ca 1h för installation och bekanta er med koden. Lös en uppgift i taget per branch. Ca 3h för att implementera funktionaliteten.

## Instruktioner
Varje uppgift ska lösas i en egen branch. Ni behöver inte skapa issues på github eller liknande utan bara nya branches.

## Uppgifter

Uppgift 1.1: Skapa en Flask-applikation i app.py med följande funktionalitet:

1. En route som ger oss en startsida som visar texten "Välkommen till min Flask-app!" inuti ett lämpligt html-element.
1. En "Om oss"-sida som visar information om webbplatsen (använd lorem för att få text)
1. Applikationen ska köra i debug-läge när den startas

Uppgift 1.2
Skapa en User-klass och generera testdata:
1. Skapa en klass, antingen klassisk Python-klass eller @dataclass, som innehåller följande attribut. OBS! Detta ska inte vara en databasmodell utan endast en vanlig klass. 
    - id (int)
    - first name (str)
    - last name (str)
    - email (str)
    - city (str)
1. Skapa en funktion get_random_users() som returnerar en lista med slumpat antal User-objekt med fejkad data från Faker
1. Skapa en route /users som visar alla användare i en tabell. Styling är inte nödvändigt.
- Tabellen ska innehålla en header med kolumnnamn och rada upp samtliga användare
- Paginering är inte nödvändigt

Uppgift 1.3:
Skapa filen users.html med följande:

1. En HTML-struktur som ärver från bas-template och lägger till sitt eget innehåll.
1. En rubrik med texten "Alla användare"
1. En tabell som visar alla användare med kolumnerna: ID, Namn, Email, Stad

Uppgift 1.4: Navbar
1. Lägg till en komponent, _navbar.html eller navbar.html, som innehåller länkar till dina routes. Lägg in denna komponent inuti bas-templaten.

Uppgift 1.6: CSS-styling
1. Länka CSS-filen inuti static-mappen i din bas-template.
1. Lägg till css reset överst i css-filen.
1. Ta bort underline på alla a-länkar.
1. Lägg till så att bakgrundsfärgen på html är i en valfri grå nyans.

Uppgift 2.1: Bugg-fix
1. inuti app.py finns det en funktion user_detail som inte fungerar som den ska pga felaktig kod. Lös buggarna som finns. När routen är korrekt skriven ska den leda till en profilsida som visar kundinfo. Styling behövs inte utan endast information på skärmen i ett p-element.

Uppgift 2.2: Bugg-fix
1. Det finns en user_detail_faulty-template som inte fungerar som den ska.
    - Ordna så att den ärver layout från bas-templaten
    - Fixa jinja-koden så att den skriver ut rätt information
    - Du kan använda den första usern från get_random_user()
    - Uppdatera din navbar så att även denna länk finns med.


Uppgift 3: Javascript
1. Skapa en answers.js-fil som du länkar till i din head-tagg. Lös följande uppgifter och skriv ut resultatet till konsolen via console.log(ditt resultat här):
1. Skapa en funktion greet(name) som returnerar "Hej, name" mha en template-string (javascripts version av f-string)
1. Skapa en array numbers med siffrorna 1, 2, 3, 4, 5. Skriv kod som:
    - Lägger till siffran 6 i slutet av arrayen. Siffran 6 ska alltid läggas till i slutet, oavsett hur många gånger funktionen anropas.
    - Skriver ut arrayens längd till konsolen
1. Skriv en funktion checkAge(age) som:
    - Returnerar "Vuxen" om age är 18 eller högre
    - Returnerar "Minderårig" annars
1. Skriv en funktion checkAgeTernary(age) som gör samma som ovan, men med en ternary (? :):
1. Skriv en for-loop som skriver ut alla jämna siffror från paramterarna start och end i konsolen
    - exempel: att köra start=0, end=4 ska skriva ut siffrorna 0, 2 och 4