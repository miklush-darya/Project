from flask import Flask
from flask import redirect, render_template, session, url_for
from config import Config
from user.routers import user_blueprint
from prod_and_cat.routers import products_blueprint


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(user_blueprint)
app.register_blueprint(products_blueprint)


@app.route("/", methods=["GET"])
def start():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()