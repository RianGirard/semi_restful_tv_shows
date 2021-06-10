from django.db import models
# import re

class ShowManager(models.Manager):
    def basic_validator(self, postData, source):
        errors = {}
        if len(postData['title']) < 1: 
            errors['title'] = 'Title name missing'
        all_shows = Show.objects.all()              # instantiate all_shows
        for show in all_shows:                      # loop through all_shows
            if postData['title'] == show.title and source == 'create':    # error if postData title == show.title | rule applies to source = 'create', not 'update'
                errors['title'] = 'That show has already been entered!'
        if len(postData['network']) < 1: 
            errors['network'] = 'Select a network'
        if len(postData['release_date']) < 1: 
            errors['release_date'] = 'Select a release date'
        if len(postData['description']) != 0 and len(postData['description']) < 10:
            errors['description'] = 'Description not long enough'
        # EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # if not EMAIL_REGEX.match(postData['email']):
        #     errors['email'] = ('Invalid email address!')
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()     # new line replaces default value of objects = models.Manager()

    def __repr__(self):
        return f"<Show object: {self.title} | {self.network} | ID#: {self.id}>"

# Create your models here.
