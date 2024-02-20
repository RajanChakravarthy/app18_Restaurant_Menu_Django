from django.shortcuts import render
from django.views import generic
from .models import Item


# creates a view for the main page
# MenuList class is used to display pages that has lots of lists of data
class MenuList(generic.ListView):
    # queryset variable is used to store list of data from the Item
    queryset = Item.objects.order_by('-date_created')
    # here the view in connected to the HTML page and to the model.
    template_name = 'index.html'




# Creates a view for the details of each menu
class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = 'menu_item_details.html'
