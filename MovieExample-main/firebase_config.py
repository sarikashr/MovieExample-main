import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyAnfsW099WJnKMmuqG3mvqB4ldOvGUyFHY",
    "authDomain": "interlink-4bd6d.firebaseapp.com",
    "databaseURL": "https://interlink-4bd6d-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "interlink-4bd6d",
    "storageBucket": "interlink-4bd6d.firebasestorage.app",
    "messagingSenderId": "562836549822",
    "appId": "1:562836549822:web:5c79c9dfa9afe137606eef",
    "measurementId": "G-HRR23YE6HQ"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

