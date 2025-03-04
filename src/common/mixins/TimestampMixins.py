from django.db import models
from django.utils.translation import gettext_lazy as _

class TimestapmMixin():    
    created_at = models.DateField(
        verbose_name=_('create_at'),
        null=False,
        blank=False,
        auto_now_add=True
    )
    
    update_at = models.DateField(
        verbose_name=_('update_at'),
        null=False,
        blank=False,
        auto_now_add=True,
    )