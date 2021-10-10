from django.urls import reverse
from django.utils.text import slugify
from unidecode import unidecode

from django.db import models


# Create your models here.
class PostModel(models.Model):
    author = models.CharField('Автор статьи', max_length=30)
    title = models.CharField('Название статьи', max_length=50)
    slug = models.SlugField('URL', max_length=60, unique=True, db_index=True, null=True, blank=True)
    text = models.TextField('Текст статьи')
    image = models.ImageField('Картинка к посту', upload_to='img')  # pillow
    publish_date = models.DateTimeField('Время публикации', auto_now=True)
    is_published = models.BooleanField('Пост опубликован?', default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('blog:show_post', kwargs={'post_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            string = str(self.title)
            self.slug = slugify(unidecode(string))
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


# статья -> statia
class Category(models.Model):
    name = models.CharField('Категория', max_length=30, unique=True)
    slug = models.SlugField('URL', max_length=30, unique=True, db_index=True)

    def get_absolute_url(self):
        return reverse('blog:show_cat', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.name
