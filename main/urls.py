from django.urls import path

from . import views

urlpatterns = [
    path('', view=PaperView.as_view(), name='index'),
    path('author/', views.AuthorView.as_view(), name='author'),
    path('author/<str:author_url>/', views.AuthorDetailView.as_view(), name='author-detail'),
    path('author/<str:author_url>/delete/', views.AuthorDeleteView.as_view(), name='author-delete'),
    path('journal/', views.JournalView.as_view(), name='journal'),
    path('journal/<str:journal_url>/', views.JournalDetailView.as_view(), name='journal-detail'),
    path('journal/<str:journal_url>/delete/', views.JournalDeleteView.as_view(), name='journal-delete'),
    path('tag/', views.TagView.as_view(), name='tag'),
    path('tag/<str:tag_url>/delete/', views.TagDeleteView.as_view(), name='tag-delete'),
    path('add/', views.PaperCreateView.as_view(), name='paper-add'),
    path('<str:paper_url>/', views.PaperDetailView.as_view(), name='paper-detail'),
    path('<str:paper_url>/edit/', views.PaperUpdateView.as_view(), name='paper-update'),
    path('<str:paper_url>/delete/', views.PaperDeleteView.as_view(), name='paper-delete'),
    path('<str:paper_url>/add_one_tag/', views.add_one_tag, name='paper-add_tag'),
]
