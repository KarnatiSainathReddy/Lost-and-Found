from django.urls import path
from . import views

urlpatterns = [
    path('report/', views.report_item, name='report_item'),
    path('', views.view_items, name='view_items'),
    path('<int:item_id>/', views.item_detail, name='item_detail'),
    path('edit/<int:item_id>/', views.edit_item, name='edit_item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
]