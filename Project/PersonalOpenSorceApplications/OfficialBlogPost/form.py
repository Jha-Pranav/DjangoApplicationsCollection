from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','text')

        widget ={
            'title' :forms.TextInput(attrs={'class':'textInputClass'}),
            'text' : forms.Textarea(attrs={'class' : 'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')

        widget={
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }
