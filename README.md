# Flask-Dugga – Övningstentamen

## Klona projektet

1. Klona ner med git clone in i en mapp och öppna i VSCode
2. Skapa en virtuell miljö
    - python -m venv venv
3. Installera beroenden från requirements.txt
    - pip install -r requirements.txt

Lycka till!

Uppskattad tidsåtgång: ca 1h för installation och bekanta er med koden. Lös en uppgift i taget per branch. Ca 3-5h för att implementera funktionaliteten. Dessa tider är mina uppskattningar men det är väldigt svårt för mig att veta hur lång tid det tar för er och vad som känns rimligt.
Ni får gärna göra denna övningstenta och ta tid på er själva så att jag kan sätta en rimlig gräns på tentamen senare. Tentamen kommer ungefär vara i denna storleksordning plus några kortare flervalsfrågor om HTML, JS och agilt arbete.

## Instruktioner
Varje uppgift ska lösas i en egen branch vilket betyder att ni ska ta med arbetet från föregående branch när ni skapar en ny. Kom därför ihåg att köra en commit, med ett meddelande, efter varje uppgift!

Applikationen saknar funktionalitet och innehåller avsiktliga fel.
Dessa ska identifieras och rättas. 

Ingen databas ska installeras.

## Uppgifter

### Uppgift 1.1: 
Skapa en Flask-applikation i app.py med följande funktionalitet:

1. En route som ger oss en startsida som visar texten "Välkommen till min Flask-app!" inuti ett lämpligt html-element.
1. En "Om oss"-sida som visar information om webbplatsen (använd lorem för att få text)
1. Applikationen ska köra i debug-läge när den startas

### Uppgift 1.2
Skapa en User-klass och generera testdata:
1. Skapa en klass, antingen klassisk Python-klass eller @dataclass, som innehåller följande attribut. OBS! Detta ska inte vara en databasmodell utan endast en vanlig klass. 
    - id (int)
    - first name (str)
    - last name (str)
    - email (str)
    - city (str)
1. Skapa en funktion get_random_users() som returnerar en lista med slumpat antal User-objekt med fejkad data från Faker eller manuell fejkdata.
1. Skapa en route /users som visar alla användare i en tabell. Styling är inte nödvändigt.
- Tabellen ska innehålla en header med kolumnnamn och rada upp samtliga användare
- Paginering är inte nödvändigt eller sortering är inte nödvändigt.

### Uppgift 1.3:
Skapa filen users.html med följande:

1. En HTML-struktur som ärver från bas-template och lägger till sitt eget innehåll.
1. En rubrik med texten "Alla användare"
1. En tabell som visar alla användare med kolumnerna: ID, Namn (dvs first name + last name), Email, Stad

### Uppgift 1.4: Navbar
1. Lägg till en komponent, _navbar.html eller navbar.html, som innehåller länkar till dina routes. Lägg in denna komponent inuti bas-templaten.

### Uppgift 1.5: CSS-styling
1. Länka CSS-filen inuti static-mappen i din bas-template.
1. Lägg till css reset överst i css-filen.
1. Ta bort underline på alla a-länkar.
1. Lägg till så att bakgrundsfärgen på html är i en valfri grå nyans.

### Uppgift 2.1: Bugg-fix
1. inuti app.py finns det en funktion user_detail som inte fungerar som den ska pga felaktig kod. Lös buggarna som finns. När routen är korrekt skriven ska den leda till en profilsida som visar kundinfo. Styling behövs inte utan endast information på skärmen i ett p-element.

### Uppgift 2.2: Bugg-fix
1. Det finns en user_detail_faulty-template som inte fungerar som den ska.
    - Ordna så att den ärver layout från bas-templaten
    - Fixa jinja-koden så att den skriver ut rätt information
    - Du kan använda den första usern från get_random_user()
    - Uppdatera din navbar så att även denna länk finns med.


### Uppgift 3: Javascript
Skapa en answers.js-fil som du länkar till i din head-tagg. Lös följande uppgifter och skriv ut resultatet till konsolen via console.log() efter varje uppgift:
1. Skapa en funktion greet(name) som returnerar "Hej, name" mha en template-string (javascripts version av f-string)
1. Skapa en array numbers med siffrorna 1, 2, 3, 4, 5. Skriv kod som:
    - Lägger till siffran 6 i slutet av arrayen. Siffran 6 ska alltid läggas till i slutet, oavsett hur många gånger funktionen anropas.
    - Skriver ut arrayens längd till konsolen
1. Skriv en funktion checkAge(age) som:
    - Returnerar "Vuxen" om age är 18 eller högre
    - Returnerar "Minderårig" annars
1. Skriv en funktion checkAgeTernary(age) som gör samma som ovan, men med en ternary (dvs med ? : syntax ? = om ja, : = annars):
1. Skriv en for-loop som skriver ut alla jämna siffror från paramterarna start och end i konsolen
    - exempel: att köra start=0, end=4 ska skriva ut siffrorna 0, 2 och 4
  


# English instructions - Flask-Dugga – Practice Exam

## Clone the project

1. Clone the repository using `git clone` into a folder and open it in VSCode
2. Create a virtual environment

   * `python -m venv venv`
3. Install dependencies from `requirements.txt`

   * `pip install -r requirements.txt`

Good luck!

Estimated time required: about **1 hour** for installation and to familiarize yourselves with the code. Solve **one task at a time per branch**. About **3–5 hours** to implement the functionality. These times are my estimates, but it is very difficult for me to know how long it will take for you or what feels reasonable.

You are welcome to do this practice exam and time yourselves so that I can set a reasonable limit for the actual exam later. The exam will be roughly of this size, plus a few shorter multiple-choice questions about HTML, JavaScript, and agile work.

## Instructions

Each task must be solved in its **own branch**, which means you should include the work from the previous branch when creating a new one. Therefore, remember to make a **commit with a message after each task**!

The application lacks functionality and contains **intentional errors**.
These should be identified and fixed.

No database should be installed.

## Tasks

### Task 1.1

Create a Flask application in `app.py` with the following functionality:

1. A route that gives us a start page showing the text **"Welcome to my Flask app!"** inside a suitable HTML element
2. An **“About us”** page that shows information about the website (use lorem ipsum for text)
3. The application should run in **debug mode** when started

### Task 1.2

Create a `User` class and generate test data:

1. Create a class, either a classic Python class or an `@dataclass`, containing the following attributes.
   **Note:** This should *not* be a database model, only a regular class.

   * id (int)
   * first name (str)
   * last name (str)
   * email (str)
   * city (str)
2. Create a function `get_random_users()` that returns a list with a random number of `User` objects with fake data from Faker or manually created fake data
3. Create a route `/users` that displays all users in a table. Styling is not required.

   * The table should contain a header with column names and list all users
   * Pagination and sorting are not required

### Task 1.3

Create the file `users.html` with the following:

1. An HTML structure that inherits from the base template and adds its own content
2. A heading with the text **"All users"**
3. A table that shows all users with the columns:
   **ID, Name (i.e. first name + last name), Email, City**

### Task 1.4: Navbar

1. Add a component, `_navbar.html` or `navbar.html`, that contains links to your routes. Insert this component inside the base template.

### Task 1.5: CSS Styling

1. Link the CSS file inside the `static` folder in your base template
2. Add a CSS reset at the top of the CSS file
3. Remove the underline from all `<a>` links
4. Set the background color of the `html` element to a chosen shade of gray

### Task 2.1: Bug fix

1. Inside `app.py` there is a function `user_detail` that does not work correctly due to faulty code. Fix the bugs. When the route is correctly written, it should lead to a profile page that shows customer information. Styling is not required—only display the information on the screen in a `<p>` element.

### Task 2.2: Bug fix

1. There is a `user_detail_faulty` template that does not work correctly.

   * Make it inherit the layout from the base template
   * Fix the Jinja code so that it outputs the correct information
   * You can use the first user from `get_random_user()`
   * Update your navbar so that this link is also included

### Task 3: JavaScript

Create an `answers.js` file and link it in your `<head>` tag. Solve the following tasks and print the result to the console using `console.log()` after each task:

1. Create a function `greet(name)` that returns **"Hello, name"** using a template string (JavaScript’s version of an f-string)
2. Create an array `numbers` with the values `1, 2, 3, 4, 5`. Write code that:

   * Adds the number `6` to the end of the array. The number 6 should always be added to the end, regardless of how many times the function is called
   * Prints the length of the array to the console
3. Write a function `checkAge(age)` that:

   * Returns **"Adult"** if `age` is 18 or higher
   * Returns **"Minor"** otherwise
4. Write a function `checkAgeTernary(age)` that does the same as above, but using a ternary operator (`? :`)
5. Write a `for` loop that prints all even numbers between the parameters `start` and `end` to the console

   * Example: running with `start = 0`, `end = 4` should print `0`, `2`, and `4`

