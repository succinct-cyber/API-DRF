from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Web application endpoint
   

    #API Endpoints
    path('', include ('api.urls'))
]