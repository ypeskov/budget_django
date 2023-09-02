from django.db.models import Manager, QuerySet
from django.db import models
from django.utils import timezone


class AppQuerySet(QuerySet):
    def delete(self):
        self.update(is_deleted=True)


class AppManager(Manager):
    def get_queryset(self):
        return AppQuerySet(self.model, using=self._db).exclude(is_deleted=True)


class BaseModel(models.Model):
    class Meta:
        abstract = True

    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = AppManager()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def delete(self, using=None, keep_parents=False):
        """Mark the record as deleted instead of deleting it"""
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super(BaseModel, self).delete()

