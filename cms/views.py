from django.shortcuts import render

# Create your views here.
from.models import Post
def homepage(r):
    return render(r,"index.html" ,{"post": Post.objects.all()})