from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreateUserView, LoginAPIView
from .api import CategoryViewSet, PersonViewSet, EventViewSet,CommentViewSet,HistoricalPeriodViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'persons', PersonViewSet)
router.register(r'events', EventViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'historical_periods', HistoricalPeriodViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', CreateUserView.as_view(), name='register'),
    path('api/login/', LoginAPIView.as_view(), name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)