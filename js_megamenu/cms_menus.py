from django.core.cache import cache
from cms.models import Placeholder
from menus.base import Modifier
from menus.menu_pool import menu_pool

@menu_pool.register_modifier
class InsertMegaMenu(Modifier):

    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        if post_cut:
            menu = cache.get('mega-menu-dict', {})
            if not menu:
                for placeholder in Placeholder.objects.filter(slot='megamenu', cmsplugin__id__isnull=False).distinct():
                    menu[placeholder.page.id] = placeholder
                cache.set('mega-menu-dict', menu)
            for node in nodes:
                if node.id in menu:
                    node.megamenu = menu[node.id]
        return nodes
