from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.db.models import Q
from django.http import Http404

from blog.models import Post, Category, Constants


def get_posts():
    return Post.objects.filter(
        Q(pub_date__lte=timezone.now())
        & Q(is_published=True)
        & Q(category__is_published=True)
    )


def index(request):
    template_name = 'blog/index.html'
    post_list = get_posts()[:Constants.POST_LIMIT]
    context = {'post_list': post_list}
    return render(request, template_name, context)


def post_detail(request, post_pk):
    template_name = 'blog/detail.html'
    post = get_object_or_404(
        Post, pk=post_pk,
        pub_date__lte=timezone.now(),
        category__is_published=True
    )
    if request.user == post.author or post.is_published:
        context = {'post': post}
        return render(request, template_name, context)
    raise Http404("У данного пользователя нет прав для просмотра"
                  " данного неопубликованного поста")


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(
        Category, slug=category_slug,
        is_published=True
    )

    post_list = get_posts().filter(category=category)
    context = {'category': category, 'post_list': post_list}
    return render(request, template_name, context)
