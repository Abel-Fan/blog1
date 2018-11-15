from django.db import models
from db.base_model import BaseModel
# Create your models here.

class Users(BaseModel):
    username = models.CharField("用户名",max_length=24)
    password = models.CharField("密码",max_length=40)
    email = models.EmailField("邮箱")

class Content(BaseModel):
    # author
    title = models.CharField("标题",max_length=50)
    author = models.CharField("作者",max_length=24)
    con = models.CharField("内容",max_length=1000)
