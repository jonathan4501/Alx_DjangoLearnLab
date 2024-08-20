
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm

def book_list(request):
    search = request.GET.get('search', '')
    books = Book.objects.filter(Q(title__icontains=search) | Q(author__icontains=search))
    return render(request, 'book_list.html', {'books': books})

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'form_example.html', {'form': form})

@permission_required('bookshelf.can_view', raise_exception=True)
def view_book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form': form})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return render(request, '404.html')
    if request.method == 'POST':
        # Edit book logic here
        pass
    return render(request, 'edit_book.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        book.delete()
        return redirect('book_list')
    except Book.DoesNotExist:
        return render(request, '404.html')