# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

from cms.models import CMSPlugin
from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool

from js_color_picker.fields import RGBColorField
from filer.fields.image import FilerImageField
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

    def __str__(self):
        return self.get_size_display()

    def get_classes(self):
        return 'col-sm-%s' % self.size



class Megamenu(CMSPlugin):
    title = models.CharField(max_length=255, blank=True)
    layout = models.CharField(max_length=255, blank=True)
    attributes = AttributesField(verbose_name='Attributes', blank=True)
    background_color = RGBColorField(
        verbose_name=_('background color'),
        blank=True,
        null=True
    )
    background_image = FilerImageField(
        verbose_name=_('background image'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    def __str__(self):
        return self.title or str(self.pk)



class Panel(CMSPlugin):
    title = models.CharField(max_length=255, blank=True)
    menu_title = models.CharField(verbose_name='Menu title', max_length=255, blank=True)
    layout = models.CharField(max_length=255, blank=True)
    attributes = AttributesField(verbose_name='Attributes', blank=True)
    show_in_menu = models.BooleanField(
        verbose_name=_('show in menu'),
        default=False,
    )
    background_color = RGBColorField(
        verbose_name=_('background color'),
        blank=True,
        null=True
    )
    background_image = FilerImageField(
        verbose_name=_('background image'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    def __str__(self):
        return self.title or str(self.pk)



class Submenu(CMSPlugin):
    title = models.CharField(max_length=255, blank=True)
    menu_title = models.CharField(verbose_name='Menu title', max_length=255, blank=True)
    layout = models.CharField(max_length=255, blank=True)
    attributes = AttributesField(verbose_name='Attributes', blank=True)
    show_in_menu = models.BooleanField(
        verbose_name=_('show in menu'),
        default=False,
    )
    background_color = RGBColorField(
        verbose_name=_('background color'),
        blank=True,
        null=True
    )
    background_image = FilerImageField(
        verbose_name=_('background image'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    def __str__(self):
        return self.title or str(self.pk)

