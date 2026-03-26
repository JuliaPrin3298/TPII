from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


@app.route("/produto")
def produto():

    nome = "Notebook"

    return render_template("produto.html", nome=nome)

