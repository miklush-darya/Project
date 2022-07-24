from flask import Flask, Blueprint
from flask import redirect, render_template, url_for, request
from config import Config

from .forms import ProductrForm, CategoryForm, ShopProductForm


app = Flask(__name__)
app.config.from_object(Config)


order_blueprint = Blueprint(
        "product", __name__,
        template_folder="templates",
        url_prefix="/product",
    )

# API = "http://127.0.0.1:8000"

@order_blueprint.route("/add", methods=["GET", "POST"])
def add_product():
    form = ProductrForm()
    if form.validate_on_submit():
        form_data = dict(form.data)
        print(form_data)
        return redirect(url_for("product"))########### на список продуктов
    return render_template("product.html", form=form)