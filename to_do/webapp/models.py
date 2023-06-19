from django.db import models

# Create your models here.
status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]
class List(models.Model):

    description = models.TextField(max_length=2000, null=False, blank=False)
    status = models.CharField(max_length=100, null=False, blank=False, choices=status_choices)
    date = models.DateField(verbose_name="Дата выполнения")



    def __str__(self):
        return f"{self.pk} {self.description}: {self.status}"

