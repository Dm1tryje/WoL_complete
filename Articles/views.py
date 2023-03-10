from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from . import models

class ArticleListView(ListView):
    model = models.Article
    template_name = 'articles/article_list.html'

class ArticleDetailView(DetailView):
    model = models.Article
    template_name = 'articles/article_detail.html'

class ArticleUpdateView(UpdateView):
    model = models.Article
    fields = ['title', 'body', ]
    template_name = 'articles/article_edit.html'

class ArticleDeleteView(DeleteView):
    model = models.Article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('article_list')

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = models.Article
    template_name = 'articles/article_new.html'
    fields = ['title', 'body', 'author']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)