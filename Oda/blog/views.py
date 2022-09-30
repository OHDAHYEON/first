from audioop import reverse
from django.shortcuts import render
from django.views.generic import *
from django.views.generic.dates import *
from blog.models import Post
from django.conf import settings

from blog.forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render

from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin


# Create your views here.

#-- ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 6

#-- DetailView
class PostDV(DetailView):
    model = Post

#-- ArchiveView
class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True
    # month_format = '%d' # 디폴트 값

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_dt'
    month_format = '%m'

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_dt'
    month_format = '%m'

class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_dt'

class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'

class TaggedObjectLV(ListView):
    model = Post
    template_name = 'taggit/taggit_post_list.html'

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context

#-- FormView
class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        post_list = Post.objects.filter(Q(title__icontains=searchWord) | 
                                        Q(description__icontains=searchWord) |
                                        Q(content__icontains=searchWord)).distinct()
        context = { 'form' : form, 
                    'search_term' : searchWord,
                    'object_list' : post_list
                }
        # context = {}
        # context['form'] = form
        # context['search_term'] = searchWord
        # context['objet_list'] = post_list

        return render(self.request, self.template_name, context)

# LoginRequiredMixin -> 로그인한 사용자가 아니면 로그인 페이지로 이동
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # fields = ['title', 'slug', 'description', 'content', 'tags']
    # initial = {'slug' : '자동으로-완성되니-적지마세요'}
    fields = ['title', 'description', 'content', 'tags', 'image']
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

# LoginRequiredMixin -> 로그인한 사용자가 아니면 로그인 페이지로 이동
# object_list -> 현재 로그인한 사용자가 작성한 Post
class PostChangeLV(LoginRequiredMixin, ListView):
    template_name = 'blog/post_change_list.html'

    def get_queryset(self):
        return Post.objects.filter(owner = self.request.user)

# OwnerOnlyMixin -> 작성자만이 수정할 수 있도록
class PostUpdateView(OwnerOnlyMixin, UpdateView):
    model = Post
    # fields = ['title', 'slug', 'description', 'content', 'tags']
    fields = ['title', 'description', 'content', 'tags', 'image']
    success_url = reverse_lazy('blog:index')

# OwnerOnlyMixin -> 작성자만이 삭제할 수 있도록
class PostDeleteView(OwnerOnlyMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')