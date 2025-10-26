from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def hello_professor():
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Práctica CI/CD - Alexis Sisneros</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #2c3e50, #4ca1af);
                color: white;
                text-align: center;
            }
            .container {
                padding: 40px;
                border-radius: 15px;
                background-color: rgba(0, 0, 0, 0.2);
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
                border: 1px solid rgba(255, 255, 255, 0.1);
            }
            h1 {
                font-size: 3em;
                margin: 0;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
            }
            p {
                font-size: 2em;
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>¡Hola, profe! &#x1F60A;</h1>
            <p>Esta es la app que estamos desplegando.</p>
        </div>
    </body>
    </html>
    """
    return Response(html_content, mimetype='text/html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)