from django.forms import ModelForm
from.models import Post

### This class represents the form that accepts the users input. This form is used in all the html pages.

class PostForm(ModelForm):
    class Meta:
        model=Post
        fields= "__all__"