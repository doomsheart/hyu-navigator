from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'input_data', views.inputData, name='input_data'),
]
