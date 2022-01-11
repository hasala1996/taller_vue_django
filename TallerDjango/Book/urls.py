from Book.serializer import AuthorSerializer
from rest_framework import routers
from .viewsets import AuthorViewSet, BookViewSet

router = routers.SimpleRouter()
router.register('books', BookViewSet)
router.register('author', AuthorViewSet)

urlpatterns = router.urls
