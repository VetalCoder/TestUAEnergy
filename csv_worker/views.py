from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import InputCSV

import csv

# Create your views here.


class CSVLoadView(FormView):
    template_name = 'csv_worker/load_csv.html'
    form_class = InputCSV
    success_url = reverse_lazy('csv_worker:view_csv')

    def form_valid(self, form):
        file = form.cleaned_data.get('file')

        dialect = csv.Sniffer().sniff(file.file.getvalue().decode('utf-8'))

        print(dialect)
