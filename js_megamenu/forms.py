# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from django.utils.text import slugify


MEGAMENU_LAYOUTS = getattr(
    settings,
    'MEGAMENU_LAYOUTS',
    ()
)
MEGAMENU_PANEL_LAYOUTS = getattr(
    settings,
    'MEGAMENU_PANEL_LAYOUTS',
    ()
)
MEGAMENU_SUBMENU_LAYOUTS = getattr(
    settings,
    'MEGAMENU_SUBMENU_LAYOUTS',
    ()
)

MEGAMENU_LAYOUT_CHOICES = MEGAMENU_LAYOUTS
if len(MEGAMENU_LAYOUT_CHOICES) == 0 or len(MEGAMENU_LAYOUT_CHOICES[0]) != 2:
    MEGAMENU_LAYOUT_CHOICES = zip(list(map(lambda s: slugify(s).replace('-', '_'), ('',) + MEGAMENU_LAYOUTS)), ('default',) + MEGAMENU_LAYOUTS)

MEGAMENU_PANEL_LAYOUT_CHOICES = MEGAMENU_PANEL_LAYOUTS
if len(MEGAMENU_PANEL_LAYOUT_CHOICES) == 0 or len(MEGAMENU_PANEL_LAYOUT_CHOICES[0]) != 2:
    MEGAMENU_PANEL_LAYOUT_CHOICES = zip(list(map(lambda s: slugify(s).replace('-', '_'), ('',) + MEGAMENU_PANEL_LAYOUTS)), ('default',) + MEGAMENU_PANEL_LAYOUTS)

MEGAMENU_SUBMENU_LAYOUT_CHOICES = MEGAMENU_SUBMENU_LAYOUTS
if len(MEGAMENU_SUBMENU_LAYOUT_CHOICES) == 0 or len(MEGAMENU_SUBMENU_LAYOUT_CHOICES[0]) != 2:
    MEGAMENU_SUBMENU_LAYOUT_CHOICES = zip(list(map(lambda s: slugify(s).replace('-', '_'), ('',) + MEGAMENU_SUBMENU_LAYOUTS)), ('default',) + MEGAMENU_SUBMENU_LAYOUTS)


class MegamenuForm(forms.ModelForm):

    layout = forms.ChoiceField(choices=MEGAMENU_LAYOUT_CHOICES, required=False)


class MegamenuPanelForm(forms.ModelForm):

    layout = forms.ChoiceField(choices=MEGAMENU_PANEL_LAYOUT_CHOICES, required=False)


class MegamenuSubmenuForm(forms.ModelForm):

    layout = forms.ChoiceField(choices=MEGAMENU_SUBMENU_LAYOUT_CHOICES, required=False)
