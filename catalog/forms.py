from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.core.exceptions import ValidationError
from django.urls import reverse

from catalog.models import Blog
from catalog.models import Product
from catalog.models import Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'photo', "category", "price"]

    def clean_name(self):
        name = self.cleaned_data['name']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']

        for word in forbidden_words:
            if word in name.lower():
                raise ValidationError("Название продукта содержит запрещенное слово.")

        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']

        for word in forbidden_words:
            if word in description.lower():
                raise ValidationError("Описание продукта содержит запрещенное слово.")

        return description

    def get_success_url(self):
        return reverse('catalog')

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ['version_number', 'version_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Создать версию'))

    def get_success_url(self):
        return reverse('catalog')

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance


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
