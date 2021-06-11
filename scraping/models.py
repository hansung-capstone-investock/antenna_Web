from django.db import models, connection
from datetime import timezone
import datetime

class dcData(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    count = models.IntegerField()

    def __str__(self):
        return self.title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(
                f'TRUNCATE TABLE {cls._meta.db_table}'
            )

# class fmkorData(models.Model):
#     title = models.CharField(max_length=200)
#     count = models.IntegerField()

#     def __str__(self):
#         return self.title
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

#     @classmethod
#     def truncate(cls):
#         with connection.cursor() as cursor:
#             cursor.execute(
#                 f'TRUNCATE TABLE {cls._meta.db_table}'
#             )

# class companyData(models.Model):
#     name = models.CharField(max_length=200)
#     code = models.CharField(max_length=6)

#     def __str__(self):
#         return self.name
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class MainNews(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000,default='')
    summary = models.TextField()
    publishDay = models.CharField(max_length=100)
    link = models.TextField()
    
    class Meta:
        # db_table = 'breakingnews'
        ordering= ('title',)
    
    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(
                f'TRUNCATE TABLE {cls._meta.db_table}'
            )

class LiveNews(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000,default='')
    summary = models.TextField()
    publishDate = models.CharField(max_length=100)
    link = models.TextField()

    class Meta:
        ordering= ('publishDate',)
    
    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(
                f'TRUNCATE TABLE {cls._meta.db_table}'
            )