from django.urls import path, include
from .views import CustomUserCreateView, EspacoEsportivo
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'espacos-esportivos', EspacoEsportivo, basename='espacos-esportivos')

schema_view = get_schema_view(
   openapi.Info(
      title="Sua API",
      default_version='v1',
      description="Descrição da sua API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contato@exemplo.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    #urls do swagger
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


    #urls das views
    path('api/register/', CustomUserCreateView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
]