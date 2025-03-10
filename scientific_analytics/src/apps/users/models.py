from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from apps.status.models import Status


class User(AbstractUser):
       
    first_name = models.CharField(
        verbose_name=_('first name'),
        max_length=255,
        null=False,
        blank=False,        
    )
    
    last_name = models.CharField(
        verbose_name=_('last name'),
        max_length=255,
        null=False,
        blank=False,
    )
    
    patronymic = models.CharField(
        verbose_name=_('patronymic'),
        max_length=255,
        null=False,
        blank=False,
    )

    rating = models.IntegerField(
        verbose_name=_('rating'),
        null=False,
        blank=True,
        default=0
    )
    
    scientific_work = models.ManyToManyField(
        'scientific_work.ScientificWork',
        verbose_name=_('scientific work'),
        blank=False,
        related_name='users_scientific_works'
    )
    
    status = models.ForeignKey(
        Status,
        verbose_name=_('status'),      
        null=True,
        blank=False,
        on_delete=models.PROTECT,
    )
    
    institution = models.ForeignKey(
        to='institution.Institution',
        verbose_name=_('status'),      
        null=True,
        blank=True,
        on_delete=models.PROTECT,
    )
    
    avatar = models.ImageField(
        verbose_name=_('avatar'),
        upload_to='avatars/',
        null=True,
        blank=True
    )
    
    def __str__(self):
        return self.username