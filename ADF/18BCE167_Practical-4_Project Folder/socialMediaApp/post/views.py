from django.shortcuts import render,redirect
from .models import Post
from .forms import createPostForm
from socialMediaApp import settings
# Create your views here.


def displayPost(req):
    post=Post.objects.all()
    username=""
    if req.user:
        username=req.user
    print(username)
    print(settings.MEDIA_ROOT)
    return render(req,'displayPost.html',{"posts":post,"username":username})

def createPost(req):
    if req.method == 'POST':
        form = createPostForm(req.POST,req.FILES)
        if form.is_valid():
            username = req.user
            posts = req.POST['post']
            title = req.POST['title']
            post=""
            try:
                image = req.FILES['image']
                try:
                    file = req.FILES['file']
                    post = Post(username=username,post=posts,title=title,image=image,file=file)
                except:
                    post = Post(username=username,post=posts,title=title,image=image)
            except:
                post = Post(username=username,post=posts,title=title)
            post.save()
            return redirect('displayPost')
    else:
        form = createPostForm()
        print(type(form))

    return render(req, 'createPost.html', {'form': form})


def updatePost(req, **primarykey):
    postId = primarykey['pk']
    post=list(Post.objects.filter(username=req.user,id=postId))[0]
    if req.method == 'POST':
        # form = createPostForm(req.POST,req.FILES)
        username = req.user
        title = req.POST['title']
        posts = req.POST['post']

        post = list(Post.objects.filter(username=username,
                    id=postId))[0]
        post.post=posts
        post.title=title
        try:
            image = req.FILES['image']
            post.image=image
        except:
            pass
        post.save()
        return redirect('displayPost')
    else:
        form = createPostForm()
        print(type(form))

    return render(req,'updatePost.html',{"post":post})

def deletePost(req, **primarykey):
    postId=primarykey['pk']
    Post.objects.filter(username=req.user,id=postId).delete()
    return redirect('displayPost')

def myPost(req):
    post=Post.objects.filter(username=req.user)
    return render(req,'myPost.html',{"posts":post})
