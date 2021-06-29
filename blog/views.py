from datetime import time
from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    
    all_posts=Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date') #method chaining primero filtro, despues ordeno con cadena de metodos
    print(all_posts)
    return render(request,'blog/post_list.html', {'all_posts':all_posts})  #contentdiccionary, envia todos los posts al html