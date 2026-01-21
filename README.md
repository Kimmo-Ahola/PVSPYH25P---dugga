# Flask Dugga – YH

## Starta projektet

1. Klona repot
2. Skapa virtuellt environment
3. Installera beroenden
4. Starta applikationen

Applikationen innehåller avsiktliga fel.
Dessa ska identifieras och rättas.

Lycka till!

## Uppgifter

Uppgift 1.1: Grundläggande Flask-applikation (15p)
Skapa en Flask-applikation i app.py med följande funktionalitet:

1. En route som ger oss en startsida som visar texten "Välkommen till min Flask-app!" inuti ett lämpligt html-element.
1. En "Om oss"-sida som visar information om webbplatsen (använd lorem för att få text)
1. Applikationen ska köra i debug-läge när den startas

Uppgift 1.2: Användarklassen och fejkad data (15p)
Skapa en User-klass och generera testdata:
1. Skapa en klass, antingen klassisk Python-klass eller @dataclass, som innehåller följande attribut:
- id (int)
- first name (str)
- last name (str)
- email (str)
- city (str)
OBS! Detta ska inte vara en databasmodell utan endast en vanlig klass.
1. Skapa en funktion get_random_users() som returnerar en lista med slumpat antal User-objekt med fejkad data från Faker
1. Skapa en route /users som visar alla användare i en tabell. Styling är inte nödvändigt.
- Tabellen ska innehålla en header med kolumnnamn och rada upp samtliga användare
- Paginering är inte nödvändigt

Uppgift 1.3: HTML-template för användarlista (15p)
Skapa filen templates/users.html med följande:

1. En HTML-struktur med <!DOCTYPE>, <html>, <head> och <body>
1. En rubrik med texten "Alla användare"
1. En tabell som visar alla användare med kolumnerna: ID, Namn, Email, Stad

Uppgift 1.4: Navbar
1. Lägg till en komponent, _navbar.html eller navbar.html som innehåller länkar till dina routes.

Uppgift 1.4: CSS-styling (10p)
1. Länka CSS-filen inuti static-mappen i din bas-template.
1. Lägg till css reset överst i css-filen.
1. Ta bort underline på alla a-länkar.
1. Lägg till så att bakgrundsfärgen på html är i en valfri grå nyans.

