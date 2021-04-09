
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from tdapp import views

urlpatterns = [
    path('', views.index.as_view(),name='index'),
    path('admin/', admin.site.urls),
    path('special/', views.special,name='special'),
    path('tdapp/', include('tdapp.urls')),
    path('logout/', views.user_logout, name='logout'),
]



urlpatternsformedia = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = urlpatterns + urlpatternsformedia