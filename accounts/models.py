from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

# Create your models here.
# ユーザーを生成する時使うヘルパー(Helper)クラス
class UserManager(BaseUserManager):
    def create_user(self, username, email, affiliation, position, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            affiliation=affiliation,
            position=position,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, affiliation, position, password):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            affiliation=affiliation,
            position=position,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# 実際のモデル(Model)で、AbstractBaseUserを相続して作るクラス
class User(AbstractBaseUser):
    username = models.CharField(
        verbose_name='名前',
        max_length=255,
    )
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    affiliation = models.CharField(
        verbose_name='所属',
        max_length=255,
    )
    position = models.CharField(
        verbose_name='役職',
        max_length=255,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'affiliation', 'position']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin