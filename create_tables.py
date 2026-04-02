from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')

from application import create_app
from application.models import db
from application.models import Customers, Mechanics, Service_tickets, Inventory

app = create_app('ProductionConfig')

with app.app_context():
    db.create_all()
    
    print("Tables created successfully!")