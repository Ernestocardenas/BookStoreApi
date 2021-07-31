from django.db import models

# Create your models here.

class Author(models.Model):
    FirstName = models.CharField(max_length=128, null=False, blank=False)
    LastName = models.CharField(max_length=128, null=False, blank=False)
    Biography =  models.TextField(max_length=8000,null=False, blank=False)
    Publisher = models.CharField(max_length=128, null=False, blank=False)

    def __str__(self):
        return self.FirstName


class Book(models.Model):
    BookIsbn = models.CharField(max_length=10, null=False, blank=False)
    BookName = models.CharField(max_length=128, null=False, blank=False)
    BookPrice = models.PositiveIntegerField(null=False, blank=False)
    BookAuthor = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    BookGenre = models.CharField(max_length=128, null=False, blank=False)
    Publisher = models.CharField(max_length=128, null=False, blank=False)
    PublishedYear = models.PositiveSmallIntegerField()
    CopiesSold = models.PositiveIntegerField()

    def __str__(self):
        return self.BookName