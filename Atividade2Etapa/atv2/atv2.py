from flask import Flask

app = Flask(__name__)

@app.route("/curriculo")
def curriculo():
    return '''
    <html>
    <body>
    <center>
        <h1>Davi Duarte Mendes</h1>
        <br>
        <div>daviduartemendes@gmail.com | (31) 99999-9999 | 17 anos<div>
    </center>
    <br>

    <hr>

    <h2>Formação Academica</h2>

    <div "font-size: 30px">Ensino Técnico: Colégio COTEMIG<div>
    <div>2024 - 2026<div>

    <hr>

    <h2>Experiência Profissional</h2>

    <div>ASSISTENTE ADMINISTRATIVO<div>    
    <div>MRV | 2025 - Ongoing

    <hr>

    <h2>Habilidades e Competências</h2>
    <div style="display: flex">
        <ul><div style="font-weight: bold">Linguagens de Programação</div>
            <li>Python</li>
            <li>JavaScript</li>
            <li>MySQL</li>
            <li>PHP</li>
            <li>C#</li>
            <li>CSS</li>
        </ul>
        <ul><div style="font-weight: bold">Habilidades</div>
            <li>Trabalho em Equipe</li>
            <li>Resolução de Problemas</li>
            <li>Gestão de Tempo</li>
            <li>Ferramentas Específicas</li>
            <li>Idioma (Inglês)</li>
        </ul>
    </div>
    <hr>




'''   
if __name__ == "__main__":
    app.run(debug=True)