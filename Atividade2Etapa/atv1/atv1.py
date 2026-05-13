from flask import Flask

app = Flask(__name__)

@app.route("/")
def decorator():
    return "Um decorator em Python é uma função que envolve outra função para modificar ou estender seu comportamento sem alterar o código original.\n" \
    "Serve para reutilizar código e separar tarefas, como checar permissões ou registrar " \
    "logs. No Flask, o decorator @app.route('/') serve para criar rotas, vinculando uma URL específica do navegador à " \
    "função que deve ser executada quando a página é acessada."


if __name__ == "__main__":
    app.run(debug=True)