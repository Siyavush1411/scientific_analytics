from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    class Meta:
        verbose_name=_('category')
        
    WORK_CATEGORY_CHOICES = [
        ('computer_science', _('Computer Science')),
        ('mathematics', _('Mathematics')),
        ('physics', _('Physics')),
        ('biology', _('Biology')),
        ('chemistry', _('Chemistry')),
        ('engineering', _('Engineering')),
        ('medicine', _('Medicine')),
        ('psychology', _('Psychology')),
        ('sociology', _('Sociology')),
        ('literature', _('Literature')),
        ('history', _('History')),
        ('philosophy', _('Philosophy')),
        ('art', _('Art')),
        ('economics', _('Economics')),
        ('law', _('Law')),
        ('education', _('Education')),
        ('linguistics', _('Linguistics')),
    ]

    
    category_name = models.CharField(
        verbose_name=_('status name'),
        choices=WORK_CATEGORY_CHOICES,
        null=False,
        blank=False        
    )