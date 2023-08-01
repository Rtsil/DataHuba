from django.shortcuts import render, redirect
from libgen_api import LibgenSearch


# Create your views here.
def index(request):
    return render(request, 'book/index.html')


def search_result(request):
    search_query = request.GET.get('q', '')
    s = LibgenSearch()
    title_filters = {}
    data = s.search_title_filtered(search_query, title_filters, exact_match=True)
    request.session['data'] = data
    return render(request, 'book/search_result.html', {'data': data})


def selected_book(request, book_index):
    data = request.session.get('data', {})
    s = LibgenSearch()
    item = data[book_index]
    download_links = s.resolve_download_links(item)
    keys = list(download_links.keys())
    item["download_link"] = download_links[keys[0]]

    return redirect(item["download_link"])
