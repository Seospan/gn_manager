from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from character_builder_rules.models import CharacterSheetLine

# Create your views here.


def index(request):
    all_sheets_lines = CharacterSheetLine.objects.all()
    template = loader.get_template('character_manager/index.html')
    context = {
        'all_sheets_lines': all_sheets_lines,
    }
    return HttpResponse(template.render(context, request))
