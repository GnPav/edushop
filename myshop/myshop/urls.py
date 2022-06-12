from django.urls import path, re_path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^cart/', include('cart.urls', namespace='cart')),
    re_path(r'^coupons/', include('coupons.urls', namespace='coupons')),
    re_path(r'^', include('shop.urls', namespace='shop')),
    re_path(r'^orders/', include('orders.urls', namespace='orders')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)