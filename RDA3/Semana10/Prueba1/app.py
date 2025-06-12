from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html', nombre='Joaquin')

@app.route('/base.html')
def base():
    return render_template('base.html', nombre='Joaquin')  # o texto plano si prefieres

if __name__ == '__main__':
    app.run(debug=True)
