from django.utils.translation import ugettext_lazy as _
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from .models import Section


@plugin_pool.register_plugin
class MegamenuSectionPlugin(CMSPluginBase):
    model = Section
    name = _('Megamenu: Section')
    render_template = 'megamenu/section.html'
    admin_preview = False
    allow_children = True
    child_classes = ['TextPlugin', 'Bootstrap4CtaPlugin', 'JSLinkListPlugin',]

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context
