from firebase import firebase
import datetime

a = 5

firebase = firebase.FirebaseApplication(
    "https://venturus-b5e60.firebaseio.com/", None)
data = {
    'Name': 'Victor',
    'Email': datetime.datetime.now()
}

result = firebase.post('/venturus-b5e60/Info', data)
print(result)
