from django.core.paginator import Paginator
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Films, People


def startpage(request):
    return HttpResponse("You are on the hw15 startpage")


@method_decorator(cache_page(60 * 15), name='dispatch')
class PeopleListView(ListView):
    model = People
    ordering = ['id']
    paginate_by = 100


# cashes in urlpatterns
# @method_decorator(cache_page(10), name='dispatch') - returns error
def films_list(request):
    obj = Films.objects.annotate(num=Count('peoplefilmsmanytomany'))

    paginator = Paginator(obj, 500)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'hw15/films_list.html', {'page_obj': page_obj})


class PeopleDetailView(DetailView):
    model = People

    # get all films watched by person
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['films_watched'] = Films.objects.filter(peoplefilmsmanytomany__person__id=self.kwargs['pk'])
        context['num'] = Films.objects.filter(peoplefilmsmanytomany__person__id=self.kwargs['pk']).count()
        return context


class FilmsDetailView(DetailView):
    model = Films

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['people_watched'] = People.objects.filter(peoplefilmsmanytomany__film_id=self.kwargs['pk'])
        return context
