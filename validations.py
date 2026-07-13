import re
email_pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$"
symbols="!@#$%^&*"
def validation_password(password):
    if len(password)<8:
        return {
                "Message":"Password must contain at least 8 Characters"
            },400
    if not any(ch.isupper() for ch in password):
        return {
                "Message":"password must contain at least  one  Uppercase letter"
         },400
    if not any(ch.islower() for ch in password):
        return {
                "Message":"password must contain at least  one  lowercase letter"
        },400
    if not any(ch.isdigit() for ch in password):
            return{
                "Message":"password must contain at least  one digit"
            },400
    if not any( ch in symbols for ch in password):
            return {
                "Message":"password must contain at least  one  Symbol"
            },400
    return None
def required_fields(required_field,data):
    for field in required_field:
        if field not in data:
            return{
                    "Message":f"{field} is required "
                },400
        if not isinstance(data[field],str):
            return{
                    "Message":f"{field} must be string"
                },400
        if not data[field].strip():
            return{
                    "Message":f"{field} is missing"
                },400
    return None
def email_validation(email):
    if not re.match(email_pattern,email):
            return {
                "Message":"Invalid Email pattern"
             },400
    return None