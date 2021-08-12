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

    def clean_comment_text(self):
        comment = self.cleaned_data.get('comment_text')

        if comment.isdigit():
            raise forms.ValidationError('Only Numbers are not allowed in comments')

        return comment


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'image', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title Here'}),
            'image': forms.ClearableFileInput(attrs={'class': 'custom-file-input'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description Here'})
        }

    def clean_image(self):
        image = self.cleaned_data.get('image')
        fifty_kb = 2**10 * 10 * 5
        if image and image.size > fifty_kb:
            raise forms.ValidationError('File is Greater than 50 kb.')
        return image
