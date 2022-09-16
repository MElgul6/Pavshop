
from django.shortcuts import render,redirect
from django.views.generic.edit import FormMixin
from .forms import CommentForm
from django.urls import reverse_lazy
from Blog.models import Blog, Tag, Comment
from Product.models import Category
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.db.models import Count



class BlogListView(ListView):
    model=Blog
    context_object_name='blogs'
    template_name='blog-list.html'
    paginate_by=3

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        # context['category'] = Category.objects.all()
        context["recent_posts"] = Blog.objects.order_by("-created_at")[:3]
        context["categories"] = Blog.objects.values('category__title').annotate(count = Count('category'))
        context['tags'] = Tag.objects.all()
        context['blogs'] = Blog.objects.all()
        return context



class BlogDetailView(FormMixin,DetailView):
    model=Blog
    form_class = CommentForm
    context_object_name='blog'
    template_name='blog-detail.html'

    def get_success_url(self):
        return reverse_lazy('blog', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["comments"] = Comment.objects.filter(blog__title=self.object)
        context["number_comments"] = len(context["comments"])
        context["tags"] = Tag.objects.all()
        context["recent_posts"] = Blog.objects.order_by("-created_at")[:3]
        context["related_blogs"] = Blog.objects.filter(category = self.object.category).exclude(id=self.object.pk)
        context["categories"] = Blog.objects.values('category__title').annotate(count = Count('category'))
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if request.user.is_authenticated:
            if form.is_valid():
                form.instance.blog = self.object
                form.instance.author = request.user
                form.save()
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        else:
            return redirect(reverse_lazy('login'))

            

    
   
        
