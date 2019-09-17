from django.shortcuts import render, get_list_or_404, redirect
from django.views.generic import (TemplateView, ListView, CreateView, 
                UpdateView, DeleteView,DetailView)
from .models import Post,Comment
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .form import PostForm, CommentForm
from django.urls import reverse_lazy

# Create your views here.

class AboutView(TemplateView):
    template_name = 'OfficialBlogPost/about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')

class PostDetailsView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'OfficialBlogPost/post_detail.html'

    form_class = PostForm

    model = Post

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'OfficialBlogPost/post_detail.html'

    form_class = PostForm
    model = Post


class PostDeleteView(LoginRequiredMixin,DeleteView):
    login_url ='/login/'
    success_url = reverse_lazy('post_list')


class PostDraftView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'OfficialBlogPost/post_detail.html'

    model = Post

    def get_queryset(self):

        return Post.objects.filter(pub_date__isnull=True).order_by('-creation_time')


# ######################################

@login_required
def post_publish(request,pk):
    print('*'*10,pk)
    post = get_list_or_404(Post, pk=pk)[0]
    print('*'*100, post)
    post.publish()
    return redirect('post_detail', pk)


@login_required
def add_comment_to_post(request,pk):
    post = get_list_or_404(Post, pk=pk)[0]
    if request.method == 'Post':
        form = CommentForm(request.POST)
        if form.is_valid() :
            Comment = form.save(commit=False)
            comment.post = post
            Comment.save()
            return redirect('post_datail', pk=post.pk)
    else:
        form= CommentForm()
    return render(request, 'OfficialBlogPost/comment_form.html', {'form': form})

@login_required
def approve_comment(request,pk):
    comment = get_list_or_404(Comment,pk=pk)[0]
    comment.approve()
    return redirect('post_detail', comment.post.pk)


def remove_comment(request,pk):
     comment = get_list_or_404(Comment, pk=pk)[0]
     comment_pk = comment.post.pk
     comment.delete()
     return redirect('post_detail', pk = comment_pk)




