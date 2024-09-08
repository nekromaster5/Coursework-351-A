from django.contrib import admin
from django.urls import path, include
from users import views as user_views

# Отладочный вывод
print("Загрузка маршрутов в главном urls.py")

urlpatterns = [
    # Отладочный вывод перед каждым маршрутом
    print("Загрузка маршрута: admin/"),
    path('admin/', admin.site.urls),
    
    print("Загрузка маршрута: register/"),
    path('register/', user_views.register, name='register'),
    
    print("Загрузка маршрута: / (blog.urls)"),
    path('', include('blog.urls')),
]

print("Маршруты успешно загружены")
