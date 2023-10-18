
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.hello.as_view(),name='home'),
    path('<int:pk>',views.candidateview,name='candidate')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
