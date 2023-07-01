from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "OFKAHWOKPHO@h1hy41-yh02y0ihfaokahkoshkohKOHOKHFKOSAJHF"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/crudsi"
db = SQLAlchemy(app)

class ProductModel(db.Model):
    __tablename__ = 'product'

    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String())
    product_description = db.Column(db.String())
    product_price = db.Column(db.Integer())
    product_quantity = db.Column(db.Integer())

    def __init__(self, product_name, product_description, product_price, product_quantity):
        self.product_name = product_name
        self.product_description = product_description
        self.product_price = product_price
        self.product_quantity = product_quantity


@app.route('/')
def index():
    #produto_zerado = (ProductModel.product_quantity == 0) não consigo testar
    product = ProductModel.query.order_by(ProductModel.product_name)
    return render_template('index.html', product = product)

@app.route('/cadastrar', methods = ["GET", "POST"],)
def cadastrar():
    if request.method == "POST":
        product_name = request.form["ProductName"]
        product_quantity = request.form["Quantity"]
        product_description = request.form["Description"]
        product_price = request.form["Price"]
        new_product = ProductModel(product_name, product_description, product_price, product_quantity)
        db.session.add(new_product)
        db.session.commit()
        flash("Produto cadastrado com sucesso!")
        return redirect(url_for("cadastrar"))
    else:
        return render_template('cadastro.html')

@app.route('/remover', methods = ["GET", "POST"],)
def remover():
    if request.method == "POST":
        product_name = request.form["ProductName"]
        product_quantity = int(request.form["Quantity"])
        
        product = ProductModel.query.filter_by(product_name=product_name).first()
        
        if product:
            if product_quantity >= product.product_quantity:
               
                db.session.delete(product)
            else:
              
                product.product_quantity -= product_quantity
            
            db.session.commit()
            return render_template('remover.html')
        else:
            flash("Produto não está cadastrado")
            return render_template('remover.html')
    else:
        return render_template('remover.html')
    

@app.route('/editar', methods=["GET", "POST"])
def editar():
    if request.method == "POST":
        product_name = request.form["ProductName"]
        product = ProductModel.query.filter_by(product_name=product_name).first()

        if product:
            product.quantity = request.form["Quantity"]
            product.price = request.form["Price"]
            db.session.add(product)
            db.session.commit()
            flash("Produto editado com sucesso! <3")
        else:
            flash("Produto não está cadastrado!")

    return render_template('editar.html')
        
    

    



if __name__ == "__main__":
    app.run(port=8000, debug=True)
