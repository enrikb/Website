from datetime import timezone, datetime
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.db import models

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class InserationManager(models.Manager):

    def create_inseration(self, user, title, description, images, category, subcategory, size):
        if not title:
            raise ValueError("Users must have an email address")
        if not user:
            raise ValueError("Users must have a user")
        if not images:
            raise ValueError("Users must have a password")
        if not category:
            raise ValueError("Users must have an title")
        if not size:
            raise ValueError("Users must have an first name")

        inseration = self.model(
            user=user,
            title=title,
            description=description,
            images=images,
            category=category,
            subcategory=subcategory,
            size=size,
            inserted_at=datetime.now,
        )

        inseration.save(using=self._db)
        return inseration


class Inseration(models.Model):
    inserter = models.ForeignKey(AUTH_USER_MODEL, related_name='inserted_object', verbose_name=_("Inserter"),
                                 on_delete=models.CASCADE)
    title = models.CharField(max_length=50,null=False, blank=False)
    description = models.TextField(max_length=500,null=False, blank=False)
    images = models.ImageField(upload_to='images/',max_length=50,null=False, blank=False)
    subcategory = models.CharField(max_length=50,null=False, blank=False)
    category = models.CharField(max_length=50,null=False, blank=False)
    size = models.CharField(max_length=50, null=False, blank=False)

    inserted_at = models.DateTimeField(_("inserted_at"), auto_now_add=True)

    objects = InserationManager()

    def save(self, **kwargs):
        if not self.id:
            self.inserted_at = timezone.now()
        super(Inseration, self).save(**kwargs)

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




