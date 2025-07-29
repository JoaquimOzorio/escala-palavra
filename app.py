from flask import Flask, render_template
from datetime import datetime, timedelta

app = Flask(__name__)

homens = [
    {"nome": "Hugo", "data": "2025-07-22"},
    {"nome": "Danilo", "data": "2025-07-23"},
    {"nome": "Pr. Wefferson", "data": "2025-07-24"},
    {"nome": "Rodrigo Milhomem", "data": "2025-07-25"},
    {"nome": "Wilker", "data": "2025-07-26"},
    {"nome": "Ueslei", "data": "2025-07-27"},
    {"nome": "Diones", "data": "2025-07-28"},
]

@app.route("/")
def index():
    hoje = datetime(2025, 8, 7)
    dias = [{"data": hoje + timedelta(i)} for i in range(len(homens))]
    escala = [{"data": d["data"].strftime("%d/%m/%Y"), "nome": h["nome"]}
              for d, h in zip(dias, homens)]
    return render_template("index.html", escala=escala)

if __name__ == "__main__":
    app.run(debug=True)