from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    # media = models.ImageField(upload_to="static/api/posts/images/",blank=True, null=True)
    # poster = models.ForeignField() requires further tweaking

    class Meta:
        ordering = ['-created']