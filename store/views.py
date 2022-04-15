from django.core.paginator import Paginator
from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound
from django.views import View
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


def index(request):
    return HttpResponse("Hello there, globomatics e-commerce store front comming here...")


def detail(request):
    return HttpResponse("Hello there, globomatics e-commerce store front detail pages comming here...")


@csrf_exempt
@cache_page(900)
@require_http_methods(["GET"])
def eletronics(request):
    items = ("Windows PC", "Apple Mac", "Apple IPhone", "Lenovo", "Samsung", "Google")
    if request.method == 'GET':
        paginator = Paginator(items, 2)
        pages = request.GET.get('page', 1)
        try:
            items = paginator.page(pages)
        except:
            items = paginator.page(1)
        return render(request, 'store/list.html', {'items': items})
    elif request.method == "POST":
        return HttpResponseNotFound("Page Not Found")


class EletronicsView(View):
    def get(self, request):
        items = ("Windows PC", "Apple Mac", "Apple IPhone", "Lenovo", "Samsung", "Google")
        if request.method == 'GET':
            paginator = Paginator(items, 2)
            pages = request.GET.get('page', 1)
            try:
                items = paginator.page(pages)
            except:
                items = paginator.page(1)
            return render(request, 'store/list.html', {'items': items})
        elif request.method == "POST":
            return HttpResponseNotFound("Page Not Found")