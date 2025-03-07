from flask import Flask, render_template
from modelo import Turma

app = Flask(__name__)


@app.route("/")
def index():
    for aluno in Turma.alunos:
        medias_materias = {}
        for materia, notas in aluno.notas_por_materia.items():
            medias_materias[materia] = sum(notas) / len(notas) if len(notas) > 0 else 0
        aluno.medias_materias = medias_materias
        aluno.media_geral = sum(medias_materias.values()) / len(medias_materias.values()) if medias_materias else 0

    return render_template("boletim.html", Turma=Turma)

if __name__ == "__main__":
    app.run(debug=True)