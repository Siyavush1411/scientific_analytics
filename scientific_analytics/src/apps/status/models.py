from django.db import models
from django.utils.translation import gettext_lazy as _

CATEGORY_CHOICES = [
    ('user', _('User')),
    ('student', _('Student')),
    ('graduate', _('Graduate')),
    ('phd', _('PhD')),
    ('assistant_professor', _('Assistant Professor')),
    ('associate_professor', _('Associate Professor')),
    ('professor', _('Professor')),
    ('emeritus_professor', _('Emeritus Professor')),
    ('researcher', _('Researcher')),
    ('lecturer', _('Lecturer')),
]

class Status(models.Model):
    class Meta:
        verbose_name = _('status')
        verbose_name_plural = _('statuses')
        
    
    status_name = models.CharField(
        verbose_name = _('status name'),
        choices = CATEGORY_CHOICES,
        null = False,
        blank = False,
    )
    
    def __str__(self):
        return self.status_name