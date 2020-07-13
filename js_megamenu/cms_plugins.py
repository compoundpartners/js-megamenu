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
