from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (HomePageView,
                    AboutPageView,
                    ContactPageView,
                    ArtworkListView,
                    ArtworkDetailView,
                    ArtworkCreateView,
                    ArtworkUpdateView,
                    ArtworkDeleteView,
                    CategoryListView,
                    CategoryDetailView,
                    CategoryCreateView,
                    CategoryUpdateView,
                    CategoryDeleteView,
                    ExhibitionListView,
                    ExhibitionDetailView,
                    ExhibitionCreateView,
                    ExhibitionUpdateView,
                    ExhibitionDeleteView,
                    CommentDetailView,
                    CommentCreateView,
                    CommentUpdateView,
                    CommentDeleteView,
                    )

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),

    path('artwork/', ArtworkListView.as_view(), name='artwork_list'),
    path('artwork/<int:pk>/', ArtworkDetailView.as_view(), name='artwork_detail'),
    path('artwork/create/', ArtworkCreateView.as_view(), name='artwork_create'),
    path('artwork/<int:pk>/update/', ArtworkUpdateView.as_view(), name='artwork_update'),
    path('artwork/<int:pk>/delete/', ArtworkDeleteView.as_view(), name='artwork_delete'),

    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

    path('exhibit/', ExhibitionListView.as_view(), name='exhibition_list'),
    path('exhibit/<int:pk>/', ExhibitionDetailView.as_view(), name='exhibition_detail'),
    path('exhibit/create/', ExhibitionCreateView.as_view(), name='exhibition_create'),
    path('exhibit/<int:pk>/update/', ExhibitionUpdateView.as_view(), name='exhibition_update'),
    path('exhibit/<int:pk>/delete/', ExhibitionDeleteView.as_view(), name='exhibition_delete'),

    path('comment/create/<int:pk>/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/', CommentDetailView.as_view(), name='comment_detail'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment_delete'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)