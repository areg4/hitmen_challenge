from django.urls import path
from .views import register_hitman, list_hitmen, hitman_detail


urlpatterns = [
    path('register/', register_hitman, name="register_hitman"),
    path('', list_hitmen, name="list_hitmen"),
    path('<int:hitman_id>/', hitman_detail, name="detail_hitman"),
]
