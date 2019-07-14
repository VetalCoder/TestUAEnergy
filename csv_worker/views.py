from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

from .forms import InputCSV
from . import dbhelper
import json
from io import StringIO
import random
import collections
import csv

# Create your views here.


class CSVLoadView(FormView):
    template_name = 'csv_worker/load_csv.html'
    form_class = InputCSV

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('authorization:login')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        file = self.request.FILES['file']
        csv_raw = StringIO(file.read().decode("utf-8"))

        reader = csv.DictReader(csv_raw)

        result_dict = {}
        for row in reader:
            name_var = row.popitem(last=False)[1]
            result_dict[name_var] = json.dumps(row)

        dbhelper.create_table_with_data(**result_dict)
        return redirect('csv_worker:view_csv')


class ShowTablesView(TemplateView):
    template_name = 'csv_worker/tables.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('authorization:login')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            for index, (name, data) in enumerate(dbhelper.get_data().items(), 1):
                context[f'table{index}_name'] = name
                context[f'table{index}_data'] = data
        except dbhelper.TableDoesNotExists:
            context['table_does_not_exists'] = 'No one CSV file loaded before...'

        context['table3_name'] = 'Random unique symbols'
        unique_symbols = list(map(chr, random.sample(range(0xd7ff), 16)))  # to 0x10ffff, if needed
        context['table3_data'] = collections.OrderedDict(
            [(f'Sym {index}', value) for index, value in zip(range(1, 17), unique_symbols)]
        )
        return context
