from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

def post_list(request):
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, request.GET.get('per_page', 10))

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'page_obj': page_obj})