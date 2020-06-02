import os
import sys
import time
import firebase_admin
from datetime import datetime
from firebase_admin import credentials
from database.firebase_interface import FirebaseInterface

cred = credentials.Certificate("database/credentials.json")
firebase_admin.initialize_app(cred)
interface = FirebaseInterface()

def sendDataToFirebase(num_people):
    docTitle = datetime.today().strftime('%Y-%m-%d')
    currentHour = datetime.today().strftime('%H:%M')
    docData = {currentHour: {"num_people": num_people}}
    interface.addOrUpdateData("kitchen_data", docTitle, docData)

def main():
    
    sendDataToFirebase(3)

if __name__ == '__main__':
    main()
