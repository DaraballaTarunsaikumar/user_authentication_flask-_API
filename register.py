import  requests
user={
    "username":"Swamy",
    "email":"swamy@gmail.com",
    "password":"Swamy@06"
}
response=requests.post("http://127.0.0.1:5000/users",json=user)
print(response.status_code)
print(response.json())

