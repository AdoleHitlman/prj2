from django import forms
from django.urls import reverse

from catalog.models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'preview']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.is_published = True
        if commit:
            instance.save()
        return instance

    def get_success_url(self):
        return reverse('index')
