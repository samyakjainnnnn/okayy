from django.db import models


class Pages(models.Model):
    '''Creates a table to support Pages'''

    title = models.CharField(max_length=255)
    price_dollar = models.IntegerField()
    price_rupee = models.IntegerField()
    intro = models.TextField(default=None)
    video_intro = models.TextField(default=None)
    roadmap = models.TextField(default=None)
    video_url = models.CharField(max_length=255, default=None)
    image_url = models.CharField(max_length=255, default=None)

    class Meta():
        '''Meta class to add functionalities'''
        verbose_name = 'page'
        verbose_name_plural = 'pages'

    def __str__(self):
        return f"{self.title}"
