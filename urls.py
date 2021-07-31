from django.urls import include, path
from rest_framework import routers
from .views import  ListAuthorView, ListBookView, BookIsbnSearch, BookSearchAuthor, CreateBook, CreateAuthor

# router = routers.DefaultRouter()
# router.register(r'author',AuthorViewSet)
# router.register(r'book', BookViewSet)

urlpatterns = [
    # path('', include(router.urls)),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # without admin
    path('isbnsearch/', BookIsbnSearch.as_view()),
    path('authorsearch/', BookSearchAuthor.as_view()),
    path('listbook/', ListBookView.as_view()),
    path('listauthor/', ListAuthorView.as_view()),

    # with admin
    path('createbook/', CreateBook.as_view()),
    path('createauthor/', CreateAuthor.as_view()),

]