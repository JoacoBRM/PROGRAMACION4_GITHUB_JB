from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('base.html', nombre='Joaquin')

@app.route('/base.html')
def base():
    return 'Hola Mundo'


if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='127.0.0.1', port=5000, debug=True)
    