from django.test import TestCase
from django.test import Client

from .models import Feature,Client
from .forms import FeatureForm


# Create your tests here.
class Setup_Class(TestCase):

    def setUp(self):
        self.client = Client.objects.create(client_name='Test')
        self.feature = Feature.objects.create(title="Blockchain", description="bond-family txn-1", target_date="2018-09-09", product_area='1',feat_priority='10',client= self.client)

class Feature_Form_Test(TestCase):
    # Valid Form Data
    def test_FeatureForm_valid(self):
        client = Client.objects.create(client_name='Test')
        form = FeatureForm(data={'title': "Blockchain", 'description': "bond-family txn-1", 'target_date': '09/09/2018', 'product_area': '1','feat_priority':'16','client':client.id})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_FeatureForm_invalid(self):
        client = Client.objects.create(client_name='Test')
        form = FeatureForm (data={'title': "", 'description': "bond-family txn-1", 'target_date': "09/09/2018", 'product_area': 1,'feat_priority':1,'client':client.id})
        self.assertFalse(form.is_valid())

#When we start testing the vews, first test for the response codes then we got with the actual response.
class Feature_Views_Test(Setup_Class):

    def test_features_list_view(self):
        from django.test import Client
        cl = Client()
        response = cl.get('/features/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "features/feature_list.html")

    def test_add_feature_view(self):
        from django.test import Client
        cl = Client()
        response = cl.get("/features/create/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "features/includes/partial_feature_create.html")

     # Invalid Data
    def test_add_featureReq_invalidform_view(self):
        from django.test import Client
        cl = Client()
        response = cl.post("/features/create/", {'title': "Blockchain", 'description': "bond-family txn-1", 'target_date': "09/09/2018", 'product_area': 1,'feat_priority':1,'client':''})
        self.assertTrue('"form_is_valid": false'.encode() in response.content)

