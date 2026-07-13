from flask import request
from db import conn,cursor
from flask_jwt_extended import create_access_token,jwt_required,get_jwt_identity
from werkzeug.security import generate_password_hash ,check_password_hash

from validations import validation_password,email_validation,required_fields
    

def user_roots(app):
    @app.route("/users",methods=["GET"])
    def get_user():
        try:
            cursor.execute('''SELECT * from users ''')
            users=cursor.fetchall()
            result=[]
            for user in users:
             result.append({
                    "id":user[0],
                    "name":user[1],
                    "email":user[2],
                    
                })
            return result,200
        
        except  Exception as e :
            print(e)
            return {
                "Message":"Database Error"
            },500
            
    @app.route("/users",methods=["POST"])
    def post_user():
        data=request.get_json(silent=True)
        if not data:
            return {
                "Message":"json data is required"
            },400
        required_field=["username","email","password"]
        field_error=required_fields(required_field,data)
        if field_error :
            return field_error
        
        data["username"]=data["username"].strip()
        data["email"]=data["email"].strip().lower()
        email_error=email_validation(data["email"])
        if email_error:
            return email_error
        password=data['password']
        password_error=validation_password(password)
        if password_error:
           return password_error
       
        try:
       
         cursor.execute(''' SELECT email FROM users  WHERE email=%s''',(data["email"],))
         existing_user =cursor.fetchone()
         if existing_user is not None:
             return {
                 "Message":"Email already registered"
             },409
         
         data["password"]=generate_password_hash(data["password"])
         query=''' INSERT INTO users(username,email,password)
         VALUES(%s,%s,%s) '''
         values=(data["username"],data["email"],data["password"])
         cursor.execute(query,values)
         conn.commit()
         return {
             "Message":"Successfully"
          },201
        except Exception as e:
            conn.rollback()
            print(e)
            return {
                "Message":"Database error"
            },500
            
    @app.route("/users/login",methods=["POST"])
    def login_user():
        data=request.get_json(silent=True)
        if not data:
            return {
                "Message":"json data is required"
            },400
        required_field=["email","password"]
        field_error=required_fields(required_field,data)
        if field_error:
            return field_error
            
        
        data["email"]=data["email"].strip().lower()
        
        try:
            
            cursor.execute(''' SELECT * FROM users WHERE  email=%s''',(data["email"],))
            user=cursor.fetchone()
            if user is None:
                  return {
                      "Message":"Invalid email or password"
                        
                    },401
            if check_password_hash(user[3],data["password"]):
                access_token=create_access_token(identity=str(user[0]))
                return {
                        "Message":"Login Successfully",
                        "user_token":access_token
                    },200
            
            return {
                    "Message":"Invalid email or password"
                },401
                
        except Exception as e:
            return {
                "Message":"Database error"
            },500
                
    @app.route("/profile",methods=["GET"])
    @jwt_required()
    def profile():
        user_id=get_jwt_identity()
        try:
         cursor.execute('''SELECT * FROM users WHERE id=%s''',(user_id,))
         user=cursor.fetchone()
         if user is None:
               return {
              "Message":"User not found"
            
          },404
        
         
         return {
            "userid":user[0],
            "username":user[1],
            "email":user[2],   
            
          },200
        except Exception as e:
            print(e)
            return {
                "Message":"Database error"
            },500
       
            
        
    