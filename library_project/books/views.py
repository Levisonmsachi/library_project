from django.views.generic import TemplateView, ListView, DetailView
from .models import Book

class HomeView(TemplateView):
    template_name = 'books/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_books = Book.objects.count()
        available_books = Book.objects.filter(is_available=True).count()
        recent_books = Book.objects.order_by('-created_at')[:3]


        context['welcome'] = 'Welcome to our Library'
        context['total_books'] = total_books
        context['available_books'] = available_books
        context['recent_books'] = recent_books
        return context
    
class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    
    def get_queryset(self):
        queryset = Book.objects.all()
        
        # Filter by status
        status = self.request.GET.get('status')
        if status == 'available':
            queryset = queryset.filter(is_available=True)
        elif status == 'checked_out':
            queryset = queryset.filter(is_available=False)
        
        # Search by title
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(title__icontains=search)
        
        return queryset

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'