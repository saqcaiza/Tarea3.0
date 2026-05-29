from flask import Flask, render_template_string

app = Flask(__name__)

# Plantilla HTML integrada (para mantener todo en un solo archivo)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Página en Flask</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f4f7f6;
            color: #333;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            text-align: center;
            padding: 30px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2ca58d;
        }
        p {
            font-size: 1.1em;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>¡Hola desde Flask! 🚀</h1>
        <p>Esta página se está sirviendo desde un único archivo <code>app.py</code>.</p>
        <p>Estás navegando en el puerto <strong>6000</strong>.</p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    # Renderizamos la plantilla directamente desde el string
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    # Configurado para correr en el puerto 6000 y con el modo debug activado
    app.run(debug=True, port=5000)