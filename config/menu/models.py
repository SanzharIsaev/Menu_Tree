from audioop import reverse
from django.db import models


class Menu(models.Model):
    
    name = models.CharField(
        'Название меню', 
        max_length=50, 
        unique=True
        )
    
    description = models.TextField(
        'Описание', 
        max_length=300, 
        blank=True
    )
    
    url = models.SlugField(
        max_length=100,
        unique=True
    )
    
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        verbose_name='Родитель',
        null=True,
        blank=True,
        related_name='tags'
    )

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name