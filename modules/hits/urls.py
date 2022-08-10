from django.urls import path
from .views import register_hit, get_list_hits, get_hit_details


urlpatterns = [
    path('create/', register_hit, name="register_hit"),
    path('', get_list_hits, name="list_hits"),
    path('<int:hit_id>/', get_hit_details, name="hit_detail"),
]
