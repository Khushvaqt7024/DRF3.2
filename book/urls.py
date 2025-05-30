from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views
from .views import BookViewSet, add_numbers_async, get_task_results

router = SimpleRouter()
router.register(r'books', BookViewSet, basename='books')

urlpatterns = [
    path('', include(router.urls)),
    path('add/', add_numbers_async, name='add_numbers_async'),
    path('result/', get_task_results, name='get_task_results')
]
