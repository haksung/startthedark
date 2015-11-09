from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User

class Event(models.Model):
    description = models.TextField()
    creation_date = models.DateTimeField(default=datetime.now)
    start_date = models.DateTimeField(null=True, blank=True)
    creator = models.ForeignKey(User, related_name='event_creator_set')
    attendees = models.ManyToManyField(User, through="Attendance")
    latest = models.BooleanField(default=True)

    def __unicode__(self):
        return self.description

    def save(self, **kwargs):
        Event.objects.today().filter(latest=True,
            creator=self.creator).update(latest=False)
        super(Event, self).save(**kwargs)

class Attendance(models.Model):
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)
    registration_date = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return "%s is attendin %s" % (self.user.username, self.event)
        

    
