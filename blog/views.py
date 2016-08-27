from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.http import Http404


def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
	return render(request, "blog/post_list.html", {"posts": posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if post.published_date==None or post.published_date>timezone.now():
		raise Http404('Post has not been published yet!')
	return render(request, "blog/post_detail.html", {"post": post})

# Create your views here.
