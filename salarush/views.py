from django.utils import timezone
from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views import generic
from django.contrib import messages

from .models import RushBook, RushListModel


def index(request):
    r = RushBook.objects.get(id=1)
    return render(request, 'index.html', {'user': r, })


def add_item(request):
    n = request.POST['list']
    m = request.POST['amount']
    t = request.POST['action']
    book = RushBook.objects.get(id=1)
    if t == "income":
        book.add_list(m, n, True)
    else:
        book.add_list(m, n, False)
    messages.info(request, f"total {book.total_rush()}")
    return HttpResponseRedirect(reverse('salarush:table', args=(1,)))


# def subtract_item(request):
#     book = get_object_or_404(RushBook, pk=1)
#     n = request.POST['list']
#     m = request.POST['amount']
#     book.add_list(m, n, False)
#     return HttpResponseRedirect(reverse('salarush:table', args=(1,)))


class AddView(generic.ListView):
    template_name = 'addTable.html'
    context_object_name = 'rush_list'

    def get_queryset(self):
        return RushListModel.objects.filter(post_date__lte=timezone.now()).order_by('post_date')

    # def get_context_data(self):
    #     context = RushBook.objects.get(pk=1)
    #     return {'user': context, }

