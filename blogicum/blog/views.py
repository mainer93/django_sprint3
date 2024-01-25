from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.db.models import Q

from blog.models import Post, Category


def index(request):
    template_name = 'blog/index.html'
    post_list = Post.objects.filter(
        Q(pub_date__lte=timezone.now())
        & Q(is_published=True)
        & Q(category__is_published=True)
    ).order_by('pub_date')[:5]

    context = {'post_list': post_list}
    return render(request, template_name, context)


def post_detail(request, post_pk):
    template_name = 'blog/detail.html'
    post = get_object_or_404(
        Post, pk=post_pk,
        is_published=True, pub_date__lte=timezone.now(),
        category__is_published=True
    )
    context = {'post': post}
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(
        Category, slug=category_slug,
        is_published=True
    )

    post_list = Post.objects.filter(
        category=category,
        pub_date__lte=timezone.now(),
        is_published=True
    )
    context = {'category': category, 'post_list': post_list}
    return render(request, template_name, context)
