from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='index_url'),
    path('blog/', views.blog, name='blog'),
    path('about-me-and-my-project/', views.about, name='about'),
    path('detailed-blog/<int:pk>', views.BlogDetailView.as_view(), name='detailed_blog'),
    path('author/', views.authors, name='authors'),
    path('author-details/<int:author_id>', views.author_detail, name='author_details'),
    path('new-blog/', views.BlogCreateView.as_view(), name='new_blog'),
    path('edit-blog/<int:pk>', views.BlogUpdateView.as_view(), name='edit_blog'),
    path('delete_blog/<int:pk>', views.BlogDeleteView.as_view(), name='delete_blog'),
]
