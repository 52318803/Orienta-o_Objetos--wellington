#onde os dados dos projetos são gerenciados e passados para os templates HTML


from flask import Flask, render_template

app = Flask(__name__)

# Lista de projetos
projects = [
    {
        "name": "Projeto 1",
        "description": "Descrição do projeto 1",
        "image": "https://via.placeholder.com/300",
        "link": "#"
    },
    {
        "name": "Projeto 2",
        "description": "Descrição do projeto 2",
        "image": "https://via.placeholder.com/300",
        "link": "#"
    },
    {
        "name": "Projeto 3",
        "description": "Descrição do projeto 3",
        "image": "https://via.placeholder.com/300",
        "link": "#"
    }
]

@app.route('/')
def index():
    return render_template('index.html', projects=projects)

if __name__ == '__main__':
    app.run(debug = True)
