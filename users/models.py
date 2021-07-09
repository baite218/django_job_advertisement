from django.db import models
from django.contrib.auth.models import AbstractUser
# from .choices import ProfessionsChoice



class Profile(AbstractUser):
    phone = models.CharField('телефон', max_length=200)
    email = models.EmailField('Email адрес', blank=True)
    subscribe = models.ManyToManyField('users.Profile', through='Subscriber', related_name='profile_followers')
    rusume = models.ForeignKey('users.ProfileResume', models.CASCADE, 'user_rusume', null=True, blank=True)
    profession = models.ForeignKey('users.Professions', models.CASCADE, 'user_profes', null=True, blank=True)

    def __str__ (self):
        return f'{self.username} {self.profession} {self.phone} '

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'профили'



class ProfileResume(models.Model):
    user = models.ForeignKey('users.Profile', models.CASCADE, blank=True)
    profession = models.ForeignKey('users.Professions', models.CASCADE, 'profesion')
    urlfield = models.URLField(max_length=200, blank=True, null=True)
    field = models.FileField(upload_to='user_avatar/', blank=True, null=True)

    def __str__(self):
        return f'{self.profession} {self.field} rusume'

    class Meta:
        verbose_name = 'резюме'
        verbose_name_plural = 'резюме'



class Professions(models.Model):
    User_CHOICES = (
        ("J", "Jobless"),
        ("B", "Dentist"),
        ("T", "Teacher"),
        ("S", "School_Psychologist"),
        ("W", "Web_Developer"),
        ("C", "Computer_Programmer"),
        ("N", "IT_Manager"),
    )
    name = models.CharField(max_length=255, choices=User_CHOICES, default="J")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'профессия'
        verbose_name_plural = 'профессия'



class Subscriber(models.Model):
    author = models.ForeignKey('users.Profile', models.CASCADE, 'profile_author')
    follower = models.ForeignKey('users.Profile', models.CASCADE, 'author_follower')
    subscribe = models.BooleanField(default=False)

    def __str__ (self):
        return f'{self.follower.username} subscribed to {self.author.username}'
    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписка'
