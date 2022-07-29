from flask import Flask, Blueprint
from flask import redirect, render_template, session, url_for, request
from .front.shop.forms import RegisterShopForm
from front.shop.api import create_shop, get_current_shop
from config import Config


app = Flask(__name__)
app.config.from_object(Config)


shop_blueprint = Blueprint("shop",
                            __name__,
                            template_folder="templates",
                            static_folder="static",
                            url_prefix="/shop",
                        )


@shop_blueprint.route("/register_shop", methods=["GET", "POST"])
# @app.route("/register", methods=["GET", "POST"])
def register_shop():
    form = RegisterShopForm()
    if form.validate_on_submit():
        shop = create_shop(**form.data)
        shop.store_in_session()
        return redirect(url_for("shop.home"))
    return render_template("register_shop.html", form=form)
