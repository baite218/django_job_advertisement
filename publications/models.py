from django.db import models
from datetime import datetime




class Post(models.Model):
    user = models.ForeignKey('users.Profile', models.CASCADE, null=True, blank=True)
    category = models.ForeignKey('publications.Category', models.CASCADE, 'post_category', null=True,  blank=True)
    price = models.DecimalField('оплата', max_digits=10, decimal_places=0)
    text = models.TextField('текст')
    created_date = models.DateTimeField('дата создания',auto_now_add=True)
    readers = models.ManyToManyField('users.Profile', through='UserPostRelation', related_name='posts')

    def __str__(self):
        return f'for: {self.category}: {self.price}'

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'



class UserPostRelation(models.Model):
    user = models.ForeignKey('users.Profile', models.CASCADE, blank=True)
    post = models.ForeignKey('publications.Post', models.CASCADE)
    like = models.BooleanField('лайк',default=False)
    saved = models.BooleanField('сохранения',default=False)

    def __str__(self):
        return f' {self.user.username}: {self.post.profession}'

    class Meta:
        verbose_name = 'лайк_и_сохранения'
        verbose_name_plural = 'лайки_и_сохранения'


 
class Comments(models.Model):
    owner = models.ForeignKey('users.Profile', models.CASCADE)
    post = models.ForeignKey('publications.Post', models.CASCADE)
    text = models.TextField('Коментарий')

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'комментария'
        verbose_name_plural = 'комментарии'



class Category(models.Model):
    name = models.CharField('Категория', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категория'
