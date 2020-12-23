from django.db import models
from datetime import date, datetime
from django.utils import timezone
import re
import bcrypt

class UserManager(models.Manager):
    def register_validator(self, user_info):
        errors = {}
#names
        if (str.isalpha(user_info['first_name'])) == False: #user_info['first_name'] is from the form of registration
            if len(user_info['first_name']) <4 :
                errors["firstname"] = "First Name should be more than 2 characters." #["first_name"] is a key for errors dictionary can be any word
        if (str.isalpha(user_info['last_name'])) == False:
            if len(user_info['last_name']) <4 :
                errors["lastname"] = "Last Name should be more than 2 characters."
#email  
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        new_user = User.objects.filter(email = user_info['email'])
        if not EMAIL_REGEX.match(user_info['email']): #checking if email matches the regex           
            errors['email'] = "Invalid email address!"
        if len(new_user):
            errors['email'] = "Email already exists.. Try another!"
#password
        if len(user_info['password']) < 8:
            errors["password"] = "Password should be at least 8 characters."
        if user_info['password'] != user_info['password_confirm']:
            errors['password_confirm']= "Password Dosent Match!"
#birthday
            now = timezone.now()
            if (user_info['birthday'] > str(now)):
                errors['birthday'] = "Invalid Birth date. Birthday should be in the past"
            today = datetime.now().strftime("%Y%m%d")
            user_birthday = user_info['birthday'].replace("-", "")
            # if len(user_info["birthday"]) > 0 and datetime.strptime(user_info["birthday"], '%Y-%m-%d') >= datetime.today() :
            #     errors["birthday"] = "Invalid Birth date"
            if (int(today[0:4]) - int(user_birthday[0:4])) <= 18:
                errors["birthday"] = "You should be at least 18 years old to register"
        return errors

#Login Validator
    def login_validator(self, user_info):
            errors = {}
            all_user = User.objects.filter(email = user_info['email'])
            EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            if not EMAIL_REGEX.match(user_info['email']):
                errors['email'] = "Wrong email address!"
            if not len(all_user):
                errors['email'] = "Email not registered! /Wrong Email"
            if len(user_info['password']) < 8:
                errors["password"] = "Password should be 8 characters minimum"
            if len(all_user) and not bcrypt.checkpw(user_info['password'].encode(), all_user[0].password.encode()):
                errors["password"] = "Wrong Password!"
            return errors

#Data_Base Tables
class Role(models.Model):
    name = models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    birthday=models.DateField(null = True)
    education=models.TextField(null=True)
    field_of_experience=models.TextField(null=True)
    birthday=models.DateField()
    education=models.TextField()
    field_of_experience=models.TextField()
    image = models.ImageField(upload_to="images/",blank=True)
    password=models.CharField(max_length=255)
    interests=models.TextField(null=True)
    about=models.TextField(null=True)
    role=models.ForeignKey(Role,related_name='user', on_delete=models.CASCADE,default=0) # foreignkey one to many  user with role
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = UserManager()

class Session (models.Model):
    date=models.DateField()
    period=models.TimeField()
    description=models.TextField()
    user=models.ForeignKey(User,related_name='user_session', on_delete=models.CASCADE) # foreignkey one to many  user with session 
    consultant=models.ForeignKey(User,related_name='consultant_session', on_delete=models.CASCADE)# foreignkey one to many  user with session 
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Partner(models.Model):
    name=models.CharField(max_length=255)
    field_of_company=models.TextField()
    about=models.TextField()
    image = models.ImageField(upload_to="images/",blank=True)
    admin=models.ForeignKey(User,related_name='partner', on_delete=models.CASCADE)# foreignkey one to many user with partner
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Story(models.Model):
    description=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)# foreignkey one to one user with story
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

#Data Base Funtions

def add_new_user(new_user):
    user = User.objects.filter(email = new_user['email'])
    if len(user) == 0:
        if new_user['password_confirm'] == new_user['password']:
            password = new_user['password']  #hashing user password
            hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            User.objects.create(first_name=new_user['first_name'],last_name=new_user['last_name'],email=new_user['email'],password=hashed)  #newUser['key name from form']
            new_user_info = User.objects.last() 
        return new_user_info
    return False


# def user_login(login_info):
#     user_exist = User.objects.filter(email=login_info['email'])
#     if len(user_exist):
#         password= login_info['password']
#         if bcrypt.checkpw(password.encode(), user_exist[0].password.encode()):
#             return user_exist[0]
#     return False



# def log_in(log_info):
#     user_in_data = User.objects.filter(email=log_info['email'])
#     if len(user_in_data):
#         # if bcrypt.checkpw(log_info['password'].encode(), user_in_data[0].password.encode()):
#         return user_in_data[0]

def user_login(login_info):
    user_exist = User.objects.filter(email=login_info['email'])
    if len(user_exist):
        password= login_info['password']
        if bcrypt.checkpw(password.encode(), user_exist[0].password.encode()):
            return user_exist[0]
    return False