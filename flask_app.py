print(">>> Importing flask_app.py")

from project.application import create_app
print(">>> Imported create_app")

from project.application.models import db
print(">>> Imported db")

app = create_app('ProductionConfig')
print(">>> App created")

# Only run create_all locally
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
