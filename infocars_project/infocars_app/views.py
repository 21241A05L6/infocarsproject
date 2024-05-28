from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import csv
import os
def fpage(request):
    return render(request, 'fpage.html')
def home(request):
    return render(request, 'home.html')

def second_page(request):
    if request.method == 'POST':
        option = request.POST.get('option')
        items = None
        if option == '1':
            items = read_csv('table1.csv')
        elif option == '2':
            items = read_csv('table2.csv')
        elif option == '3':
            items = read_csv('table3.csv')
        elif option == '4':
            items = read_csv('table4.csv')
        elif option == '5':
            items = read_csv('table5.csv')    
        return render(request, 'second_page.html', {'items': items})
    else:
        return render(request, 'second_page.html')


def read_csv(filename):
    items = []
    file_path = os.path.join(settings.BASE_DIR, '..', 'csv_files', filename)
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Skip the header row
        for row in reader:
            item = {}
            for i, value in enumerate(row):
                item[headers[i]] = value
            items.append(item)
    return items