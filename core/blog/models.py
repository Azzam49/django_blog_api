from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


#foreign key has PROTECT that means when the category
#gets deleted , its post won't get deleted
class Post(models.Model):

    # django uses managers to interface between model and
    #the database, now instead of using only the default
    # Post.objects. to return data we could use PostObjects
    #which will return the specfic filters we applied to it,
    #in our case is .filter(status='published')
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT,default=1
    )
    title = models.CharField(max_length=100)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    #unqiue_for_date='published' , this will tell django to now
    #allow 2 records have the same slug value and same date of published field
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts'
    )
    status = models.CharField(
        max_length=10, choices=options, default='published'
    )



    #STOPPED AT:
    #https://www.youtube.com/watch?v=soxd_xdHR0o
    #MINT 46