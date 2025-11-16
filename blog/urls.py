from django.urls import path
from blog import views

urlpatterns = [
    path("post_list/", views.post_list, name="post_list"),
    path("<int:post_info>/", views.post_infornation, name="post_informations")
]