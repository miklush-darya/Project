from itertools import product
from flask import Flask, Blueprint
from flask import redirect, render_template, url_for, request
from config import Config
import requests

from prod_and_cat.forms import ProductrForm, CategoryForm, ShopProductForm
from user.api import get_current_user

from prod_and_cat.api import add_product, add_category
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


products_blueprint = Blueprint(
        "products", __name__,
        template_folder="templates",
        url_prefix="/products",
    )

API = "http://127.0.0.1:8000"

#http://127.0.0.1:8000/api/products/

@products_blueprint.route("/", methods=["GET"])
def list_product():
    prod = requests.get(f"{API}/api/products/").json()
    categ = requests.get(f"{API}/api/category/").json()
    return render_template("prodlist.html", product=prod, category=categ)


@products_blueprint.route("/addproduct", methods=["GET", "POST"])
def add_prod():
    form = ProductrForm()
    if form.validate_on_submit():
        user = get_current_user()
        user.store_in_session()
        form_data = dict(form.data)
        # form_data['category'] = list(form_data['category'])
        add_product(**form_data)
        # categ = add_category(**form.data)
        return redirect(url_for("products.list_product"))
    return render_template("addprod.html", form=form)


# @products_blueprint.route("/category", methods=["GET"])
# def list_category():
#     categ = requests.get(f"{API}/api/category/").json()
#     return render_template("categorylist.html", category=categ)


# @order_blueprint.route("/<int:id>", methods=["GET", "POST"])
# def one_order(id):
#     var = requests.get(f"{API}/order/api/order/").json()
#     order = var[id - 1]
#     form = CommentForm()
#     if form.validate_on_submit():
#         user = get_current_user()
#         user.store_in_session()
#         form_data = dict(form.data)
#         form_data['user'] = int(user.id)
#         form_data['order'] = order['id']
#         form_data['is_active'] = True
#         comment_add(**form_data)

#     com = requests.get(f'{API}/order/api/order_comments/').json()
#     comments = []
#     for i in range(len(com)):
#         if com[i]['order'] == order['id']:
#             comments.append(com[i])

#     return render_template("one_order.html", order=order, comments=comments, form=form)



@products_blueprint.route("/", methods=["GET"])
def add_product():
    # form = ProductrForm()

    return render_template("base.html")

# @products_blueprint.route("/list", methods=["GET", "POST"])
# def add_product():
#     form = ProductrForm()
#     if form.validate_on_submit():
#         # user = get_current_user() ###
#         # user.store_in_session() ###
#         form_data = dict(form.data)
#         add_product(**form_data) ###
#         print(form_data)
#         return redirect(url_for("products.base"))########### на список продуктов
#     return render_template("product.html", form=form)


# @order_blueprint.route("/add", methods=["GET", "POST"])
# def add():
#     form = OrderForm()
#     if form.validate_on_submit():
#         user = get_current_user()
#         user.store_in_session()
#         form_data = dict(form.data)
#         form_data['date_finish'] = str(form_data["date_finish"])
#         form_data['speciality'] = list(form_data['speciality'])
#         form_data['user'] = int(user.id)
#         order_add(**form_data)
#         if form_data['photo']:
#             form_data.pop("photo")
#             photo = form.photo.data
#             link = upload_file_to_s3(photo)
#             form_data["photo"] = link
#             form_data['order'] = order_id()
#             print(form_data)
#             photo_add(**form_data)
#         return redirect(url_for("index"))
#     return render_template("add.html", form=form)

# @products_blueprint.route("/list", methods=["GET", "POST"])
# def list_product():
#     a = request.get(f"{API}/api/products/").json()
#     return render_template("product.html", a=a)

# @products_blueprint.route("/add", methods=["GET", "POST"])
# def add():
#     form = ProductrForm()
#     if form.validate_on_submit():
#         form = dict(form.data)
#         print(form)
#         return redirect(url_for("prod_and_cat.product"))
#     return render_template("prod_and_cat.product.html", form=form)