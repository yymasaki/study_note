from django.contrib import admin
from django.urls import path, include
from .views import hello_world
from .views import ListEntryView, DetailEntryView, CreateEntryView, UserView, UpdateEntryView, DeleteEntryView

urlpatterns = [
    path('hello/', hello_world, name='hello_2'),
    path('entries/', ListEntryView.as_view(), name='list_entry'),
    path('entry/<int:pk>/detail/', DetailEntryView.as_view(), name='detail_entry'),
    path('entry/create/', CreateEntryView.as_view(), name='create_entry'),
    path('user/<int:user>/entries/', UserView.as_view(), name='user_list'),
    path('entry/<int:pk>/update/', UpdateEntryView.as_view(), name='update_view'),
    path('entry/<int:pk>/delete/', DeleteEntryView.as_view(), name='delete_view'),
]