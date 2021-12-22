from flask import Flask

from database import setup
from resources.tasks import task_bp

app = Flask(__name__)

setup.create_tables()

app.register_blueprint(task_bp)

if __name__ == '__main__':
    app.run(debug=True)