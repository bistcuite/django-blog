from django import forms
from .models import User

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class NewPostForm(forms.Form):
    title = forms.CharField(max_length=200)
    slug = forms.SlugField(max_length=200)
    content = forms.CharField(widget=forms.Textarea)
    status = forms.Select(choices=STATUS)