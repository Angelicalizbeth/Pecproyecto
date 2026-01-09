from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bienvenida')
def bienvenida():
    nombre = request.args.get('nombre')
    grupo = request.args.get('grupo')
    carrera = request.args.get('carrera')
    return render_template('bienvenida.html', nombre=nombre, grupo=grupo, carrera=carrera)

@app.route('/introduccion')
def introduccion():
    return render_template('introduccion.html')

@app.route('/como_empezar')
def como_empezar():
    return render_template('comoempezar.html')

@app.route('/beneficios')
def beneficios():
    return render_template('beneficios.html')

@app.route('/programas')
def programas():
    return render_template('programas.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/quees')
def quees():
    return render_template('quees.html')

@app.route('/contactos')
def contactos():
    return render_template('contactos.html')

@app.route('/reciclaje_inteligente')
def reciclaje_inteligente():
    return render_template('reciclaje_inteligente.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
