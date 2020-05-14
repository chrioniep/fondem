from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Event(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()



    def __str__(self):
        return self.title
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Event, self).save(*args, **kwargs)

    
    def get_absolute_url(self):
        return reverse('website:single-news', kwargs={
            'slug':self.slug
        })
    

    def get_absolute_event_url(self):
        return reverse('dash:update', kwargs={
            'slug':self.slug
        })
    
    def get_absolute_delete_url(self):
        return reverse('dash:delete', kwargs={
            'slug':self.slug
        })

