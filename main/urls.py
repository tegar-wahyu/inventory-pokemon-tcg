from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('add_item', add_item, name='add_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('change_item_amount/<int:item_id>/<str:amount>/', change_item_amount, name='change_item_amount'),
    path('delete_item/<int:item_id>/', delete_item, name='delete_item'),
]