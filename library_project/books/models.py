from django.db import models

class Book(models.Model):
    # Basic information
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    
    # Book details
    description = models.TextField()
    isbn = models.CharField(max_length=13, unique=True)  # ISBN is 13 digits
    
    # Status
    is_available = models.BooleanField(default=True)
    
    # Dates
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # String representation
    def __str__(self):
        return self.title