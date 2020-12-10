from django.test import TestCase, Client

# Create your tests here.

class HourlyWeatherTestCase(TestCase):
    def setUp(self):
        pass
    def test_hourly_weather_function_returns_weather_without_city_name(self):
        client = Client()
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("home.html")

