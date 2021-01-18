from django.db import models

class Comic(models.Model):
    title = models.CharField('Название', max_length=255)
    codename = models.CharField('Кодовое название', max_length=255, unique=True)
    publication_date = models.DateField('Дата публикации')
    previous_issue = models.OneToOneField('self', related_name="+", on_delete=models.SET_NULL, null=True, blank=True, default=None)
    next_issue = models.OneToOneField('self', related_name="+", on_delete=models.SET_NULL, null=True, blank=True, default=None)

    def __str__(self):
        return self.title


class Page(models.Model):
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    image = models.CharField('Изображение', max_length=255)
    label = models.CharField('Подпись', max_length=255)
    number = models.IntegerField('Номер страницы')
    
    def __str__(self):
        return self.comic.title + ", p." + str(self.number)