from django.urls import path
from site_app.views import MainPage

urlpatterns = [
    path('', MainPage.as_view())
]