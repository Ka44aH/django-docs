from django.contrib import admin
from django.urls import path, include, re_path
import testdocs.views as v
from .views import serve_docs


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', v.register, name="register"),
    re_path(r"^(?P<path>.*)$", serve_docs, name="docs_files"),
]
