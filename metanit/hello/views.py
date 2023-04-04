from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm
  
def index(request):
    return render(request, "index.html")
 
def about(request):
    return HttpResponse("<h2>О сайте</h2>")
 
def contact(request):
    return HttpResponse("<h2>Контакты</h2>")

def user(request):
    if request.method == 'POST':
        name = request.POST.get("name", "Undefined")
        age = request.POST.get("age", 1)
        user = {"name": name, "age": age}
        data = {"user":user}
        return render(request, "user.html", context=data)
    else:
        return render(request, "getter.html")

def userform(request):
    userform = UserForm()
    if request.method == 'POST':
        name = request.POST.get("name", "Undefined")
        age = request.POST.get("age", 1)
        user = {"name": name, "age": age}
        data = {"user":user}
        return render(request, "user.html", context=data)
    else:
        return render(request, "userform.html", {"form": userform})
    
    

# установка куки
def set(request):
    # получаем из строки запроса имя пользователя
    username = request.GET.get("username", "Undefined")
    # создаем объект ответа
    response = HttpResponse(f"Hello {username}")
    # передаем его в куки
    response.set_cookie("username", username)
    return response
