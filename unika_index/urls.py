from django.urls import path
from unika_index.views import index_view
urlpatterns = [
    path('', index_view)
    
]
