from django.shortcuts import render
from books.models import Book


def books_view(request, slug=None):
    template = 'books/books_list.html'
    context = {}
    books_query = Book.objects.all()
    dates = list(books_query)
    unique_dates = []
    for data in dates:
        if str(data.pub_date) not in unique_dates:
            unique_dates.append(str(data.pub_date))
    unique_dates.sort()
    if slug:
        books_query = books_query.filter(pub_date=slug)
        if unique_dates[0] < slug < unique_dates[-1]:
            context['has_previous'] = unique_dates[unique_dates.index(slug)-1]
            context['has_next'] = unique_dates[unique_dates.index(slug)+1]
        elif slug == unique_dates[-1]:
            context['has_previous'] = unique_dates[unique_dates.index(slug) - 1]
        elif slug == unique_dates[0]:
            context['has_next'] = unique_dates[unique_dates.index(slug) + 1]

    context['Books'] = books_query

    return render(request, template, context)
