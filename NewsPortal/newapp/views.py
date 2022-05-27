from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from .models import Post
from .filters import PostFilter
from .forms import PostForm


class PostNewsList(ListView):
    model = Post
    ordering = ['-dateCreation']
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 2  # Тут 2 потому что всего 4 публикации
    form_class = PostForm


class Post_Filter(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'news_detail.html'
    context_object_name = 'news'
    #queryset = Post.objects.all()


class PostCreateView(CreateView):
    template_name = 'add.html'
    form_class = PostForm


class PostUpdateView(UpdateView):
    template_name = 'edit.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):
    template_name = 'delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
