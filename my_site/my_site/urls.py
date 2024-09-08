from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

# Отладочный вывод
print("Загрузка маршрутов в my_site/urls.py")

urlpatterns = [
    # Отладочный вывод перед каждым маршрутом
    print("Загрузка маршрута: admin/"),
    path('admin/', admin.site.urls),
 
    
    print("Загрузка маршрута: / (blog.urls)"),
    path('', include('blog.urls')),
]

print("Проверка режима DEBUG")
if settings.DEBUG:
    print("DEBUG режим включен, добавление статических маршрутов")
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

print("Маршруты успешно загружены")
