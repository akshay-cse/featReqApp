from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Feature,Client
from django.http import JsonResponse,HttpResponse
from django.template.loader import render_to_string
from .forms import FeatureForm

import logging
logging.basicConfig(level=logging.DEBUG)
logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
logger = logging.getLogger(__name__)

fileHandler = logging.FileHandler("{0}/{1}.log".format('./../featReqApp/', 'feature'))
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)



#logger.setLevel(logging.WARNING)

# just fetching list of features list already present in db
def feature_list(request):
    try:
        #Info level msg
        logger.info('Fetching feature request list')
        features = Feature.objects.all().order_by('-client', '-feat_priority')
        logger.info('Returning response: %s', features)
        return render(request, 'features/feature_list.html', {'feature_list': features})
    except Exception as err:
        logger.error('Failed to get the feature list', exc_info=True)
        return HttpResponse(err) 

# we are not rendering a template but returning a Json response.
# Now we refactor the feature_create view to reuse its code in the feature_update view:
def feature_create(request):
    logger.info('Create feature request')
    try:
        logger.info('Starting request %s', request)
        data = dict()
        if request.method == 'POST':
            logger.info('Request type is POST; While Saving data')
            form = FeatureForm(request.POST)
        else:
            logger.info('Request type is GET')
            form = FeatureForm()
            #clients = Client.objects.all() 
        return save_feature_form(request, form, 'features/includes/partial_feature_create.html')
    except Exception as err:
        logger.error('Failed to create the feature request', exc_info=True)
        return HttpResponse(err)     

def save_feature_form(request, form, template_name):
    try:
        logger.info('Starting request %s', request)
        data = dict()
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                data['form_is_valid'] = True
                #again sort here
                features = Feature.objects.all().order_by('-client', '-feat_priority')
                data['html_feature_list'] = render_to_string('features/includes/partial_feature_list.html', {
                    'feature_list': features
                })
            else:
                data['form_is_valid'] = False
        context = {'form': form}
        data['html_form'] = render_to_string(template_name, context, request=request)
        logger.info('Returning response: %s', JsonResponse(data))
        return JsonResponse(data)
    except Exception as err:
        logger.error('Failed to save form data', exc_info=True)
        return HttpResponse(err)    


def create_client(request):
    logger.info('Creating Client')
    try:
        logger.info('Starting request %s', request)
        if 'client' in request.GET:
            client_name = request.GET['client']
            #Client.objects.create(name=client_name)
            Client.objects.create(client_name=client_name)
            message = 'You created client : %r' % request.GET['client']
            logger.info('Returning response: %s', message) 
            return HttpResponse(message)
    except Exception as err:
        logger.error('Failed to create client', exc_info=True)
        return HttpResponse(err)

def feature_update(request, pk):
    logger.info('Update feature request')
    try:
        logger.info('Starting request %s', request)
        feature = get_object_or_404(Feature, pk=pk)
        if request.method == 'POST':
            form = FeatureForm(request.POST, instance=feature)
        else:
            form = FeatureForm(instance=feature)
        logger.info('Returning response: %s', JsonResponse(data))     
        return save_feature_form(request, form, 'features/includes/partial_feature_update.html')
    except Exception as err:
        return HttpResponse(err)

def feature_delete(request, pk):
    logger.info('Delete feature request')
    try:
        logger.info('Starting request %s', request)
        feature = get_object_or_404(Feature, pk=pk)
        data = dict()
        if request.method == 'POST':
            feature.delete()
            data['form_is_valid'] = True  # This is just to play along with the existing code
            features = Feature.objects.all()
            data['html_feature_list'] = render_to_string('features/includes/partial_feature_list.html', {
                'feature_list': features
            })
        else:
            context = {'feature': feature}
            data['html_form'] = render_to_string('features/includes/partial_feature_delete.html',
                context,
                request=request,
            )
        logger.info('Returning response: %s', JsonResponse(data))    
        return JsonResponse(data)
    except Exception as err:
        logger.error('Failed to delete feature', exc_info=True)
        return HttpResponse(err)