from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Posts

class BlogTest(TestCase):
    def setUp(self):
        self.user = get_user_model.create.user(
            
                username = 'maghsood026',
                email    =  'maghsood95@gmail.com',
                password =  '111111', 
            
        )
        self.post = Posts.object.create(
            
                title  = '302 status code',
                author = self.user,
                body   = 'templary redirect'
        )

        def test_string_representaion(self):
            post = Posts(title = 'programming is good')
            self.assertEqual(str(post), post.title)
        
        def test_get_absolute_url(self):
            self.assertEqual(self.post.test_get_absolute_url(), '/post/1/')

        def get_post_content(self):
            self.assertEqual(f'self.post.title' , '302 status code')
            self.assertEqual(f'self.post.author', 'maghsood026')
            self.assertEqual(f'self.post.body'  , 'templary redirect')

        def test_post_list_view(self):
            response = self.client.get(reverse('home'))
            self.assertEqual(response.status_code, 200)
            self.assertEqualContains(response, '302 status code')
            self.assertTemplateUsed(response, 'home.html')

        def test_post_list_detail(self):
            response = self.client.get(reverse('/post/1/'))
            no_response = self.client.get(reverse('/post/1000/'))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(no_response.status_code, 404)
            self.assertEqualContains('302 status code')
            self.assertTemplateUsed('post_detail.html')

        def test_create_post_view(self):
            response = self.client.post(reverse('post_new'),{
                'title' : 'new title',
                'body'  : 'body of post',
                'author': self.user  
            })
            self.assertEqual(response.status_code, 200)
            self.assertEqualConatins(response, 'new title')
            self.assertEqualTemplateUsed(response, 'post_new.html')
        
        def test_update_post_view(self):
            response = self.client.post(reverse('update_post', args = '1'), {
            'title': 'Updated title',
            'body': 'Updated text',
            })
            self.assertEqual(response.status_code, 302)
        
        def test_post_delete_view(self):
            response = self.client.get(
            reverse('post_delete', args='1'))
            self.assertEqual(response.status_code, 200)


