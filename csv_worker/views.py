from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from .forms import InputCSV
from . import dbhelper
import json
from io import StringIO

import csv

# Create your views here.


class CSVLoadView(FormView):
    template_name = 'csv_worker/load_csv.html'
    form_class = InputCSV

    def form_valid(self, form):
        file = self.request.FILES['file']
        csv_raw = StringIO(file.read().decode("utf-8"))

        reader = csv.DictReader(csv_raw)

        result_dict = {}
        for row in reader:
            name_var = row.popitem(last=False)[1]
            result_dict[name_var] = json.dumps(row)

        print(result_dict)
        dbhelper.create_table_with_data(**result_dict)
        return redirect('csv_worker:view_csv')


class ShowTablesView(TemplateView):
    template_name = 'csv_worker/tables.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
