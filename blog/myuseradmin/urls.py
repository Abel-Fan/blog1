from django.urls import path
from . import views

app_name = "myuseradmin"

urlpatterns=[
    path("",views.index,name="index"), #首页
    path("listAddCon/", views.listAddCon, name="listAddCon"), #打开添加内容页面
    path("addCon/", views.addCon, name="addCon"),  #添加内容
    path("listAllCon/", views.listAllCon, name="listAllCon"), #查看全部内容
    path("listOneCon/<int:id>/", views.listOneCon, name="listOneCon"), #查看单个内容
    path("editCon/", views.editCon, name="editCon"), #修改内容
    path("listEditCon/<int:id>",views.listEditCon,name="listEditCon"),
    path("delOneCon",views.delOneCon, name="delOneCon"), #删除内容
    path("editInfo/", views.editInfo, name="listAddCon"),#修改个人资料
    path("search/",views.search,name="search"), #查找
    path("listLogin/",views.listLogin,name="listLogin"), #登录界面
    path("login/",views.login,name="login"), #登录
    path("loginout/", views.loginout, name="loginout"),  # 登录
]
