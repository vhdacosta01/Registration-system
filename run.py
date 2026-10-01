from flask import Flask
from app.routes.router import router
from app.config.database import init_database

app = Flask(
    __name__,
    template_folder="app/templates",
    static_folder="app/static"
)

app.secret_key = "sua_chave_secreta"

app.register_blueprint(router)

init_database()


if __name__ == "__main__":
    app.run(debug=True)