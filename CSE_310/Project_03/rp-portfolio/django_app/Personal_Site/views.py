from django.shortcuts import redirect, render
from .models import Post
from .forms import PostForm

### These functions are called to render all the html pages for the site.

def home(request):
### These line get the input in the form and send it to the database.

    if request.method== "POST":
        form= PostForm(request.POST)
        form.save()
        return redirect("../posts/")
    else:
        form= PostForm()
    context = {"form": form}
    return render(request, 'Personal_Site/home.html', context)

def summary(request):
    if request.method== "POST":
        form= PostForm(request.POST)
        form.save()
        return redirect("../posts/")
    else:
        form= PostForm()
    context = {"form": form}
    return render(request, 'Personal_Site/summary.html', context)

def post(request):
    if request.method== "POST":
        form= PostForm(request.POST)
        form.save()
        return redirect("../posts/")
    else:
        form= PostForm()

### The dictionary below gets all the posts in the database and sends them to the posts webpage.
    database_data={
    "posts":Post.objects.all(),
    "number_posts":Post.objects.count(),
    "form":form,
    }   
    return render(request, 'Personal_Site/posts.html', database_data)
