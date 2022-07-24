from flask import Flask
from flask import redirect, render_template, session, url_for
# from prod_and_cat.forms import ProductrForm, CategoryForm, ShopProductForm
# from prod_and_cat.api import access, create_user, get_current_user
from config import Config


app = Flask(__name__)
app.config.from_object(Config)






if __name__ == "__main__":
    app.run()