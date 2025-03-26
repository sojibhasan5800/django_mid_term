from django.contrib import admin
from django.urls import path, include
from .views import homepage
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home_page'),
    path('author_page/', include('authors.urls')),
   
    
   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
