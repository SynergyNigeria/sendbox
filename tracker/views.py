from django.views.generic import ListView
from .models import User_Package_Detail
from django.db.models import Q

# Create your views here.

class SearchClass(ListView):
    model = User_Package_Detail
    template_name = 'dashboard.html'

    # defining quaryset
    def get_queryset(self):
        query = self.request.GET.get('track_id')
        object_list = User_Package_Detail.objects.filter(Q(order_id__iexact=query))
        
        return object_list