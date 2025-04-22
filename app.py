from flask import Flask
from threading import Thread

app = Flask('')

html_code = """
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Termini di Servizio</title>
    <style>
        /* General Styles */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.8;
            margin: 0;
            padding: 0;
            background: linear-gradient(to bottom, #f3f4f6, #e9ecef);
            color: #333;
        }
        header {
            background: linear-gradient(135deg, #007BFF, #0056b3);
            color: white;
            padding: 2.5rem 1rem;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            position: relative;
        }
        header::after {
            content: '';
            position: absolute;
            bottom: -20px;
            left: 50%;
            transform: translateX(-50%);
            width: 80px;
            height: 5px;
            background: white;
            border-radius: 50px;
        }
        header h1 {
            font-size: 3rem;
            margin: 0;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        }
        main {
            max-width: 900px;
            margin: 3rem auto;
            padding: 2.5rem;
            background: white;
            border-radius: 15px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
            animation: fadeIn 1s ease-in-out;
        }
        h2 {
            color: #007BFF;
            border-left: 6px solid #007BFF;
            padding-left: 1rem;
            margin-bottom: 1.5rem;
            font-size: 1.8rem;
        }
        p {
            margin-bottom: 1.5rem;
            font-size: 1.1rem;
        }
        ul {
            margin: 1.5rem 0;
            padding-left: 2rem;
        }
        ul li {
            margin-bottom: 1rem;
            position: relative;
            padding-left: 2rem;
            font-size: 1.1rem;
        }
        ul li::before {
            content: "✔";
            color: #007BFF;
            position: absolute;
            left: 0;
            top: 0.2rem;
            font-size: 1.2rem;
        }
        footer {
            text-align: center;
            margin: 3rem 0 1rem;
            font-size: 0.9rem;
            color: #666;
        }
        footer::before {
            content: '';
            display: block;
            width: 60px;
            height: 4px;
            background: #007BFF;
            margin: 0 auto 1rem;
            border-radius: 50px;
        }
        a {
            color: #007BFF;
            text-decoration: none;
            font-weight: bold;
            transition: color 0.3s ease;
        }
        a:hover {
            color: #0056b3;
            text-decoration: underline;
        }
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>Termini di Servizio</h1>
    </header>
    <main>
        <h2>Introduzione</h2>
        <p>Benvenuto nella pagina dei Termini di Servizio. Utilizzando i nostri servizi, accetti i seguenti termini e condizioni.</p>
        <h2>Linee Guida per l'Uso</h2>
        <ul>
            <li>Non è consentito utilizzare i nostri servizi per attività illegali.</li>
            <li>Rispetta gli altri utenti e la loro privacy.</li>
            <li>Non tentare di hackerare o interrompere i nostri servizi.</li>
        </ul>
        <h2>Modifiche ai Termini</h2>
        <p>Ci riserviamo il diritto di aggiornare questi termini in qualsiasi momento. Ti invitiamo a controllare periodicamente questa pagina per eventuali aggiornamenti.</p>
        <h2>Contattaci</h2>
        <p>Se hai domande su questi termini, contattaci all'indirizzo email <a href="mailto:marinarogiorgio79@gmail.com">marinarogiorgio79@gmail.com</a>.</p>
    </main>
    <footer>
        &copy; 2023 Nome della Tua Azienda. Tutti i diritti riservati.
    </footer>
</body>
</html>
"""

@app.route('/')
def home():
    return html_code

@app.route('/status')
def status():
    return "Il bot è attivo!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

keep_alive()