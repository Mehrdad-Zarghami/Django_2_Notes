from django.test import TestCase
from django.shortcuts import reverse
from .models import Note


class NotesListViewTest(TestCase):
    def setUp(self):
        """
        To create sample objects for testing purposes and use this sample objects in different tests.
        """
        self.sample_note_1 = Note.objects.create(text='sample_text_for_mehrdad', author='mehrdad')

    def test_notes_list_view_url(self):  # The name of our methods in Test class should start with the word 'test'.
        response = self.client.get('/')  # Send a get request to the address of "NameOfWebsite.com/" and get response
        self.assertEqual(response.status_code, 200)  # Check if status_code is 200 (successful) or not

    def test_notes_list_view_url_by_name(self):
        response = self.client.get(reverse('notes_list'))
        self.assertEqual(response.status_code, 200)

    def test_notes_list_page_contain_text(self):
        # a test to check if "notes_list" page contains the text of notes(records of database) or not

        # Create a sample note for testing purposes:

        response = self.client.get(reverse('notes_list'))
        self.assertContains(response, self.sample_note_1.text)

        
        
# obj = NotesListViewTest()
# res = obj.test_notes_list_view_url()
# print(res)
