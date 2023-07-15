import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : "https://faceattendancerealtime-3056d-default-rtdb.firebaseio.com/"

})

ref=db.reference('Students')

data = {
    "321654":
        {
            "name":"MH",
            "major": "EXTC",
            "starting_year":2020,
            "total_attendance":6,
            "standing": "G",
            "year":4,
            "last_attendance_time": "2022-08-13 00:54:34"
        },
"852741":
        {
            "name":"Emi",
            "major": "EXTC",
            "starting_year":2021,
            "total_attendance":5,
            "standing": "A",
            "year":4,
            "last_attendance_time": "2022-08-13 00:54:34"
        },
"963852":
        {
            "name":"Elon",
            "major": "ENTC",
            "starting_year":2014,
            "total_attendance":9,
            "standing": "C",
            "year":2,
            "last_attendance_time": "2022-08-13 00:54:34"
        }
}

for key , value in data.items():
    ref.child(key).set(value)
