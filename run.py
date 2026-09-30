from flask import Flask
from app.routes.router import router

app = Flask(
    __name__,
    template_folder="app/templates",
    static_folder="app/static"
)


app.secret_key = "your_secret_key"

app.register_blueprint(router)

if __name__ == "__main__":
    app.run(debug=True)