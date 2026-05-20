from flask import Flask, request, render_template, render_template_string

app = Flask(__name__)

DADOS_USUARIO = {"nome": "Ana", "email": "ana@email.com"}
LISTA_ALUNOS = ["Bruno", "Camila", "Daniel", "Eduarda"]

def show_the_login_form():
    return render_template_string("""
        <h2>Login</h2>
        <form method="POST">
            <input type="text" name="usuario" placeholder="Usuário"><br><br>
            <input type="password" name="senha" placeholder="Senha"><br><br>
            <button type="submit">Entrar</button>
        </form>
    """)

def do_the_login():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')

    if usuario == 'davi' and senha == '12400149':
        return f"<h1>Bem-vindo, {usuario}!</h1>"
    else:
        return "<h1>Login inválido</h1>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

@app.route('/')
def index():
    return render_template('index2.html', nome="Carlos", idade=25)

@app.route('/3')
def exercicio_3():    
    return render_template('index3.html', usuario=DADOS_USUARIO)

@app.route('/4')
def exercicio_4():    
    return render_template('index4.html', alunos=LISTA_ALUNOS)

@app.route('/5')
def exercicio_5():    
    nota_aluno = 7.5
    return render_template('index5.html', nota=nota_aluno)

if __name__ == "__main__":
    app.run(debug=True)