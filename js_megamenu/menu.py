from cms.models import Placeholder
from menus.base import Modifier
from menus.menu_pool import menu_pool


@menu_pool.register_modifier
class InsertMegaMenu(Modifier):

    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        menu = {}
        if post_cut:
            for placeholder in Placeholder.objects.filter(slot='megamenu', page__publisher_is_draft=False, cmsplugin__id__isnull=False):
                menu[placeholder.page.pk] = placeholder
            for node in nodes:
                if node.id in menu:
                    node.megamenu = menu[node.id]
        return nodes
