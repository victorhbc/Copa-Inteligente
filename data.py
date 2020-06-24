import firebase_admin
from datetime import datetime
from firebase_admin import credentials
from database.firebase_interface import FirebaseInterface
import time

cred = credentials.Certificate('database/credentials.json')
firebase_admin.initialize_app(cred)
interface = FirebaseInterface()

docTitle = datetime.today().strftime('%Y-%m-%d')
docData = {'10:30': {"num_people": 7}}
interface.addOrUpdateData("kitchen_data", docTitle, docData)

docData = {'10:45': {"num_people": 8}}
interface.addOrUpdateData("kitchen_data", docTitle, docData)

docData = {'11:45': {"num_people": 9}}
interface.addOrUpdateData("kitchen_data", docTitle, docData)