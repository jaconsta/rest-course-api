import json
from django.test import TestCase

JSON_TYPE = 'application/json'


class MyFirstCase(TestCase):

    @staticmethod
    def decode_response(response):
        return json.loads(response.content.decode('utf-8'))

    def test_case_demonstration(self):
        """
        As a dummy test. It is not testing our application
        """
        my_operation = True
        self.assertEqual(my_operation, True)

    def test_get_images(self):
        """
        b'[{"file": "white.png", "name": "first"}, {"file": "one.png", "name": "second"}]'

        :return:
        """
        expected = [
            {
                'name': 'first',
                'file': 'white.png'
            }, {
                'name': 'second',
                'file': 'one.png'
            }
        ]
        response = self.client.get('/api/v_0/images/')
        response_body = self.decode_response(response)
        print(response.content)
        self.assertEqual(response.status_code, 200)
        [self.assertIn(body, expected) for body in response_body]

    def test_create_new_image(self):
        """
        Creates a new image and returns the created object.
        """

        url = '/api/v_0/images/create/'
        with open('base_image/test_files/white.png', 'rb') as f:
            form = {
                'name': 'white_board',
                'file': f
            }
            response = self.client.post(url, data=form)
        self.assertEqual(response.status_code, 201)
        response_body = response.json()
        self.assertEqual(response_body['id'], 1)
        self.assertEqual(response_body['name'], 'white_board')
        self.assertEqual(response_body['file'], '/static/test_files/white.png')
