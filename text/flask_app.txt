
from application import create_app
from application.models import db

app = create_app('ProductionConfig')

# Only run create_all locally
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
