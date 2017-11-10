from django.test import TestCase


class HomeTest(TestCase):
    #def SetUp(self):
     #   self.response = self.client.get('/')

    def test_get(self):
        """Return status 200"""
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)

    def test_template(self):
        """Must use index.html"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')



#def test_dolar(self):
#    """Mostra a cotacao do dolar"""
#    self.assertContains(self.response, 'R$ 3,50')
