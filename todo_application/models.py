from django.db import models


# Create your models here.

class ToDo(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=1000)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "ToDo"
        verbose_name_plural = "ToDo"


class SubTasks(models.Model):
    title = models.CharField(max_length=100, null=False)
    completed = models.BooleanField(default=False)
    todo = models.ForeignKey(ToDo, on_delete=models.CASCADE, related_name="subtasks")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "SubTask"
        verbose_name_plural = "SubTasks"
