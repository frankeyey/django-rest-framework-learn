from django.urls import path
# from news.api.views import article_list_create_api_view, article_detail_create_api_view
from news.api.views import ArticleListCreateAPIView, ArticleDetailCreateAPIView, JournalistListCreateAPIView

urlpatterns = [
  # Using @api_view Decorator
  # path("articles/", article_list_create_api_view, name="article-list"),
  # path("articles/<int:pk>/", article_detail_create_api_view, name="article-detail")

  # Using APIView Class
  path("articles/", ArticleListCreateAPIView.as_view(), name="article-list"),
  path("articles/<int:pk>/", ArticleDetailCreateAPIView.as_view(), name="article-detail"),
  path("journalists/", JournalistListCreateAPIView.as_view(), name="journalist-list"),
]