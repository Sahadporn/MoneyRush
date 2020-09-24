from django.utils import timezone
from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect
from django.views import generic

from .models import RushBook, RushListModel


def index(request):
    r = RushBook.objects.get(id=1)
    return render(request, 'index.html', {'user': r, })


def add_item(request):
    n = request.POST['list']
    m = request.POST['amount']
    book = RushBook.objects.get(id=1)
    book.add_list(m, n, True)
    return HttpResponseRedirect(reverse('salarush:table', args=(1,)))


class AddView(generic.ListView):
    template_name = 'addTable.html'
    context_object_name = 'rush_list'

    def get_queryset(self):
        return RushListModel.objects.filter(post_date__lte=timezone.now()).order_by('-post_date')
