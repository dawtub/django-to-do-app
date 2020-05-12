from django.test import TestCase
from django.urls import reverse

from users.models import CustomUser
from .models import Task


class TaskModelTests(TestCase):
    def setUp(self):
        self.user_1 = CustomUser.objects.create_user('Dave', 'dave@test.com', 'test123')
        self.task_1 = Task.objects.create(user=self.user_1, text='Write unit tests')
        self.task_2 = Task.objects.create(user=self.user_1, text='Commit unit tests', completed=True)

    def test_is_task_completed(self):
        self.assertTrue(self.task_2.is_done(), "Task completed")
        self.assertFalse(self.task_1.is_done(), "Task shouldn't be completed")


class IndexViewPositiveTestCase(TestCase):
    def setUp(self):
        self.user_1 = CustomUser.objects.create_user('Dave', 'dave@test.com', 'test123')
        self.user_2 = CustomUser.objects.create_user('Pjetrek', 'pjetrek@test.com', 'test123')
        self.task_1 = Task.objects.create(user=self.user_1, text='Write unit tests')
        self.task_2 = Task.objects.create(user=self.user_1, text='Commit unit tests', completed=True)

    def test_should_return_two_tasks(self):
        self.client.force_login(user=self.user_1)
        response = self.client.get(reverse('tasks:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['tasks_list']), 2)

    def test_should_create_task(self):
        self.client.force_login(user=self.user_2)
        response = self.client.post(reverse('tasks:add'),
                                    data={'text': 'First task'}
                                    )
        task = Task.objects.filter(user=self.user_2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(task), 1, "Should return 1 task")
        self.assertRedirects(response, '/tasks/')

    def test_should_complete_task(self):
        self.client.force_login(user=self.user_1)
        response = self.client.get(reverse('tasks:complete', args=(self.task_1.pk,)))
        task = Task.objects.get(pk=self.task_1.pk)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(task.is_done(), 'Should be completed')
        self.assertRedirects(response, '/tasks/')

    def test_should_delete_task(self):
        self.client.force_login(user=self.user_1)
        response = self.client.get(reverse('tasks:delete', args=(self.task_1.pk,)))
        self.assertEqual(response.status_code, 302)
        self.assertRaises(Task.DoesNotExist, Task.objects.get, pk=self.task_1.pk)
        self.assertRedirects(response, '/tasks/')

    def test_no_tasks_available(self):
        self.client.force_login(user=self.user_2)
        response = self.client.get(reverse('tasks:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No tasks are available')
        self.assertQuerysetEqual(response.context['tasks_list'], [])
