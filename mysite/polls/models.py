import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    # change to __str__ model
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):                  # __unicode__ on Python 2
        return '%s' % (self.question_text)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    # change to __str__ model
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):             # __unicode__ on Python 2
        return '%s' % (self.choice_text)

# class Question(models.Model):
#   question_text = models.CharField(max_length=200)
#   pub_date = models.DateTimeField('date published')
#
# class Choice(models.Model):
#   question = models.ForeignKey(Question)
#   choice_text = models.CharField(max_length=200)
#   votes = models.IntegerField(default=0)

#   def was_published_recently(self):
#      return self.pub_date >= timezone.now() - datetime.timedelta(days=1)