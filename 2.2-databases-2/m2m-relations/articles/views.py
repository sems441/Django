from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    context = {}

    ordering = '-published_at'
    query = Article.objects.all().prefetch_related('scopes__tag').order_by(ordering)

    context["object_list"] = query

    return render(request, template, context)
