import random
import short_url
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, RedirectView
from .models import Link
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404


# Create your views here.
class LinkList(ListView):
    model = Link
    template_name = 'link_list.html'
    paginate_by = 50
    queryset = Link.objects.all().order_by('-id')


class CreateLink(CreateView):
    model = Link
    fields = ['completelink']
    template_name = 'add_link.html'

    def form_valid(self, form):
        rand = random.randint(100, 999999999)
        if Link.objects.filter(slug=short_url.encode_url(rand)).exists():
            raise ValidationError('A Short Link with this value already exists.')
        self.object = form.save(commit=False)
        self.object.slug = short_url.encode_url(rand)
        return super(CreateLink, self).form_valid(form)

    def get_success_url(self):
        return reverse('link_detail', args=(self.object.slug,))


class LinkDetail(DetailView):
    model = Link
    template_name = 'link_detail.html'


class Redirect(RedirectView):

    def get(self, request, *args, **kwargs):
        self.url = get_object_or_404(Link, slug=kwargs['slug']).completelink
        return super(Redirect, self).get(request, *args, **kwargs)
