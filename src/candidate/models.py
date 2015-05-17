from django.db import models
import uuid
import json


class History(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    version = models.PositiveIntegerField()
    events = []

    def apply(self, event_func, **kwargs):
        e = Event(agg_id=self.uuid,
                  name=event_func.__name__,
                  data=json.dumps(kwargs),
                  agg_type=self.__class__.__name__)
        event_func(kwargs)
        self.events.append(e)

    def save(self, *args, **kwargs):
        for e in self.events:
            self.version += 1
            e.version = self.version
            e.save()
        super(History, self).save(*args, **kwargs)
        self.events = []

    def load_events(self):
        return get_events(self.__class__.__name__, self.uuid)

    class Meta:
        abstract = True


class Candidate(History):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, default="")

    def __unicode__(self):
        return self.name

    def update_name(self, name):
        if(self.name != name):
            self.apply(self.name_updated, name=name)

    def name_updated(self, e):
        self.name = e['name']

    def update_email(self, email):
        if(self.email != email):
            self.apply(self.email_updated, email=email)

    def email_updated(self, e):
        self.email = e['email']

    def create(self, name):
        self.apply(self.created, name=name)

    def created(self, e):
        self.name = e['name']
        self.version = 0


def get_candidate(id):
    return Candidate.objects.get(id=id)


def get_candidates():
    return Candidate.objects.all()


def create_candidate(data):
    candidate = Candidate()
    candidate.create(**data)
    candidate.save()
    return candidate


class Event(models.Model):
    name = models.CharField(max_length=255)
    data = models.TextField(default="")
    agg_id = models.UUIDField()
    agg_type = models.CharField(max_length=255)
    version = models.PositiveIntegerField()
    ts = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "{:<20} {:<14} {:<20} {:<20} {:%Y-%m-%d %H:%M:%S}".format(
            self.name,
            self.agg_type,
            self.agg_id,
            self.data,
            self.ts)


def get_events(agg_type, agg_id):
    return list(Event.objects.filter(agg_type=agg_type, agg_id=agg_id)
                             .order_by('-version'))
