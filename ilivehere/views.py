from django.views.generic import CreateView, DetailView

from .forms import StoryForm
from .models import Story


class StoryCreateView(CreateView):
    model = Story
    form_class = StoryForm


class StoryDetailView(DetailView):
    model = Story