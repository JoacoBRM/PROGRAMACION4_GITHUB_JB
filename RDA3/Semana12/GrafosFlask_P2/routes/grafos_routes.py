from flask import Blueprint, render_template, request
from grafo_utils import grafo_a_imagen, camino_optimo_con_costera, obtener_ciudades, grafo_a_imagen, grafo_a_imagen_camino

starter_bp = Blueprint('grafos', __name__, url_prefix='/grafos')

@starter_bp.route('/')
def starter():
    return render_template("grafos/starter.html")

@starter_bp.route('/calcular_camino', methods=['GET', 'POST'])
def calcular_camino():
    ciudades = obtener_ciudades()
    resultado = None
    if request.method == 'POST':
        origen = request.form.get('origen')
        destino = request.form.get('destino')
        if origen and destino and origen != destino:
            resultado = camino_optimo_con_costera(origen, destino)
    return render_template("grafos/calcular_camino.html", ciudades=ciudades, resultado=resultado)

@starter_bp.route('/camino')
def ver_camino():
    resultado = camino_optimo_con_costera("Ibarra", "Loja")
    return render_template("grafos/camino.html", resultado=resultado)

@starter_bp.route('/grafo_imagen')
def grafo_imagen():
    return grafo_a_imagen()

@starter_bp.route('/grafo_imagen_camino')
def grafo_imagen_camino():
    camino = request.args.getlist('camino')
    return grafo_a_imagen_camino(camino)
