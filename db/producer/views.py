from wq.db.rest.views import ModelViewSet
from django.db.models.query import EmptyQuerySet
from .models import Producer


class ProducerViewSet(ModelViewSet):

    # this appends data to /producers.json but not to /producers/1.json...
    def list(self, request, *args, **kwargs):
        response = super(ProducerViewSet, self).list(request, *args, **kwargs)

        for i in range(0, len(response.data['list'])):
            if response.data['list'][i]['category_label'] == "Dairy products" or response.data['list'][i]['category_label'] == "Lactate":
                response.data['list'][i]['category_dairy_products'] = True
            elif response.data['list'][i]['category_label'] == "Fruits" or response.data['list'][i]['category_label'] == "Fructe":
                response.data['list'][i]['category_fruits'] = True
            elif response.data['list'][i]['category_label'] == "Vegetables" or response.data['list'][i]['category_label'] == "Legume":
                response.data['list'][i]['category_vegetables'] = True
            elif response.data['list'][i]['category_label'] == "Meat" or response.data['list'][i]['category_label'] == "Carne":
                response.data['list'][i]['category_meat'] = True
            elif response.data['list'][i]['category_label'] == "Fish" or response.data['list'][i]['category_label'] == "Peste":
                response.data['list'][i]['category_fish'] = True
            elif response.data['list'][i]['category_label'] == "Bakery products" or response.data['list'][i]['category_label'] == "Produse panificatie":
                response.data['list'][i]['category_bakery_products'] = True
            elif response.data['list'][i]['category_label'] == "Honey" or response.data['list'][i]['category_label'] == "Miere":
                response.data['list'][i]['category_honey'] = True
            else:
                response.data['list'][i]['category_none'] = True

        return response

    # This could be called to get querysets also for single producers (/producers/1.json) and manipulate them.
    # However, the method is not intended for manipulation of querysets.
    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     # add code for adding flags (category_fruits,...) to producer querysets
    #     return qs