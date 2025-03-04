from django.views.generic import ListView
from .models import Table

class TableListView(ListView):
    model = Table
    template_name = "tables/table_list.html"
