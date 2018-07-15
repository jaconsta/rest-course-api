import json
from django.test import TestCase

JSON_TYPE = 'application/json'


class BaseImageTests(TestCase):
    url = '/api/v1/images/'
    headers = {'content-type': 'application/json'}

    @staticmethod
    def decode_response(response):
        return json.loads(response.content.decode('utf-8'))

    def test_create_new_image(self):
        """
        Creates a new image and returns the created object.
        """
        with open('base_image/test_files/white.png', 'rb') as f:
            form = {
                'name': 'public_name',
                'file': f
            }
            response = self.client.post(self.url, data=form)
        self.assertEqual(response.status_code, 201)
        response_body = response.json()
        self.assertEqual(response_body['id'], 1)
        self.assertEqual(response_body['name'], 'public_name')

    def test_list_images(self):
        """
        Creates some images and list them.
        """
        file_names = ['one', 'two', 'three']

        for file_name in file_names:
            image_route = 'base_image/test_files/{file_name}.png'.format(file_name=file_name)
            with open(image_route, 'rb') as f:
                form = {
                    'name': file_name,
                    'file': f
                }
                created_response = self.client.post(self.url, data=form)
            # Ensure it was created
            self.assertEqual(created_response.status_code, 201)

        list_response = self.client.get(self.url)
        self.assertEqual(list_response.status_code, 200)
        images_json = list_response.json()
        self.assertEqual(len(images_json), len(file_names))
        # Image names where created properly
        for image in images_json:
            self.assertIn(image['name'], file_names)
        # All image names are unique.
        response_names = set([image['name'] for image in images_json])
        self.assertCountEqual(response_names, file_names)

    def test_get_one_image(self):
        """
        Creates some images and list them.
        """
        file_names = ['one', 'two']

        for index, file_name in enumerate(file_names, start=1):
            image_route = 'base_image/test_files/{file_name}.png'.format(file_name=file_name)
            with open(image_route, 'rb') as f:
                form = {
                    'id': index,
                    'name': file_name,
                    'file': f
                }
                created_response = self.client.post(self.url, data=form)
            # Ensure it was created
            self.assertEqual(created_response.status_code, 201)

        url = '{url}{image_id}/'.format(url=self.url, image_id=2)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        image_json = response.json()
        self.assertEqual(image_json['name'], file_names[1])

    def test_update_image_name(self):
        """
        Updates the name of the image
        """
        with open('base_image/test_files/white.png', 'rb') as f:
            form = {
                'name': 'public_name',
                'file': f
            }
            response = self.client.post(self.url, data=form)
        self.assertEqual(response.status_code, 201)

        url = '{url}{image_id}/'.format(url=self.url, image_id=1)
        new_name = 'new_name'
        data = {
            'name': new_name
        }
        patch_response = self.client.put(url, data=json.dumps(data), content_type=JSON_TYPE)
        self.assertEqual(patch_response.status_code, 200)
        patch_image = patch_response.json()
        self.assertEqual(patch_image['name'], new_name)
