from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from common.mixins.TimestampMixins import TimestapmMixin
from apps.status.models import Status


class User(AbstractUser, TimestapmMixin):
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
        null=True,
        blank=False,
    )

    rating = models.IntegerField(
        verbose_name=_('rating'),
        null=False,
        blank=True,
        default=0
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
    
    degree = models.CharField(
        verbose_name=_('degree'),
        max_length=80,
    )
    
    material_user_id = models.CharField(
        verbose_name=_('material user id')
    )
    
    def __str__(self):
        return self.username