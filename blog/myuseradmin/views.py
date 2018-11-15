from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Content,Users

# 导入 Paginator EmptyPage PageNotAnInteger
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from functools import wraps
def check_login(f):
    @wraps(f)
    def inner(request,*arg,**kwargs):
        print(request.session.get('username'))
        if request.session.get('username'):

            return f(request,*arg,**kwargs)
        else:
            return redirect('/myuseradmin/listLogin')
    return inner


# Create your views here.
@check_login
def index(request):
    content = 12
    return render(request,"myuseradmin/index.html")

@check_login
def listAddCon(request):
    return render(request, "myuseradmin/add.html")
@check_login
def addCon(request):
    title = request.POST['title']
    content = request.POST['content']
    authour = request.POST['authour']
    Content.objects.create(con=content,author=authour,title=title)
    return HttpResponse("添加内容")

@check_login
def listAllCon(request):
    # 获取所有数据
    all = Content.objects.all().filter(id_delete=0)
    # 生成paginator对象，定义每页显示3条
    paginator = Paginator(all,3)
    # 从当前页获取页码数,默认为1
    page = request.GET.get('page',1)
    # 把当前页面转化为整数类型
    currentPage = int(page)

    print("page",page)
    try:
        book_list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        book_list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        book_list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容

    return render(request,"myuseradmin/list.html",locals())

@check_login
def listOneCon(request,id):
    con = Content.objects.get(id=id)
    return render(request,"myuseradmin/listone.html",{'con':con})
@check_login
def editCon(request):
    title = request.POST['title']
    con = request.POST['con']
    author = request.POST['author']
    Content.objects.update(title=title,con=con,author=author)
    return HttpResponse("修改内容")

@check_login
def listEditCon(request,id):
    con = Content.objects.get(id=id)
    return render(request,"myuseradmin/edit.html",{'con':con})

@check_login
def delOneCon(request):
    id = request.POST['id']
    Content.objects.get(id=id).update(id_delete=1)
    return HttpResponse("删除内容")

@check_login
def editInfo(request):

    return render(request,"myuseradmin/pass.html")

@check_login
def search(request):
    keyword = request.GET['keyword']
    all = Content.objects.all().filter(title__contains=keyword)
    return render(request,"myuseradmin/server.html",locals())




def listLogin(request):

    return render(request,"myuseradmin/login.html",{'username':"username"})


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        u = Users.objects.get(username=username)
        if u.password==password:
            res = redirect("../")
            request.session['username']=username
            # res.set_cookie('username',password,1000)
            return res
    except:
        return redirect("../listLogin",username="admin")


@check_login
def loginout(request):

    del request.session["username"]

    return redirect("../listLogin")
