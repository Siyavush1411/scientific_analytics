from django.db import models
from django.utils.translation import gettext_lazy as _

class Institution(models.Model):
    class Meta:
        verbose_name = _('institution')
        verbose_name_plural = _('institutions')

    TYPE_CHOICES = [
        ('university', _('University')),
        ('college', _('College')),
        ('company', _('Company')),
        ('other', _('Other')),
    ]

    name = models.CharField(
        max_length=255,
        verbose_name=_('name')
        )
    
    address = models.CharField(
        max_length=500,
        verbose_name=_('Address')
        )
    
    institution_type = models.CharField(
        max_length=20,
        verbose_name=_('institution type'),
        choices=TYPE_CHOICES
    )
    
    website = models.URLField(
        blank=True,
        verbose_name=_('website'),
        null=True
        )
    
    phone = models.CharField(
        max_length=20,
        verbose_name=_('Phone'),
        blank=True,
        null=True
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created At')
        )
