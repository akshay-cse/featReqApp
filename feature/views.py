from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Feature,Client
from django.http import JsonResponse,HttpResponse
from django.template.loader import render_to_string
from .forms import FeatureForm

# just fetching list of features list already present in db
def feature_list(request):
    features = Feature.objects.all()
    return render(request, 'features/feature_list.html', {'feature_list': features})

# we are not rendering a template but returning a Json response.
# Now we refactor the feature_create view to reuse its code in the feature_update view:
def feature_create(request):
    data = dict()
    if request.method == 'POST':
        form = FeatureForm(request.POST)
    else:
        form = FeatureForm()
    clients = Client.objects.all() 
    return save_feature_form(request, form,clients, 'features/includes/partial_feature_create.html')


def save_feature_form(request, form, clients, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            features = Feature.objects.all()
            data['html_feature_list'] = render_to_string('features/includes/partial_feature_list.html', {
                'feature_list': features
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form,'clients':clients}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)



def create_client(request):
     if 'client' in request.GET:
        client_name = request.GET['client']
        #Client.objects.create(name=client_name)
        Client.objects.create(client_name=client_name)
        message = 'You created client : %r' % request.GET['client']
        return HttpResponse(message)

def feature_update(request, pk):
    feature = get_object_or_404(Feature, pk=pk)
    if request.method == 'POST':
        form = FeatureForm(request.POST, instance=feature)
    else:
        form = FeatureForm(instance=feature)
    return save_feature_form(request, form, 'features/includes/partial_feature_update.html')


def feature_delete(request, pk):
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
    return JsonResponse(data)