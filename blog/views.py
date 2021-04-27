from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import (
    ListView,
    DetailView,
)
from django.urls import reverse_lazy 


class MainView(ListView):
    model = Post
    template_name = 'blog/home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    
    fields = ['title','author','body']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['title', 'body']

    '''
    def dispatch(self,request,id,*args,**kwargs):
        post = get_object_or_404(Post,id=id)
        if obj.user != self.author:
            raise Http404('You are not allowed')
        return super(BlogUpdateView,self).dispatch(request, *args, **kwargs)
        # time no dey to get creative but i will love to improve on this functionality later
    '''

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')

def comment_view(request):

    context = {}
    return render (request,'blog/comment.html',context)
