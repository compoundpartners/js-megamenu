from django.template import TemplateDoesNotExist
from django.template.loader import select_template
from django.utils.translation import ugettext_lazy as _
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from . import models, forms


@plugin_pool.register_plugin
class MegamenuSectionPlugin(CMSPluginBase):
    model = models.Section
    name = _('Megamenu: Section')
    render_template = 'megamenu/section.html'
    admin_preview = False
    allow_children = True
    child_classes = [
        'TextPlugin',
        'Bootstrap4BoxoutPlugin',
        'JSLinkListPlugin',
        'Bootstrap4CollapsePlugin',
        'Bootstrap4LinkPlugin',
        'PromoUnitPlugin',
        'Bootstrap4PicturePlugin',
    ]

    def render(self, context, instance, placeholder):
        classes = [
            instance.get_classes(),
            instance.attributes.get('class'),
        ]
        classes = ' '.join(_class for _class in classes if _class)
        instance.attributes['class'] = classes
        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context


class LayoutMixin():

    def get_layout(self, context, instance, placeholder):
        return instance.layout

    def get_render_template(self, context, instance, placeholder):
        layout = self.get_layout(context, instance, placeholder)
        if layout:
            template = self.TEMPLATE_NAME % layout
            try:
                select_template([template])
                return template
            except TemplateDoesNotExist:
                pass
        return self.render_template

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context

@plugin_pool.register_plugin
class MegamenuPlugin(LayoutMixin, CMSPluginBase):
    model = models.Megamenu
    form = forms.MegamenuForm
    name = _('Megamenu')
    render_template = 'megamenu/megamenu.html'
    TEMPLATE_NAME = 'megamenu/megamenu_%s.html'
    module = _('Megamenu')
    admin_preview = False
    allow_children = True
    child_classes = [
        'MegamenuPanelPlugin',
        'MegamenuSubmenuPlugin',
        'Bootstrap4LinkPlugin',
    ]
    exclude = ['attributes']

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context


@plugin_pool.register_plugin
class MegamenuPanelPlugin(LayoutMixin, CMSPluginBase):
    model = models.Panel
    form = forms.MegamenuPanelForm
    name = _('Panel')
    render_template = 'megamenu/panel.html'
    TEMPLATE_NAME = 'megamenu/panel_%s.html'
    module = _('Megamenu')
    admin_preview = False
    allow_children = True
    parent_classes = ['MegamenuPlugin', 'MegamenuSubmenuPlugin']

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context


@plugin_pool.register_plugin
class MegamenuSubmenuPlugin(LayoutMixin, CMSPluginBase):
    model = models.Submenu
    form = forms.MegamenuSubmenuForm
    name = _('Submenu')
    render_template = 'megamenu/submenu.html'
    TEMPLATE_NAME = 'megamenu/submenu_%s.html'
    module = _('Megamenu')
    admin_preview = False
    allow_children = True
    parent_classes = ['MegamenuPlugin']
    child_classes = [
        'MegamenuPanelPlugin', 'Bootstrap4LinkPlugin'
    ]

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context
