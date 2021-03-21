from django.urls import path
from badboxd.views import emp, show, edit, update, destroy


urlpatterns = [
    path('emp', emp),
    path('show/', show),
    path('edit/<int:id>', edit,name = "edit"),
    path('update/<int:id>', update,name = "update"),
    path('delete/<int:id>', destroy, name = "delete"),



]