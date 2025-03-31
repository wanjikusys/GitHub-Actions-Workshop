from django.test import TestCase
from django.urls import reverse
from .models import Task

class TaskModelTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(text='Test Task')

    def test_task_creation(self):
        self.assertEqual(self.task.text, 'Test Task')
        self.assertFalse(self.task.completed)

class TaskViewsTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(text='Test Task')

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task')
        self.assertTemplateUsed(response, 'index.html')

    def test_task_detail_view(self):
        response = self.client.get(reverse('task_detail', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task')
        self.assertTemplateUsed(response, 'detail.html')

    def test_create_task(self):
        response = self.client.post(reverse('index'), {'task': 'New Task'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Task.objects.filter(text='New Task').exists())

    def test_edit_task(self):
        response = self.client.post(reverse('edit_task', args=[self.task.id]), {'task': 'Updated Task'})
        self.task.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.task.text, 'Updated Task')

    def test_delete_task(self):
        response = self.client.post(reverse('delete_task', args=[self.task.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())