from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Article

# View for viewing an article
@permission_required('app_name.can_view', raise_exception=True)
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_detail.html', {'article': article})

# View for creating an article
@permission_required('app_name.can_create', raise_exception=True)
def article_create(request):
    if request.method == 'POST':
        # handle form submission
        pass
    return render(request, 'article_form.html')

# View for editing an article
@permission_required('app_name.can_edit', raise_exception=True)
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        # handle form submission
        pass
    return render(request, 'article_form.html', {'article': article})

# View for deleting an article
@permission_required('app_name.can_delete', raise_exception=True)
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('article_list')
