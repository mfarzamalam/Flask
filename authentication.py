import pyrebase

config = {
    "apiKey": "AIzaSyBiM7pShglQoWESauwAhsmnDFYzFrBwj3k",
    "authDomain": "testing-with-fastapi.firebaseapp.com",
    "projectId": "testing-with-fastapi",
    "storageBucket": "testing-with-fastapi.appspot.com",
    "messagingSenderId": "117877501282",
    "appId": "1:117877501282:web:b7916553b4c2d24cf8503b",
    "measurementId": "G-JLPNZ0GLGC",
    "databaseURL": ""
}


firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

email = "farzam-test@gmail.com"
password = "123456789"

# create_new_user = auth.create_user_with_email_and_password(email=email, password=password)
# print("create_new_user:", create_new_user)


sign_in_user = auth.sign_in_with_email_and_password(email=email, password=password)
print("sign_in_user:", sign_in_user)
print()


user_id_token = sign_in_user.get("idToken")
print("user_id_token:", user_id_token)
print()


user_info = auth.get_account_info(user_id_token)
print("user_info:", user_info)