# from django.contrib import admin
# from django.urls import path, include

# from django.conf.urls.i18n import set_language

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('hotel.urls')),
#     path('set_language/', set_language, name='set_language'),
# ]


# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('hotel.urls')),
#     path('accounts/', include('accounts.urls')),
# ]


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hotel.urls')),
    path('accounts/', include('accounts.urls')),  # 👈 Include this
]
