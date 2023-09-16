from django.urls import path
from main.views import homepage, add_item, clear_items, show_xml, show_json, show_xml_by_id, show_json_by_id 

app_name = 'main'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('add_item', add_item, name='add_item'),
    path('clear_items', clear_items, name='clear_items'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
]