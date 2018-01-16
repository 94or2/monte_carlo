from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Member, Group, GroupMemberMap


class IndexView(generic.ListView):
    template_name = 'carlo/index.html'
    context_object_name = 'latest_group_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Group.objects.all()
        # .filter(
        #     pub_date__lte=timezone.now()
        # ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Group
    template_name = 'carlo/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Group.objects.all()  # .filter(pub_date__lte=timezone.now())
