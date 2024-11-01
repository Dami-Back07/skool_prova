from django.urls import path


from . import views

urlpatterns = [
    path("",views.index , name="index"),
    path("view-users" , views.view_user , name="viewusers"),
    path("view-posts" , views.view_post , name="viewposts"),
    path("<int:user_id>" ,views.user_detail , name="user_detail"),
    path("<int:post_id>/posts" , views.post_detail , name="post_detail"),
]