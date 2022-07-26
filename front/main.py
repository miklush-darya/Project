from flask import Flask
from flask import redirect, render_template, session, url_for
from config import Config
from user.routers import user_blueprint


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(user_blueprint)





if __name__ == "__main__":
    app.run()