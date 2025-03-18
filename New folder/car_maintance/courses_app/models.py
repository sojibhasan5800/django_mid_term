from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# from .fields import orderField
# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    class Meta:
        ordering =['title']
    def __str__(self):
        return self.title

class Course(models.Model):
    owner = models.ForeignKey(User,related_name='courses_created', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,related_name='subject_created', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_date']
    def __str__(self):
        return self.title

class Modules(models.Model):
    course = models.ForeignKey(Course,related_name='modules_created', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    # order = orderField(blank = True, for_fields=['course']) // session-5-2 Customize Fields
   
    class Meta:
        # ordering = ['order']
        pass
    def __str__(self):
        return self.title

# class Content(models.Model):
#     module = models.ForeignKey(Modules,related_name='contents', on_delete=models.CASCADE)
#     content_type = models.ForeignKey(ContentType,related_name='contentstype', on_delete=models.CASCADE,
#                                      limit_choices_to={
#                                          {'model_int':
#                                           ('text',
#                                            'video',
#                                            'image',
#                                            'file')}
#                                      } )
#     object_id = models.PositiveIntegerField()
#     item = GenericForeignKey('content_type','object_id')
   
#     # order = orderField(blank = True, for_fields=['course']) // session-5-2 Customize Fields
   
#     class Meta:
#         # ordering = ['order']
#         pass




