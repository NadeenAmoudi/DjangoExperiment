from django.db import models

class Chapter(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    chapterNum = models.IntegerField()
    pageNum = models.IntegerField()

    # def get_absolute_url(self):
    #     return reverse('chapter_edit', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name