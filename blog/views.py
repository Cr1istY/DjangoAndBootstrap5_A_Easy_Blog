from django.shortcuts import render, redirect, reverse
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST, require_GET
from .models import Blog, BlogComment,BlogCategory
from .forms import PubBlogForm
from django.db.models import Q
from django.core.paginator import Paginator

import random
# Create your views here.

def index(request):
    blogs = Blog.objects.all()
    blogs = Paginator(blogs, 10)
    categories = BlogCategory.objects.all()
    page_number = request.GET.get('page')
    blogs_obj = blogs.get_page(page_number)
    pages = range(1, blogs_obj.paginator.num_pages + 1)
    return render(request, 'html/index.html', context={'blogs':blogs_obj, 'pages':pages, 'categories': categories})

def home(request):
    return render(request, 'html/home.html')

def blog(request, blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        return redirect('home')
    return render(request, 'html/blog_detail.html', context={'blog': blog})

@require_http_methods(['GET', 'POST'])
@login_required()
def pub(request):
    if request.method == 'GET':
        categories = BlogCategory.objects.all()
        return render(request, 'html/blog_pub.html', context={'categories': categories})
    else:
        form = PubBlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            category_id = form.cleaned_data.get('category')
            blog = Blog.objects.create(title=title, content=content, category_id=category_id, author=request.user)

            return JsonResponse({'code': 200, 'msg': '博客发布成功', 'data': {'blog_id': blog.id}})
        else:
            print(form.errors)
            return JsonResponse({'code': 400, 'msg': '发布失败'})

@require_POST
@login_required()
def pub_comment(request):
    blog_id = request.POST.get('blog_id')
    content = request.POST.get('content')
    BlogComment.objects.create(blog_id=blog_id, content=content, author=request.user)
    #
    return redirect(reverse("blog:blog_detail", kwargs={'blog_id': blog_id}))

@require_GET
def search(request):
    q = request.GET.get('q')
    blogs = Blog.objects.filter(Q(title__icontains=q) | Q(content__icontains=q) | Q(category__name__icontains=q) | Q(author__username__icontains=q) ).all()
    categories = BlogCategory.objects.all()
    return render(request, 'html/index.html', context={'blogs': blogs, 'categories': categories})

def recommend(request):
    blog = random.choice(Blog.objects.all())
    return render(request, 'html/blog_detail.html', context={'blog': blog})

