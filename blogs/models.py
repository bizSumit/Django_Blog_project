from django.db import models
from django.urls import reverse

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField('auth.User',on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=55)
    genere = models.CharField(max_length=55)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    blog_text = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.FileField(upload_to="blog_images/",null=True,blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detailed_blog',kwargs={'pk':self.pk})


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment_text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.blog.title}'