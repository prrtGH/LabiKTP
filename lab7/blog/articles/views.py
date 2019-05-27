# -*- coding: cp1251 -*- 
from models import Article
from django.shortcuts import render
from django.shortcuts import redirect 
from django.http import Http404

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
        # ���������� ������ �����, ���� ����� POST 
            form = { 
            'text': request.POST["text"], 
            'title': request.POST["title"] 
            } 
# � ������� form ����� ��������� ����������, ��������� ������������� 
            if form["text"] and form["title"]: 
# ���� ���� ��������� ��� ������ 
                try: 
                    article=Article.objects.get(title=form["title"]) 
                    form['errors']= u"����� �������� ������ ��� ����������" 
                    return render(request, 'create_post.html', {'form': form}) 
                except Article.DoesNotExist: 
                    article = Article.objects.create(text=form["text"],
                    title=form["title"],
                    author=request.user,) 
                    return redirect('get_article', article_id=article.id) 
# ������� �� �������� ����� 
            else: 
# ���� ��������� ������ ����������� 
                form['errors'] = u"�� ��� ���� ���������" 
                return render(request, 'create_post.html', {'form': form}) 
        else: 
# ������ ������� �������� � ������, ���� ����� GET 
            return render(request, 'create_post.html', {}) 
    else: 
        raise Http404
