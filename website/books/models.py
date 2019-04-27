from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50) 
    website = models.URLField()
    
    def __str__(self):
        return self.name

    class Admin:
        pass

class Author(models.Model):
    salutation = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='tmp')   # 这个路径应该是相对路径，不应该是'/temp',和django1* 还是有区别的
    
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
    class Admin:
        pass

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)  # 此处也是和django1*不一样的地方
    publication_date = models.DateField()
    
    def __str__(self):
        return self.title

    class Admin:
        list_display = ('title', 'publisher', 'publication_date')
        list_filter = ('publisher', 'publication_date')
        ordering = ('-publication_date',)
        search_fields = ('title',)