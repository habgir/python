from typing import Optional
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render,get_object_or_404
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from .models import post
from django.core.paginator import Paginator


def home(request):
    context = {
    'posts':post.objects.all()
    }
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model = post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
class PostDetailView(DetailView):
    model = post
class PostCreateView(LoginRequiredMixin,CreateView):
    model = post
    fields = ['title','content']

    def form_valid(self, form) :
        form.instance.auther = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = post
    fields = ['title','content']
    def form_valid(self, form) :
        form.instance.auther = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.auther:
            return True
        return False
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = post
    template_name = 'blog/post_delete.html'
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.auther:
            return True
        return False


class MyPostView(ListView): 
    model = post      
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts' 
    paginate_by = 3
    def get_queryset(self):
        user = get_object_or_404(User,username =self.kwargs.get('username'))
        return post.objects.filter(auther= user).order_by('-date_posted')
    
def about(request):
    return render(request,'blog/about.html',{'title':'about'})




