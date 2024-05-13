from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import MenuView, MenuDetailView

urlpatterns = [
    path('', MenuView.as_view(), name='menu'),
    path('<slug:slug>/', MenuDetailView.as_view(), name='main_menu_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)