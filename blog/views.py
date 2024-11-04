# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from datetime import datetime
from django import forms
from django.contrib.auth.models import User

# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/post_list.html', {'posts': posts})

def post_list(request):
    query = request.GET.get('q')  # Get the search query from the URL
    if query:
        posts = Post.objects.filter(title__icontains=query)  # Filter posts based on title
    else:
        posts = Post.objects.all()  # Get all posts if no query

    return render(request, 'blog/post_list.html', {'posts': posts})
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    current_year = datetime.now().year
    return render(request, 'blog/post_detail.html', {'post': post, 'current_year': current_year})

@login_required  # Protect this view so only logged-in users can create a post
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Set the author to the logged-in user
            post.save()
            return redirect('post_list')  # Redirect to the list view after saving
    else:
        form = PostForm()

    return render(request, 'blog/post_form.html', {'form': form})

@login_required  # Protect this view so only logged-in users can edit a post
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Redirect to the list view after saving
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('post_list')  # Redirect to post list after login
        else:
            # Handle invalid login
            return render(request, 'blog/login.html', {'error': 'Invalid username or password'})
    
    return render(request, 'blog/login.html')

# View for user signup
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, email=email, password=password)
            login(request, user)
            return redirect('post_list')  # Redirect to post list after signup
    else:
        form = UserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})





def logout_view(request):
    logout(request)
    return redirect('post_list')  # Redirect to post list after logout



class UsernamePasswordResetForm(forms.Form):
    username = forms.CharField(max_length=254, required=True)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("No user with that username exists.")
        return username
    

def username_password_reset(request):
    if request.method == 'POST':
        form = UsernamePasswordResetForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            return redirect('password_reset_confirm', user_id=user.id)  # Redirect to password reset confirm
    else:
        form = UsernamePasswordResetForm()

    return render(request, 'registration/username_password_reset.html', {'form': form})

