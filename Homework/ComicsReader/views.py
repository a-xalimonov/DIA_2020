from django.shortcuts import get_object_or_404, render

from .models import Comic, Page


def comics(request):
    return render(request, "ComicsReader/comics.html", {"comics_list": Comic.objects.order_by('-publication_date')})


def read(request, comic_id):
    comic_object = get_object_or_404(Comic, pk=comic_id)
    return render(request, "ComicsReader/read.html", {
        "comic": comic_object,
        "page_list": comic_object.page_set.order_by('number'),
        })