from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
# Create your views here.

def home(request):
    currentuser = request.user.username
    frds = ['kumar', 'raja']  # have to get only friend list
    frds.append(currentuser)
    #posts = Post.objects.all()
    posts = []
    for i in range(len(frds)):
        lstpost = Post.objects.filter(postedBy=frds[i])
        posts.extend(lstpost)
        #posts = Post.objects.filter(postedBy=frds[i])
    posts.reverse()   # instead of reverse use date and time concept to view recent post in top
    return render(request, 'index.html', {'posts': posts})

def post(request):
    print("new post....")
    postType = 'I'
    postedBy = request.user.username
    description = request.POST['description']
    image = request.FILES['image']
    video = request.FILES['video']
    print("image type is:", type(image))
    print("image is:", image)
    isActive = True
    post = Post(postType = postType, postedBy = postedBy, description = description, image = image, video = video, isActive = isActive)
    post.save()
    print("post has been saved")
    return redirect('/')
