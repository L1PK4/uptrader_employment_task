from django import template
from item.models import Item


register = template.Library()

@register.inclusion_tag('item.html', takes_context=True)
def draw_menu(context, name):
    url = context['request'].path
    print(context)
    path_to_root = list(Item.objects.get(url=url).get_path_to_root())
    print(path_to_root)
    if path_to_root[-1].id != Item.objects.get(name=name).id:
        return {'current': False}
    temp_item = path_to_root.pop()
    path_dict = {temp_item: {}}
    current_item = path_dict[temp_item]
    while path_to_root:
        children = temp_item.get_children()
        for child in children:
            current_item[child] = {}
        temp_item = path_to_root.pop()
        try:
            current_item = current_item[temp_item]
        except KeyError:
            break
    local_context = {
        'current': True,
        'path_from_item': path_dict
    }
    print(local_context)
    return local_context