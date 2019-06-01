from django.test import TestCase


class LandingPageViewTest(TestCase):
    def test_view_should_have_form_with_email_field_and_submit_button(self):
        response = self.client.get('/')

        expected = '<form action="." method="post">'
        self.assertContains(response, expected, status_code=200)
        expected = '<input name="email" type="email">'
        self.assertContains(response, expected, status_code=200)
        expected = '<button type="submit">Submit</button>'
        self.assertContains(response, expected, status_code=200)

