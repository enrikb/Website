from datetime import timezone, datetime
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.db import models

from account.models import Account


CATEGORY_CHOICES = []
SUBCATEGORY_CHOICES = []

class InserationManager(models.Manager):

    def create_inseration(self, title, description, images, category, subcategory, size):
        if not title:
            raise ValueError("Users must have an email address")
        if not images:
            raise ValueError("Users must have a password")
        if not category:
            raise ValueError("Users must have an title")
        if not size:
            raise ValueError("Users must have an first name")

        inseration = self.model(
            title=title,
            description=description,
            images=images,
            category=category,
            subcategory=subcategory,
            size=size,
        )
        inseration.save(using=self._db)
        return inseration


<<<<<<< HEAD
class Inseration(models.Model):
    inserter = models.ForeignKey(AUTH_USER_MODEL, related_name='inserted_object', verbose_name=_("Inserter"),
                                 on_delete=models.CASCADE)
    title = models.CharField(max_length=50,null=False, blank=False)
    description = models.TextField(max_length=500,null=False, blank=False)
    images = models.ImageField(upload_to='images/',max_length=50,null=False, blank=False)
    subcategory = models.CharField(max_length=50,null=False, blank=False)
    category = models.CharField(max_length=50,null=False, blank=False)
    size = models.CharField(max_length=50, null=False, blank=False)
=======
<<<<<<< HEAD
=======
class Inseration(models.Model):
    inserter = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    images = models.ImageField(upload_to='images/', max_length=50, null=False, blank=False)
    subcategory = models.CharField(max_length=50, null=False, blank=False)
    category = models.CharField(max_length=50, null=False, blank=False, choices=CATEGORY_CHOICES)
    size = models.CharField(max_length=50, null=False, blank=False)
>>>>>>> a12e047... worked on inseration module
>>>>>>> 2b4b6af1a3d507fb716183ea02ad7d1150381a8c

    inserted_at = models.DateTimeField(_("inserted_at"), auto_now_add=True)

<<<<<<< HEAD
    objects = InserationManager()


    def inseration_count_for(user):
        """
        returns the number of unread messages for the given user but does not
        mark them seen
        """
        return Inseration.objects.filter(inserter=user).count()

    class Meta:
        ordering = ['-inserted_at']
        verbose_name = _("Insertion")
        verbose_name_plural = _("Insertions")
<<<<<<< HEAD




<<<<<<< HEAD
=======
    def has_module_perms(self, app_label):
        return True
=======
>>>>>>> a12e047... worked on inseration module
>>>>>>> 2b4b6af1a3d507fb716183ea02ad7d1150381a8c
=======
>>>>>>> 2081c79... worked on inseration, works now
