from django.shortcuts import render
from django.views import generic
from .models import Item, MEAL_TYPE


# creates a view for the main page
# MenuList class is used to display pages that has lots of lists of data
class MenuList(generic.ListView):
    # queryset variable is used to store list of data from the Item
    queryset = Item.objects.order_by('-date_created')
    # here the view in connected to the HTML page and to the model.
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # super --> calls the parent class ListView
        context = super().get_context_data(**kwargs)
        context['meals'] = MEAL_TYPE
        return context




# Creates a view for the details of each menu
class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = 'menu_item_details.html'
