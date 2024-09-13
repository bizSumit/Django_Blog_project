from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog, Author, Comment
from datetime import datetime
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic import CreateView, UpdateView ,DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm

# Create your views here.
# class HomepageView(TemplateView):
#     template_name = 'blogs/index.html'


# def index_functions(request):
#     all_blogs = Blog.objects.all()
#     context = {"blogs_key": all_blogs}
#     return render(request, 'blogs/index.html', context)

class BlogListView(ListView):
    model = Blog
    context_object_name = 'blogs_key'
    ordering = ['title','date']
    template_name = 'blogs/index.html'
    

def blog(request):
    return render(request, 'blogs/blog.html')


def about(request):
    return render(request, 'blogs/about.html')


# def detailed_blog(request, id):
#     blog = Blog.objects.get(pk=id)
#     return render(request, 'blogs/detailed_blog.html', {"blog": blog})

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogs/detailed_blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(blog=self.object)
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        blog = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            return redirect(blog.get_absolute_url())
        return self.get(request, *args, **kwargs)


def authors(request):
    all_author = Author.objects.all()
    context = {"authors": all_author}
    return render(request, 'blogs/authors.html', context)


def author_detail(request, author_id):
    author = Author.objects.get(pk=author_id)
    blogs = Blog.objects.filter(author=author)  #field name of Blog : author = object of author
    #context={"author": author,"blogs":blogs}
    return render(request, 'blogs/author_details.html', {"author":author, "blogs":blogs})


# def new_blog(request):
#     all_author = Author.objects.all()
#     if request.method == "POST":
#         title = request.POST.get('blog_title')
       
#         blog_text = request.POST.get('blog_text')
#         author_id = request.POST.get('author_id')
#         print("Blog title : ", title)
#         print("Author id :", author_id)
#         author = Author.objects.get(id=author_id)
#         date = datetime.now()

#         blog = Blog.objects.create(title=title, blog_text=blog_text,
#                                    author=author, date=date)
#         return redirect("index_url")
#     return render(request, 'blogs/new_blog.html', {"all_author":all_author})


class BlogCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Blog
    fields = ['title', 'blog_text', 'image']
    template_name = 'blogs/new_blogs_view.html'
    success_message = "Blog successfully saved"
    success_url = reverse_lazy('index_url')

    def form_valid(self, form):
        if not hasattr(self.request.user, "author"):
            author = Author.objects.create(name=self.request.user.username,
                                           genere="NewAuthor",
                                           email=self.request.user.email)
            form.instance.author = author
        else:
            form.instance.author = self.request.user.author
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Blog
    fields = ['title',  'blog_text','image']
    template_name = 'blogs/edit_blog.html'
    success_message = "Blog successfully updated"
    success_url = reverse_lazy('index_url')


class BlogDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Blog
    template_name = 'blogs/delete_blog.html'
    success_message = "Blog successfully deleted"
    success_url = reverse_lazy('index_url')
