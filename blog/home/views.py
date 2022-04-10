from imp import reload
from multiprocessing import context
from optparse import IndentedHelpFormatter
from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.contrib import auth
import os
from .form import *


##################################################
def home(request):
    context={'blogs': Blogmodel.objects.all()}
    return render(request,'home.html',context)
##################################################


##################################################
def see_blog(request,slug):
    context={}
    try:
        blog_obj=Blogmodel.objects.filter(slug=slug).first()
        context['blog']=blog_obj
    except Exception as e:
        print(e)
    return render(request,'see_blog.html',context)
##################################################


##################################################
def blog_list(request):
    context={}
    try:
        blog_objs=Blogmodel.objects.filter(user=request.user)
        context['blog_objs']=blog_objs
    except Exception as e:
        print(e)
    return render(request,'blog_list.html',context)
##################################################


##################################################
def blog_update(request,slug):
    context={}
    try:
        blog_obj=Blogmodel.objects.get(slug=slug)
        if blog_obj.user != request.user:
            return redirect('/')
        initial_dict={
            'content':blog_obj.content
        }
        form=BlogForm(initial=initial_dict)
        if request.method=='POST':
            title=request.POST.get('title')
            form=BlogForm(request.POST)
            if form.is_valid():
                content=form.cleaned_data['content']
            blog_obj.title=title
            blog_obj.content=content
            blog_obj.save()
        context['form']=form
        context['blog_obj']=blog_obj
    except Exception as e:
        print(e)
    return render(request, 'blog_update.html',context)
##################################################


##################################################
def image_update(request,slug):
    context={}
    blog_obj=Blogmodel.objects.get(slug=slug)
    if blog_obj.user != request.user:
        return redirect('/')
    if request.method=='POST':
        image=request.FILES['image']
        img_name=request.FILES['image'].name
        fs=FileSystemStorage()
        file=fs.save(image.name,image)
        fileurl=fs.url(file)
        report=img_name
        if len(image)>0:
            Blogmodel.objects.filter(slug=slug).update(image=image)   
            return redirect('/blog_list/') 
    return render(request, 'image_update.html',context)
##################################################


##################################################
def blog_delete(request,id):
    try:
        blog_obj=Blogmodel.objects.get(id=id)
        if blog_obj.user == request.user:
            blog_obj.delete()
    except Exception as e:
        print(e)
    return redirect('/blog_list/')
##################################################


##################################################
def login_view(request):
    return render(request,'login.html')
##################################################


##################################################
def register_view(request):
    return render(request, 'register.html')
##################################################


##################################################
def logout_view(request):
    auth.logout(request)
    return redirect('/')
##################################################


##################################################
def add_blog(request):
    context= {'form':BlogForm}
    try:
        if request.method=='POST':
            form=BlogForm(request.POST)
            image=request.FILES['image']
            title=request.POST.get('title')
            user=request.user
            if form.is_valid():
                content=form.cleaned_data['content']

            blog_obj=Blogmodel.objects.create(user=user,image=image,title=title,content=content)
            print(blog_obj)
            return reload('/add_blog/')
    except Exception as e:
        print(e)
    return render(request,'add_blog.html',context)
##################################################