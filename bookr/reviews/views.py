from django.shortcuts import render


def index(request):
    name = "World!"
    return render(request, "base.html", {"name": name})


def szukanie(request):
    szukana = request.GET.get("szukana")
    context = {"szukana": szukana}
    return render(request, "book-search.html", context)
