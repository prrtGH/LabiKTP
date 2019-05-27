# -*- coding: cp1251 -*- 
from models import Article
from django.shortcuts import render
from django.shortcuts import redirect 
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login

def archive(request):
    return render(request, 'archive.html', {"posts":
Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404


def create_post(request): 
    if not request.user.is_anonymous(): 
        if request.method == "POST": 
        # обработать данные формы, если метод POST 
            form = { 
            'text': request.POST["text"], 
            'title': request.POST["title"] 
            } 
# в словаре form будет храниться информация, введенная пользователем 
            if form["text"] and form["title"]: 
# если поля заполнены без ошибок 
                try: 
                    article=Article.objects.get(title=form["title"]) 
                    form['errors']= u"Такое название статьи уже существует" 
                    return render(request, 'create_post.html', {'form': form}) 
                except Article.DoesNotExist: 
                    article = Article.objects.create(text=form["text"],
                    title=form["title"],
                    author=request.user,) 
                    return redirect('get_article', article_id=article.id) 
# перейти на страницу поста 
            else: 
# если введенные данные некорректны 
                form['errors'] = u"Не все поля заполнены" 
                return render(request, 'create_post.html', {'form': form}) 
        else: 
# просто вернуть страницу с формой, если метод GET 
            return render(request, 'create_post.html', {}) 
    else: 
        raise Http404

def reg(request):
        if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {
            'username': request.POST["username"],
            'password': request.POST["password"]
            }
            # в словаре form будет храниться информация, введенная пользователем
            if form["username"] and form["password"]:
                # если поля заполнены без ошибок
                try:
                    user=User.objects.get(username=form["username"])
                    form['errors']= u"Такой логин уже существует"
                    return render(request, 'reg.html', {'form': form})
                except User.DoesNotExist:
                    user = User.objects.create_user(username=form["username"],password=form["password"])
                    user=authenticate(username=form["username"],password=form["password"])
                    if user:
                        login(request,user)
                        return redirect('create_post')
                # перейти на страницу поста
            else:
                # если введенные данные некорректны
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'reg.html', {'form': form})
        else:
            # просто вернуть страницу с формой, если метод GET
            return render(request, 'reg.html', {})

def aut(request):
        if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {
            'username': request.POST["username"],
            'password': request.POST["password"]
            }
            # в словаре form будет храниться информация, введенная пользователем
            if form["username"] and form["password"]:
                # если поля заполнены без ошибок
                try:
                    user=authenticate(username=form["username"],password=form["password"])
                    if user:
                        login(request,user)
                        return redirect('create_post')
                    else:
                        form['errors']= u"Нет аккаунта с таким сочетанием никнейма и пароля"
                        return render(request,'autoriz.html',{'form':form})
                except User.DoesNotExist:
                    form['errors']= u"Нет аккаунта с таким сочетанием никнейма и пароля"
                    return redirect('autoriz')
                # перейти на страницу поста
            else:
                # если введенные данные некорректны
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'autoriz.html', {'form': form})
        else:
            # просто вернуть страницу с формой, если метод GET
            return render(request, 'autoriz.html', {})
