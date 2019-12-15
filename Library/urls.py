from django.urls import path
from . import views
from . views import GameListView

urlpatterns = [
    path('', GameListView.as_view(), name='Library-home'),

]
