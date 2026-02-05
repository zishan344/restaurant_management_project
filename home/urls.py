from django.urls import path
from .views import *

urlpatterns = [
    path("menu_category/", MenuCategroyView.as_view(), name="menu-category")
]