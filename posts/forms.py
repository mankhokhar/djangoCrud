from django import forms
from . import models


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['comment_text']
        widgets = {
            'comment_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comment Here'},),
        }
        labels = {
            'comment_text': '',
        }
