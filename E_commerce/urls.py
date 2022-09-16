from django.contrib import admin
from django.urls import path,include
from django.conf.urls.i18n import i18n_patterns
from Core.views import contact,index,about
from Cart.views import checkout,shopping
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('User/', include('User.urls')),
    
    
    path('',include('Product.urls')),
    path('api/', include('Blog.api.urls')),
    path('api/', include('Cart.api.urls')),
    path('api/', include('Product.api.urls')),
    path('api/', include('User.api.urls')),
    path('',include('Blog.urls')),
    path('',include('Cart.urls')),
    path('',include('Core.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('api/token/', TokenObtainPairView.as_view(), name='token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)


urlpatterns += i18n_patterns(
    path("i18n/", include("django.conf.urls.i18n")),
    path('', include('Core.urls')),
    path('', include('Product.urls')),
    path('', include('Blog.urls')),
    path('', include('Cart.urls')),
    path('User/', include('User.urls')),
)