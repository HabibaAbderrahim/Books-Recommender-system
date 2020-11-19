# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Movie(models.Model):
    author = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=41, blank=True, null=True)
    category = models.CharField(max_length=75, blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    publish_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    description = models.CharField(max_length=370, blank=True, null=True)
    image = models.ImageField(upload_to='movies')
    banner = models.ImageField(upload_to='movies_banner',blank=True, null=True)
    slug = models.SlugField(max_length=100)
    count = models.IntegerField(default=0)
    language = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'book'

    def save(self, *args , **kwargs):
         if not self.slug :
              self.slug = slugify(self.title)
         super(Movie , self).save(*args ,**kwargs)


    def __str__(self):
       return self.title


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'



class Post(models.Model):
    num_movie = models.ForeignKey(Movie, models.DO_NOTHING, db_column='num_movie')
    num_user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='num_user')
    note = models.IntegerField()
    datecrea = models.DateField(db_column='dateCrea')  # Field name made lowercase.
    idpost = models.AutoField(primary_key=True , max_length=40)

    class Meta:
        managed = True
        db_table = 'post'
    def __str__(self):
       return '{}-{}'.format(self. num_movie.title,(self.num_user.username))
   

class TopBooks(models.Model):
    id_tops = models.AutoField(db_column='id_Tops', primary_key=True,  default="", editable=False)  # Field name made lowercase.
    book = models.ForeignKey(Movie, models.DO_NOTHING, db_column='Book')  # Field name made lowercase.
    top1 = models.ForeignKey(Movie, models.DO_NOTHING, db_column='Top1',related_name='topic_content_type1')  # Field name made lowercase.
    top2 = models.ForeignKey(Movie, models.DO_NOTHING, db_column='Top2',related_name='topic_content_type2')  # Field name made lowercase.
    top3 = models.ForeignKey(Movie, models.DO_NOTHING, db_column='Top3',related_name='topic_content_type3')  # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'top_books'

    def __str__(self):
       return '{}'.format(self.book.title)

class Top(models.Model):
    id_tops = models.AutoField(db_column='id_Tops', primary_key=True,  default="", editable=False) # Field name made lowercase.
    book = models.ForeignKey(Movie, models.DO_NOTHING, db_column='Book')  # Field name made lowercase.
    top1 = models.ForeignKey(Movie, models.DO_NOTHING, db_column='Top1',related_name='topitype1')  # Field name made lowercase.
    top2 = models.ForeignKey(Movie, models.DO_NOTHING, db_column='Top2',related_name='topictype')  # Field name made lowercase.
    top3 = models.ForeignKey(Movie, models.DO_NOTHING, db_column='Top3',related_name='topictype3')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'top'