from django.urls import path

from . import views

urlpatterns = [
    path('', view=PaperView.as_view(), name='index'),
    path('author/', views.AuthorView.as_view(), name='author'),
    path('author/add/', views.AuthorCreateView.as_view(), name='author-add'),
    path('author/<str:author_url>/', views.AuthorDetailView.as_view(), name='author-detail'),
    path('author/<str:author_url>/edit/', views.AuthorUpdateView.as_view(), name='author-update'),
    path('author/<str:author_url>/delete/', views.AuthorDeleteView.as_view(), name='author-delete'),
    path('journal/', views.JournalView.as_view(), name='journal'),
    path('journal/add/', views.JournalCreateView.as_view(), name='journal-add'),
    path('journal/<str:journal_url>/', views.JournalDetailView.as_view(), name='journal-detail'),
    path('journal/<str:journal_url>/edit/', views.JournalUpdateView.as_view(), name='journal-update'),
    path('journal/<str:journal_url>/delete/', views.JournalDeleteView.as_view(), name='journal-delete'),
    path('tag/', views.TagView.as_view(), name='tag'),
    path('tag/add/', views.TagCreateView.as_view(), name='tag-add'),
    path('tag/<str:tag_url>/', views.TagDetailView.as_view(), name='tag-detail'),
    path('tag/<str:tag_url>/edit/', views.TagUpdateView.as_view(), name='tag-update'),
    path('tag/<str:tag_url>/delete/', views.TagDeleteView.as_view(), name='tag-delete'),
    path('paper/add/', views.PaperCreateView.as_view(), name='paper-add'),
    path('paper/<str:paper_url>/', views.PaperDetailView.as_view(), name='paper-detail'),
    path('paper/<str:paper_url>/edit/', views.PaperUpdateView.as_view(), name='paper-update'),
    path('paper/<str:paper_url>/delete/', views.PaperDeleteView.as_view(), name='paper-delete'),
    path('paper/<str:paper_url>/add_one_tag/', views.add_one_tag, name='paper-add_tag'),
]