from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Posts, Comments
from django.urls import reverse_lazy
from .forms import UserRegistrationForm
from practice.tasks import send_mail
from django.contrib.auth.models import User as User


def startpage(request):
    return HttpResponse("You are on startpage")

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

    # havent tested, need cellery beimg started
    email = ['sometestemail@test.com']
    text = ['new comment added']
    # send_mail.apply_async(text, email)

"""
profiles
"""
class UserProfileView(DetailView):
    model = User
    template_name = 'practice'

"""
authorization, authentification and so on
"""
def register(request):
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
