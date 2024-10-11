from django.urls import path
from . import views


urlpatterns = [
    path("api/", views.BulkCreateApiView.as_view(), name="product_api"),
]
