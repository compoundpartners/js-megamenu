# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _

from cms.models import CMSPlugin
from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool

from djangocms_attributes_field.fields import AttributesField


class MegamenuExtension(PageExtension):
    show_megamenu = models.BooleanField(_('Show Megamenu Placeholder'), null=False, default=False)

extension_pool.register(MegamenuExtension)


class Section(CMSPlugin):
    SIZE_CHOICES = (
        ('2', '1/6'),
        ('3', '1/4'),
        ('4', '1/3'),
        ('6', '1/2'),
        ('8', '2/3'),
    )
    size = models.CharField(max_length=1, choices=SIZE_CHOICES, default='2')
    title = models.CharField(max_length=255, blank=True)
    attributes = AttributesField(verbose_name='Attributes', blank=True)

    def __unicode__(self):
        return self.get_size_display()

    def get_classes(self):
        return 'col-sm-%s' % self.size
