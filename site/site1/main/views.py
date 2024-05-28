from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string

menu = ["О сайте", "Добавить статью", "Войти"]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]


def index(request):
    data = {
        'title': 'главная страница',
        'menu': menu,
        'posts': data_db,
        }
    return render(request, 'main/index.html', context=data)

def sozvesdie(request):
    return render(request, 'main/sozvezdie.html')

def faq(request):
    return render(request, 'main/faq.html', {'title': 'О сайте'})

def categories(request, cat_id):
    return HttpResponse(f"<h1>Стати по категории</h1><p>id: {cat_id}</p>")

def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


# def categories(request, cat_id):
#     return render(request, 'main/index.html')