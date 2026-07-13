import requests
user={
    "email":"swamy@gmail.com",
    "password":"Swamy@06"
   
}

response=requests.post("http://127.0.0.1:5000/users/login",json=user)
token=response.json()["user_token"]

header={
    "Authorization":f"Bearer {token}"
}
response=requests.get("http://127.0.0.1:5000/profile",headers=header)
print(response.json())