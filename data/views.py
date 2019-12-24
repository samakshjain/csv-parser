from django.views import generic

from .models import Data


class ListView(generic.list.ListView):
    model = Data
    paginate_by = 50
