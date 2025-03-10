from django.db import models
from django.utils.translation import gettext_lazy as _
from common.mixins.TimestampMixins import TimestapmMixin
from apps.category.models import Category

class ScientificWork(TimestapmMixin, models.Model):
    class Meta:
        verbose_name = _('scientyfic work')
    
    category = models.ForeignKey(
        Category,
        verbose_name=_('category'),
        null=False,
        blank=False,
        on_delete=models.PROTECT
    )
    
    author = models.ForeignKey(
        'users.User',
        verbose_name=_('author'),
        null=False,
        blank=True,
        on_delete=models.PROTECT,
    )
    
    work_name = models.CharField(
        verbose_name=_('work name'),
        max_length=255,
        null=False,
        blank=False,
    )
    
    work_rating = models.IntegerField(
        verbose_name=_('work rating'),
        null=False,
        blank=False,
    )
    
    uniquenes_score = models.IntegerField(
        verbose_name=_('uniquenes score'),
        null=False,
        blank=False
    )
    
    def __str__(self):
        return str(self.work_name)