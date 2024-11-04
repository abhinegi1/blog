from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control beautiful-input', 
                'placeholder': 'Enter the post title',
                'aria-describedby': 'titleHelp',
                'title': 'The title of your post should be concise and descriptive'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control beautiful-input', 
                'placeholder': 'Write your content here...', 
                'rows': 5,
                'aria-describedby': 'contentHelp',
                'title': 'Write the main content of your post. Be clear and engaging!'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control beautiful-input', 
                'placeholder': 'Your name or pen name',
                'aria-describedby': 'authorHelp',
                'title': 'Enter the author’s name'
            }),
        }
