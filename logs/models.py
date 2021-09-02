from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    created_on = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Log(models.Model):
    timestamp = models.DateTimeField()

    # todo: replace with TextField if necessary
    message = models.CharField(max_length=1000)

    category = models.ForeignKey(
        Category,
        related_name='logs',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )

    class Meta:
        verbose_name = 'log'
        verbose_name_plural = 'logs'
        ordering = ['-timestamp']

    def __str__(self):
        return self.message
