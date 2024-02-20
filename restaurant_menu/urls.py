from django.urls import path
from . import views

# pk --> Primary key

urlpatterns = [
    path('', views.MenuList.as_view(), name='home'),
    path('item/<int:pk>/', views.MenuItemDetail.as_view(), name='menu_item')
]