from django.conf.urls import url
from . import views
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    # url(r'^$', views.post_model_list_view, name='list'),
    url(r'^$', views.get_image , name='get_image'),
]