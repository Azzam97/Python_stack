from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['fname']) < 2:
            errors['fname'] = "First name should be at least 2 characters long"
        if len(postData['lname']) < 2:
            errors['lname'] = "Last name should be at least 2 characters long"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address"
        if len(postData['password']) < 8:
            errors['password'] = "Password should be 8 characters long"
        if postData['password'] != postData['pwdconfirm']:
            errors['confirm'] = "Password not the same, try again"
        return errors
    
    def login_validator(self, postData2):
        errors2 = {}
        email2 = postData2['email2']
        password2 = postData2['password2']
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData2['email2']):
            errors2['email2'] = "Invalid email address"
        users = User.objects.filter(email = email2)
        if users:
            logged_user = users[0]
            if not bcrypt.checkpw(password2.encode(), logged_user.password.encode()):
                errors2['password2'] = "Wrong password, try again"
        return errors2


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Message(models.Model):
    user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.message}"


class Comment(models.Model):
    comment_user = models.ForeignKey(User, related_name='commentsAsUsers', on_delete=models.CASCADE)
    comment_message = models.ForeignKey(Message, related_name='commentsAsMessages', on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.comment}"