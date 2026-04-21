from flask import Flask
from routes.employee_routes import employee_bp

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

app.register_blueprint(employee_bp)

if __name__ == "__main__":
    app.run(debug=True)