from django.urls import path


from . import views

urlpatterns = [
    path("",views.index , name="index"),
    path("viewusers" , views.view_user , name="viewusers"),
]