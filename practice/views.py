from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User as User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserRegistrationForm, LoginForm, PasswordForm
from .models import Posts, Comments


def startpage(request):
    return render(request, 'practice/startpage.html')


"""
Posts
"""


# добавть авторизацию через миксин, автозапись пользователя
class PostsCreateView(CreateView):
    model = Posts
    template_name = 'practice/posts_create.html'
    success_url = reverse_lazy('posts_list')
    fields = ['post_text', 'short_description', 'full_description', 'picture', 'is_draft', 'user']


class PostsUpdateView(UpdateView):
    model = Posts
    fields = ['is_draft']
    success_url = reverse_lazy('posts_list')
    template_name = 'practice/posts_create.html'


class PostsListView(ListView):
    model = Posts
    template_name = 'practice/posts_list.html'

    ordering = ['id']
    paginate_by = 10


class PostsDetailView(DetailView):
    model = Posts
    template_name = 'practice/posts_detail.html'


"""
Comments
"""


class CommentsCreateView(CreateView):
    model = Comments
    fields = ['text', 'username', 'post']
    template_name = 'practice/comments_create.html'

    success_url = reverse_lazy('posts_list')

    # havent tested, need cellery being started
    email = ['sometestemail@test.com']
    text = ['new comment added']
    # send_mail.apply_async(text, email)


"""
profiles
"""


class UserProfileView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'practice/userprofile.html'
    fields = ['username', 'first_name', 'email', 'is_active']
    username = None



"""
authorization, authentification and so on
"""


def user_register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'practice/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'practice/register.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('startpage')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'practice/login.html', {'form': form})


def user_logout(request):
    return render(request, 'practice/logout.html')


def user_change_password(request, pk):
    u = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password2']
            u.set_password(make_password(password))
            u.save()
    else:
        form = PasswordForm()
    return render(request, 'practice/reset_password.html', {'form': form, 'pk': pk})
