from django.db import models
from django.utils.translation import gettext_lazy as _
from common.mixins.TimestampMixins import TimestapmMixin
from apps.category.models import Category

class ScientificWork(TimestapmMixin, models.Model):
    class Meta:
        verbose_name = _('scientific work')
    
    category = models.ForeignKey(
        Category,
        verbose_name=_('category'),
        null=False,
        blank=False,
        on_delete=models.PROTECT
    )
    
    author = models.ManyToManyField(
        'users.User',
        verbose_name=_('author'),
        null=False,
        blank=True,
    )
    
    work_name = models.CharField(
        verbose_name = _('work name'),
        max_length = 255,
        null = False,
        blank = False,
    )
    
    work_rating = models.IntegerField(
        verbose_name = _('work rating'),
        null =True,
        blank=False,
    )
    
    file_path = models.ImageField(
        verbose_name = _('file path'),
        upload_to='uploads/',
    )
    
    uniquenes_score = models.IntegerField(
        verbose_name = _('uniquenes score'),
        null=True,
        blank=False
    )
    

    material_work_id = models.IntegerField(
        verbose_name=_('materia work id')
    )
    language_id = models.IntegerField(verbose_name=_('language ID'), default=1)
    date_publish = models.DateField(verbose_name=_('date published'), auto_now_add=True)
    pub_place_id = models.IntegerField(verbose_name=_('publication place ID'), default=0)
    count = models.IntegerField(verbose_name=_('count'), default=1)
    user_id = models.IntegerField(verbose_name=_('user ID'), default=0)
    date_edit = models.DateTimeField(verbose_name=_('date edited'), auto_now=True)
    date_add = models.DateTimeField(verbose_name=_('date added'), auto_now_add=True)
    kafedra_id = models.IntegerField(verbose_name=_('kafedra ID'), default=0)
    comment = models.TextField(verbose_name=_('comment'), blank=True, null=True, default="")
    user_k = models.IntegerField(verbose_name=_('user K'), default=0)
    user_d = models.IntegerField(verbose_name=_('user D'), default=0)
    conference_name = models.CharField(verbose_name=_('conference name'), max_length=255, blank=True, null=True, default="")
    name_jurnal = models.CharField(verbose_name=_('journal name'), max_length=255, blank=True, null=True, default="")
    url = models.URLField(verbose_name=_('URL'), blank=True, null=True, default="")
    material_direction_id = models.IntegerField(verbose_name=_('material direction ID'), default=0)
    material_direction_dictionary_id = models.IntegerField(verbose_name=_('material direction dictionary ID'), default=0)
    
    
    def __str__(self):
        return str(self.work_name)