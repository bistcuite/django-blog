from importlib.resources import contents
from multiprocessing import AuthenticationError
from django.shortcuts import render
from django.views import generic
from .models import Post
from .forms import NewPostForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class NewPost(LoginRequiredMixin,generic.CreateView):
    model = Post
    form_class  = NewPostForm
    template_name = 'newpost.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
def fgfd(request):
    if request.method == "POST" :
        form = NewPostForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            slug = form.cleaned_data['slug']
            content = form.cleaned_data['content']

            post = Post(title=title,slug=slug,content=content,author=request.user,status=1)
            post.save()
            return HttpResponseRedirect(f'/{slug}')
    form = NewPostForm()
    return render(request, 'newpost.html',{'form':form})
