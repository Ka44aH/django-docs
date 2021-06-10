from django.shortcuts import render
from .forms import RegisterForm
from django.http.response import Http404
try:
    from django.core.urlresolvers import reverse
except ImportError:
    from django.urls import reverse

from django.views.static import serve
from django.conf import settings
from django.contrib.auth.decorators import login_required


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

    else:
        form = RegisterForm()

    return render(response, "register.html", {"form": form})


DOCS_ROOT = getattr(settings, 'DOCS_ROOT', None)


@login_required
def serve_docs(request, path, **kwargs):
    if 'document_root' not in kwargs:
        kwargs['document_root'] = DOCS_ROOT
    if path.startswith('ref'):
        if request.user.is_superuser:
            return serve(request, path, **kwargs)
        else:
            path = ''
            return serve(request, path, **kwargs)
    try:
        return serve(request, path, **kwargs)
    except Http404:

        raise
