from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post(request):
    print("new post....")
    postType = 'I'
    postedBy = 1001
    description = request.POST['description']
    image = request.FILES['image']
    print("image type is:", type(image))
    print("image is:", image)
    isActive = True
    post = Post(postType = postType, postedBy = postedBy, description = description, image = image, isActive = isActive)
    post.save()
    print("post has been saved")
    return redirect('/')
