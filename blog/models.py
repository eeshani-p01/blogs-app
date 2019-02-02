from django.db import models
from django.utils import timezone   #for getting the time at post added
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)    #now is fn bt we are not calling(now()) it here
    author = models.ForeignKey(User, on_delete=models.CASCADE)    #to get user who added post, will import it from another table, will do by foreign key
    # on-delete attr we are instructing what to do when the user who created is deleted
    # here we are going to delete the user's post

    def __str__(self):
        return self.title       # dunder str method