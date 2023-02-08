from django import forms
from .models import User,Post

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class NewPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewPostForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Post
        fields = ['title', 'slug', 'content','status']