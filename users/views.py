from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.models import User  # Или ваша модель пользователя

class UserListView(ListView):
    model = User
    template_name = "users/user_list.html"  # Создайте шаблон

class UserDetailView(DetailView):
    model = User
    template_name = "users/user_detail.html"  # Создайте шаблон

class UserCreateView(CreateView):
    model = User
    fields = ['username', 'email', 'password']
    template_name = "users/user_form.html"  # Создайте шаблон
