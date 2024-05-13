from django.shortcuts import render
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.views.generic.base import View
from .models import Menu


class MenuView(View):
    
    def get(self, request):
        menus = Menu.objects.all()
        return render(request, 'menu/index.html', {'menus': menus})


class MenuDetailView(View):
    
    def get(self, request, slug):
        menu_details = Menu.objects.prefetch_related('tags').get(url=slug)
        return render(request, 'menu/main_menu.html', {'menu_details': menu_details})

