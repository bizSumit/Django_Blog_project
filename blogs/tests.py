from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from .models import Author, Blog

class BlogPageTests(SimpleTestCase):

    # to check with url pattern
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)


    # to check with url name
    def test_url_correct_for_name(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogs/blog.html')
        self.assertContains(response, '<h1>This is blog ')


    # def test_correct_template_used(self):
    #     response = self.client.get(reverse('blog'))
    #     self.assertTemplateUsed(response, 'blogs/blog.html')

    # def test_template_content_is_correct(self):
    #     response = self.client.get(reverse('blog'))
    #     self.assertContains(response, '<h123>This is blog ')

class AuthorsPageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author1 = Author.objects.create(name="Author123",
                                           genere="Fiction",
                                           email="dummy@email.com")
    
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/author/')
        self.assertEqual(response.status_code, 200)

    def test_url_exists_name(self):
        response = self.client.get(reverse("authors"))
        self.assertEqual(response.status_code, 200)

    def test_correct_template_used(self):
        response = self.client.get(reverse("authors"))
        self.assertTemplateUsed(response, 'blogs/authors.html')

    def test_template_content_correct(self):
        response = self.client.get(reverse("authors"))
        self.assertContains(response, "Author123")


class HomePageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author2 = Author.objects.create(name="Test123",
                                            genere="Fictionaa",
                                            email="Dummy@gmail.com")
        cls.blog1 = Blog.objects.create(title="Blog post one",
                                        author=cls.author2,
                                        blog_text="this is blog first case")
        cls.blog2 = Blog.objects.create(title="Blog post 2second",
                                        author=cls.author2,
                                        blog_text="this is blog second case")

    def test_home_by_url(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    # def test_author_page_in_home_page_tests(self):
    #     response = self.client.get(reverse('authors'))
    #     self.assertContains(response, "Author123")

    def test_home_page(self):
        response = self.client.get(reverse('index_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogs/index.html')
        self.assertContains(response, "Test123")
        self.assertContains(response, "Blog post one")
        self.assertContains(response, "Blog post 2second")        

    def test_blog_detail_view(self):
        response = self.client.get(reverse("detailed_blog", kwargs={'pk':self.blog1.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogs/detailed_blog.html')
        self.assertContains(response, "Test123")
        self.assertContains(response, "Blog post one")
        self.assertContains(response, "this is blog first case")
        

    def test_suthor_detail_page(self):
        response = self.client.get(reverse('author_details', args=[self.author2.pk]))  #kwargs={'author_id':self.author2.pk}
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogs/author_details.html')
        self.assertContains(response, "Dummy@gmail.com")
        self.assertContains(response, "Test123")
        self.assertContains(response, "Blog post one")
        self.assertContains(response, "Blog post 2second")