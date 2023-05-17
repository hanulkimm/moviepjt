from django.shortcuts import render
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_backend.settings")

django.setup()

from movies.models import Location

import csv, sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname('backend'), '..')))


# Create your views here.

if __name__ == '__main__':
    import csv
    
    f = open('C:/Users/SSAFY/Desktop/movie_location.csv')
    rdr = csv.reader(f)
    title = next(rdr)
    arr = []
    for line in rdr:
        state, city = line[10],line[11]
        if (state, city) not in arr:
            arr.append((state, city))
            Location.objects.create(
                state = state,
                city = city
        )

    