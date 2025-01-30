from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Artwork, Category, Exhibition, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404

class HomePageView(ListView):
    model = Artwork
    template_name = 'app/home.html'
    context_object_name = 'artworks'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class ContactPageView(TemplateView):
    template_name = 'app/contact.html'




class ArtworkListView(LoginRequiredMixin, ListView):
    model = Artwork
    template_name = 'artwork/artwork_list.html'
    context_object_name = 'artworks'

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            if user.role == 'Artist':  
                return Artwork.objects.filter(artist=user)  # Artists see only their own artworks
            return Artwork.objects.all()  # Regular users see all artworks
        
        return Artwork.objects.none()  # If somehow user is not authenticated, return nothing



class ArtworkDetailView(DetailView):
    model = Artwork
    template_name = 'artwork/artwork_detail.html'
    context_object_name = 'artwork'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        artwork = self.object
        context['comments'] = artwork.comments.all()
        return context


class ArtworkCreateView(LoginRequiredMixin, CreateView):
    model = Artwork
    fields = ['title', 'image', 'description', 'category']
    template_name = 'artwork/artwork_create.html'
    success_url = reverse_lazy('artwork_list')

    def form_valid(self, form):
        # Ensure the artist is set to the currently logged-in user
        form.instance.artist = self.request.user
        return super().form_valid(form)

class ArtworkUpdateView(LoginRequiredMixin, UpdateView):
    model = Artwork
    fields = ['title', 'image', 'description', 'category']
    template_name = 'artwork/artwork_update.html'

    def get_success_url(self):
        return reverse_lazy('artwork_detail', kwargs={'pk': self.object.pk})

    def get_queryset(self):
        return Artwork.objects.filter(artist=self.request.user)

class ArtworkDeleteView(LoginRequiredMixin, DeleteView):
    model = Artwork
    template_name = 'artwork/artwork_delete.html'
    success_url = reverse_lazy('artwork_list')

    def get_queryset(self):
        return Artwork.objects.filter(artist=self.request.user)




class CategoryListView(ListView):
    model = Category
    template_name = 'category/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artworks'] = Artwork.objects.filter(category=self.object)
        return context


class CategoryCreateView(CreateView):
    model = Category
    fields = [ 'name','description']
    template_name = 'category/category_create.html'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'description']
    template_name = 'category/category_update.html'

    def get_success_url(self):
        return reverse_lazy('category_detail', kwargs={'pk': self.object.pk})

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category/category_delete.html'
    success_url = reverse_lazy('category_list')



class ExhibitionListView(ListView):
    model = Exhibition
    template_name = 'exhibition/exhibition_list.html'
    context_object_name = 'exhibitions'

class ExhibitionDetailView(DetailView):
    model = Exhibition
    template_name = 'exhibition/exhibition_detail.html'
    context_object_name = 'exhibition'

class ExhibitionCreateView(CreateView):
    model = Exhibition
    fields = [ 'title','date','location','artworks']
    template_name = 'exhibition/exhibition_create.html'
    success_url = reverse_lazy('exhibition_list')

class ExhibitionUpdateView(LoginRequiredMixin, UpdateView):
    model = Exhibition
    fields = ['title', 'date', 'location', 'artworks']
    template_name = 'exhibition/exhibition_update.html'

    def get_success_url(self):
        return reverse_lazy('exhibition_detail', kwargs={'pk': self.object.pk})



class ExhibitionDeleteView(LoginRequiredMixin, DeleteView):
    model = Exhibition
    template_name = 'exhibition/exhibition_delete.html'
    success_url = reverse_lazy('exhibition_list')

    def get_queryset(self):
        return Exhibition.objects.filter(artist=self.request.user)







class CommentDetailView(DetailView):
    model = Comment
    template_name = 'comment/comment_detail.html'
    context_object_name = 'comment'


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']
    template_name = 'comment/comment_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.artwork = Artwork.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('artwork_detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        artwork = Artwork.objects.get(pk=self.kwargs['pk'])
        context['artwork'] = artwork
        return context

class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'comment/comment_update.html'

    def get_success_url(self):
        return reverse_lazy('artwork_detail', kwargs={'pk': self.object.artwork.pk})



class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'comment/comment_delete.html'

    def get_success_url(self):
        return reverse_lazy('artwork_detail', kwargs={'pk': self.object.artwork.pk})