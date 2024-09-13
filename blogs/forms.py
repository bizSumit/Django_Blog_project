from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment_text']
        widgets = {
            'comment_text': forms.Textarea(attrs={'rows': 4}),
        }
