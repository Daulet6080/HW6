from django.db import models
from django.conf import settings

class HistoricalPeriod(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    categories = models.ManyToManyField(Category, related_name='persons')
    photo = models.ImageField(upload_to='persons_photos/', blank=True, null=True)
    birth_year = models.IntegerField(blank=True, null=True) 
    birth_date = models.DateField(blank=True, null=True)  
    historical_period = models.ForeignKey(HistoricalPeriod, on_delete=models.SET_NULL, null=True, related_name='persons')

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    categories = models.ManyToManyField(Category, related_name='events')
    involved_persons = models.ManyToManyField(Person, related_name='events')
    photo = models.ImageField(upload_to='events_photos/', blank=True, null=True)
    historical_period = models.ForeignKey(HistoricalPeriod, on_delete=models.SET_NULL, null=True, related_name='events')

    def __str__(self):
        return self.title

class Comment(models.Model):
    event = models.ForeignKey(Event, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.event.title}"
