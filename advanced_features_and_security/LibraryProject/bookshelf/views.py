from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

# View for viewing an book
@permission_required('app_name.can_view', raise_exception=True)
def book_detail(request, pk):
    books = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': books})

# View for creating an book
@permission_required('app_name.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        # handle form submission
        pass
    return render(request, 'book_form.html')

# View for editing an book
@permission_required('app_name.can_edit', raise_exception=True)
def book_edit(request, pk):
    books = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        # handle form submission
        pass
    return render(request, 'book_form.html', {'book': books})

# View for deleting an book
@permission_required('app_name.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')
