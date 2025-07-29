# Escala de palavras para grupo de WhatsApp com Flask e HTML
from datetime import datetime, timedelta
import calendar
from flask import Flask, render_template, request

app = Flask(__name__)

# Dados fixos
dias_fixos = {
    'saturday': 'Pr. João Claudio',
    'sunday': 'Culto'
}

restricoes = {
    'Ricardo Manuel': {'dia_semana': 'friday', 'fim_do_mes': True},
    'Rodrigo Milhomem': {'dia_semana': 'friday'},
}

participantes = [
    'Diones', 'Samuel Henrique', 'Paulo Uchoa', 'Pr. Ueslei', 'Pr. Jovem',
    'Hugo', 'Ricardo Manuel', 'Samuel Carneiro', 'Wilker', 'Pr. Virley',
    'Pr. Dionel', 'Jorge Olimpio', 'Pr. Wefferson', 'Fabrício',
    'Rodrigo Milhomem', 'Danilo', 'Cleyton', 'Malcon'
]

ultimos = [
    'Hugo', 'Danilo', 'Pr. Wefferson', 'Rodrigo Milhomem', 'Pr. João Claudio',
    'Jorge Olimpo', 'Pr. Dionel', 'Wilker', 'Pr. Jovem', 'Ricardo Manuel',
    'Pr. João Claudio', 'Samuel Carneiro', 'Pr. Ueslei', 'Ricardo Manuel'
]

fila = [p for p in participantes if p not in ultimos] + ultimos


def gerar_escala(participantes, ultimos_que_falaram, data_inicio):
    fila = [p for p in participantes if p not in ultimos_que_falaram]
    fila += [p for p in ultimos_que_falaram if p in participantes]

    escala = []
    data = data_inicio
    fila_index = 0

    while len(escala) < len(participantes):
        if data.weekday() in [5, 6]:  # sábado ou domingo
            if data.weekday() == 5:
                nome = "Pr. João Claudio"
            else:
                nome = "Culto"
        else:
            if fila_index < len(fila):
                nome = fila[fila_index]
                fila_index += 1
            else:
                break  # sem mais nomes na fila
        escala.append((data.strftime("%d/%m/%Y"), nome))
        data += timedelta(days=1)
    return escala



@app.route('/', methods=['GET', 'POST'])
def index():
    escala = {}
    if request.method == 'POST':
        data_inicio = request.form['data_inicio']
        dias = int(request.form.get('dias', 14))
        escala = gerar_escala(data_inicio, dias)
    return render_template('index.html', escala=escala)


if __name__ == '__main__':
    app.run(debug=True)
