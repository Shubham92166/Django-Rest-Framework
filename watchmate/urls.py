from django.contrib import admin
from django.urls import path, include
import watchlist 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include('watchlist.api.urls')),
]
