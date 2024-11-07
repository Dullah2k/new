from django.contrib import admin
from django.urls import path, include
from account import views

urlpatterns = [
	path('admin/', admin.site.urls),
  path('account/', include('account.urls')),
]
