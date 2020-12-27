from django.db import models

class movie(models.Model):

    title = models.CharField('Название фильма', max_length=50)

    def __str__(self):
        return self.title

class detail(models.Model):

    movie_link = models.ForeignKey(movie, on_delete=models.CASCADE)
    image_url = models.URLField('Обложка фильма')
    year = models.CharField('Дата выхода', max_length=21)
    desc = models.CharField('Описание', max_length=500)

    def __str__(self):
        return self.desc
