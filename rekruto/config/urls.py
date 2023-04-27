from django.contrib import admin
from django.urls import path
from displaymessage.views import get_message

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_message)
]
