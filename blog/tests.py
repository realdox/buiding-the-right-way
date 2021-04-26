from django.test import TestCase
from django.contrib.auth import get_user_model # inbuil user for author authentication
from django.urls import reverse # it is important for get absolute url
from .models import Post 

class RealdoxMappingText(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="musterdseeddev",
            email='anything@email.com',
            password = 'nonofurbusines'
        )

        self.post = Post.objects.create(
        title='This is personal',
        body='Nice body content',
        author=self.user,
        )

 
        
    def test_post_content(self):
        
        self.assertEqual(f"{self.post.author}",'musterdseeddev')
        self.assertEqual(f"{self.post.body}",'Nice body content')

    def test_post_main_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'blog/home.html')

    def test_post_detail_view(self):
        response = self.client.get('/detail/1/')
        no_response = self.client.get('/detail/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'This is personal')
        self.assertTemplateUsed(response, 'blog/post_detail.html')





















