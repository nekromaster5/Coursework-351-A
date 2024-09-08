from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
    print("Вызов представления register")
    if request.method == 'POST':
        print("Метод POST в register")
        form = UserRegisterForm(request.POST)
        print("Форма в register (POST):", form)
        if form.is_valid():
            print("Форма валидна")
            form.save()
            username = form.cleaned_data.get('username')
            print(f"Создан пользователь: {username}")
            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
            return redirect('login')
        else:
            print("Форма не валидна")
    else:
        print("Метод GET в register")
        form = UserRegisterForm()
        print("Форма в register (GET):", form)
    return render(request, 'users/register.html', {'form': form})
 