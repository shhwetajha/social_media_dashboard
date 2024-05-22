from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from accounts.views import *
from django.http import HttpResponse
from .models import *

# Create your views here.
@login_required(login_url='signin')
def view_home(request):
    user=account.objects.get(username=request.user.username)
    user_profile=Profile.objects.get(user=user)
    posts=post.objects.all()
    # comments=CommentPost.objects.all().filter(post_id=posts.id).order_by('date_added')
    context={'user':user,'profile':user_profile,'posts':posts}
    return render(request,'index.html',context)

@login_required(login_url='signin')
def view_upload(request):
    if request.method=='POST':
        user=request.user.username
        image=request.FILES.get('image_upload')
        caption=request.POST['caption']
        post_data=post.objects.create(user=user,image=image,caption=caption)
        return redirect('home')
    else:
        return redirect('home')

@login_required(login_url='signin')
def view_likepost(request):
    username=request.user.username
    post_id=request.GET.get('post_id')

    Post=post.objects.get(id=post_id)
    like_filter=LikePost.objects.filter(post_id=post_id,username=username).first()
    if like_filter == None:
        new_like=LikePost.objects.create(username=username,post_id=post_id)
        new_like.save()
        Post.no_of_likes=Post.no_of_likes+1
        Post.save()
        return redirect('home')
    else:
        like_filter.delete()
        Post.no_of_likes=Post.no_of_likes-1
        Post.save()
        return redirect('home')
    
@login_required(login_url='signin')
def view_commentpost(request,post_id):
    if request.method=='POST':
        user=request.user
        postt_id=post_id
        Post=post.objects.get(id=post_id)

        print(post_id)
        comment=request.POST.get('comment')
        comment_data=CommentPost.objects.create(user=request.user,post_id=postt_id,comment=comment)
        comment_data.save()
        Post.comments=comment_data
        Post.save()

        return redirect('home')
    else:     
        return render(request,'home.html')



    

# def view_signup(request):
#     return render(request,'signup.html')