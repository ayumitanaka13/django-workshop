from django.urls import path
from .views import apiOverviews, getAllProducts
# from .views import Http, Test, Top

# http://localhost:8000/
urlpatterns = [
    # path('', Top), # http://localhost:8000/
    path('api/', apiOverviews), # http://localhost:8000/api
    path('api/products', getAllProducts), # http://localhost:8000/api/products
    # path('api/test', Test), # http://localhost:8000/api/test
]
