from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Facebook(models.Model):
    id = models.BigIntegerField(primary_key=True)
    person = models.ForeignKey('main.Person')

    def __unicode__(self):
        return self.person.name


class Steam(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    is_main = models.BooleanField()
    person = models.ForeignKey('main.Person')

    def __unicode__(self):
        return self.name

    # On calling save(), check to see if "is_main" has been set on another
    # Steam object.  If it has, set "is_main" to false on that object.
    def save(self, *args, **kwargs):
        if self.is_main:
            try:
                temp = Steam.objects.get(is_main=True)
                if self != temp:
                    temp.is_main = False
                    temp.save()
            except Steam.DoesNotExist:
                pass
        super(Steam, self).save(*args, **kwargs)


class Hero(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name