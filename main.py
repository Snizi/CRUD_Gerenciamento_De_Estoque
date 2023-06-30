from flask import Flask, render_template, request, redirect, session, flash, url_for


app = Flask(__name__)
app.secret_key = "OFKAHWOKPHO@h1hy41-yh02y0ihfaokahkoshkohKOHOKHFKOSAJHF"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods = ["GET", "POST"],)
def cadastrar():
    if request.method == "POST":
        product_name = request.form["ProductName"]
        product_quantity = request.form["Quantity"]
        product_description = request.form["Description"]
        flash("Produto cadastrado com sucesso!")
        return redirect(url_for("cadastrar"))
    else:
        return render_template('cadastro.html')

    

if __name__ == "__main__":
    app.run(port=8000, debug=True)
