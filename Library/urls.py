from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from . views import( 
	GameListView,
	GameDetailView, 
	GameCreateView,
	GameUpdateView,
	GameDeleteView
	)

urlpatterns = [
    path('', GameListView.as_view(), name='Library-home'),
    path('games/<int:pk>/', GameDetailView.as_view(), name='game-detail'),
	path('games/new/', GameCreateView.as_view(), name='game-create'),
	path('games/<int:pk>/update/', GameUpdateView.as_view(), name='game-update'),
	path('games/<int:pk>/delete/', GameDeleteView.as_view(), name='game-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)