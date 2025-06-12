from flask import Flask, render_template, request
from operaciones import Calculadora

calc = Calculadora()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculadora', methods=['GET', 'POST'])
def calculadora():
    resultado = None
    numero1 = ''
    numero2 = ''
    operacion = ''

    if request.method == 'POST':
        try:
            numero1 = request.form.get('numero1', '')
            numero2 = request.form.get('numero2', '')
            operacion = request.form.get('operacion')

            n1 = float(numero1)
            n2 = float(numero2)

            if operacion == "sumar":
                resultado = calc.suma(n1, n2)
            elif operacion == "restar":
                resultado = calc.resta(n1, n2)
            elif operacion == "multiplicar":
                resultado = calc.multiplicacion(n1, n2)
            elif operacion == "dividir":
                resultado = calc.division(n1, n2)
            else:
                resultado = "¡Operación no válida!"

        except Exception as e:
            resultado = f"Error: {str(e)}"

    return render_template(
        'calculadora.html',
        resultado=resultado,
        numero1=numero1,
        numero2=numero2,
        operacion=operacion
    )


if __name__ == '__main__':
    app.run(debug=True)
 