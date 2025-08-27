from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content', 'picture']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "What's happening?",
                'rows': 3
            }),
            'picture': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }