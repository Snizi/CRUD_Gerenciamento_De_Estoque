from flask import Flask, render_template, request, redirect, session, flash, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastro.html')


if __name__ == "__main__":
    app.run(port=8000, debug=True)
