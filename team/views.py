from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Project, Member, TimeStamp


class OverView(generic.TemplateView):
    template_name = 'team/overview.html'

    def get_context_data(self, **kwargs):
        context = super(OverView, self).get_context_data(**kwargs)
        context['project_list'] = Project.objects.all()
        context['member_list'] = Member.objects.all()
        context['timestamp'] = TimeStamp.objects.all()
        return context
