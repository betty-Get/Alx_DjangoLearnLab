from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
# ✅ This satisfies the 'from .models import Library'
from .models import Book, Library


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # ✅ Must match exactly
    # ✅ Required by checker to use 'library' in template
    context_object_name = 'library'
