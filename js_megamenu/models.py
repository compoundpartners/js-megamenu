from django.db import models
from cms.models import CMSPlugin


class Section(CMSPlugin):
    SIZE_CHOICES = (
        ('2', '1/6'),
        ('3', '1/4'),
        ('4', '1/3'),
        ('6', '1/2'),
    )
    size = models.CharField(max_length=1, choices=SIZE_CHOICES, default='2')
    title = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.get_size_display()

    def get_classes(self):
        return 'col-sm-%s' % self.size
