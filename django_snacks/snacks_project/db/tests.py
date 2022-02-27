from django.test import SimpleTestCase
from django.urls import reverse

class DbTests(SimpleTestCase):
  def test_home_page_status_code(self):
    url = reverse('db_home')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_home_base_template(self):
    url = reverse('db_home')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'db_home.html')
    self.assertTemplateUsed(response, 'db_base.html')

  def test_humans_page_status_code(self):
    url = reverse('humans')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_humans_base_template(self):
    url = reverse('humans')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'humans.html')
    self.assertTemplateUsed(response, 'db_base.html')

  def test_bulma_page_status_code(self):
    url = reverse('bulma')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_bulma_base_template(self):
    url = reverse('bulma')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'bulma.html')
    self.assertTemplateUsed(response, 'humans.html')

  def test_chichi_page_status_code(self):
    url = reverse('chichi')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_chichi_base_template(self):
    url = reverse('chichi')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'chichi.html')
    self.assertTemplateUsed(response, 'humans.html')

  def test_krillin_page_status_code(self):
    url = reverse('krillin')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_krillin_base_template(self):
    url = reverse('krillin')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'krillin.html')
    self.assertTemplateUsed(response, 'humans.html')

  def test_roshi_page_status_code(self):
    url = reverse('roshi')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_roshi_base_template(self):
    url = reverse('roshi')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'roshi.html')
    self.assertTemplateUsed(response, 'humans.html')

  def test_tien_page_status_code(self):
    url = reverse('tien')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_tien_base_template(self):
    url = reverse('tien')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'tien.html')
    self.assertTemplateUsed(response, 'humans.html')

  def test_yamcha_page_status_code(self):
    url = reverse('yamcha')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_yamcha_base_template(self):
    url = reverse('yamcha')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'yamcha.html')
    self.assertTemplateUsed(response, 'humans.html')

  def test_saiyans_page_status_code(self):
    url = reverse('saiyans')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_saiyans_base_template(self):
    url = reverse('saiyans')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'saiyans.html')
    self.assertTemplateUsed(response, 'db_base.html')

  def test_gohan_page_status_code(self):
    url = reverse('gohan')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_gohan_base_template(self):
    url = reverse('gohan')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'gohan.html')
    self.assertTemplateUsed(response, 'saiyans.html')

  def test_goku_page_status_code(self):
    url = reverse('goku')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_goku_base_template(self):
    url = reverse('goku')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'goku.html')
    self.assertTemplateUsed(response, 'saiyans.html')

  def test_vegeta_page_status_code(self):
    url = reverse('vegeta')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_vegeta_base_template(self):
    url = reverse('vegeta')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'vegeta.html')
    self.assertTemplateUsed(response, 'saiyans.html')
