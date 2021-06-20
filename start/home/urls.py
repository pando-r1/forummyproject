from django.urls import path
from home import views as home
from django.shortcuts import redirect
from django.urls import reverse


urlpatterns = [
    path("home/", home.home, name="home"),
    path("", lambda request: redirect(reverse("home"))),
    path("post/<int:post_id>/", home.show_post,  name="post"),
    path("page/<int:page>/", home.home,  name="page"),
    path("category/<int:category_id>/", home.home,  name="category"),
]