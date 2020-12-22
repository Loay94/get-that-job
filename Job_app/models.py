from django.db import models
import re
import bcrypt

# def user_login(login_info):
#     user_exist = User.objects.filter(email=login_info['email'])
#     if len(user_exist):
#         password= login_info['password']
#         if bcrypt.checkpw(password.encode(), user_exist[0].password.encode()):
#             return user_exist[0]
#     return False
