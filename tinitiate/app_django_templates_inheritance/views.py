from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.http import HttpResponse

# Template Blocks
def template_blocks(request):

    # Create Template Object
    template = loader.get_template('template-blocks.html')

    # Data to be passed to the template
    context = {
        'l_blue_data': 'This is BLUE Data',
        'l_green_data': 'This is GREEN Data',
        'l_red_data': 'This is RED data',
    }

    return HttpResponse(template.render(context, request))
# END