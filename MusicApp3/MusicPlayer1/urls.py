from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name="index" ),
    path('Govinda',views.Govinda, name="govinda"),
    path('<str:name>',views.greet, name="greet")
]
