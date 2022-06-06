from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from blog.forms import Comment_detail_Form
from blog.models import Blog, Comment_blog
from home.models import Informations
from room.models import Rooms, Category
from django.core.paginator import (Paginator, PageNotAnInteger, EmptyPage)



def blog(request):
    info = Informations.objects.all()
    category = Category.objects.all()
    blog_piked = Blog.objects.all().order_by('?')[:8]
    blog = Blog.objects.all()
    comment_blog = Comment_blog.objects.all()
    paginator = Paginator(blog, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        blog = paginator.page(page)
    except PageNotAnInteger:
        blog = paginator.page(1)
    except EmptyPage:
        blog = paginator.page(paginator.num_pages)
    context = {
        'info': info,
        'category': category,
        'blog':blog,
        'comment_blog':comment_blog,
        'blog_piked':blog_piked,
    }
    return render(request, 'news.html', context)


def blog_detail(request,id):
    info = Informations.objects.all()
    category = Category.objects.all()
    allblog = Blog.objects.all().order_by('?')[:2]
    blog = Blog.objects.all().order_by('?')[:8]
    blog_detail = Blog.objects.get(pk=id)
    comment_blog = Comment_blog.objects.filter(blog_id=id, status='True')
    comment_blog_count = comment_blog.count()
    context = {
        'category': category,
        'info': info,
        'blog_detail':blog_detail,
        'comment_blog':comment_blog,
        'comment_blog_count':comment_blog_count,
        'allblog':allblog,
        'blog':blog,
    }
    return render(request, 'blog_detail.html', context)


def comment_blog(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = Comment_detail_Form(request.POST)
        if form.is_valid():
            data = Comment_blog()
            data.name = form.cleaned_data['name']
            data.surname = form.cleaned_data['surname']
            data.phone = form.cleaned_data['phone']
            data.comment = form.cleaned_data['comment']
            data.ip = request.META.get('REMOTE_ADDR')
            data.blog_id = id
            data.save()
            messages.success(request, "Sizning izohingiz qabul qilindi !")
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)