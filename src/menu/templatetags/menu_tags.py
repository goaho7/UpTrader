from django import template
from django.urls import resolve
from menu.models import Menu

register = template.Library()

@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    menu_items = Menu.objects.filter(menu_name=menu_name).select_related('parent')

    def build_menu_tree(items, parent=None):
        tree = []
        for item in items:
            if item.parent == parent:
                children = build_menu_tree(items, item)
                tree.append({'item': item, 'children': children, 'active': item.get_url() == request.path_info or any(c['active'] for c in children)})
        return tree

    menu_tree = build_menu_tree(menu_items)
    return {'menu_tree': menu_tree}
