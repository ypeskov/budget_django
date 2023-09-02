# from django.db.models import Manager, QuerySet
from django.db import models
from django.utils import timezone
from django.conf import settings


def get_settings():
    default_settings = dict(
        cascade=True,
    )
    return getattr(settings, 'DJANGO_SOFTDELETE_SETTINGS', default_settings)


class BaseModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def delete(self, cascade=None, *args, **kwargs):
        cascade = get_settings()['cascade']
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
        self.after_delete()
        if cascade:
            self.delete_related_objects()
        # TODO: Call soft_delete_signals

    def restore(self, cascade=None):
        cascade = get_settings()['cascade']
        self.is_deleted = False
        self.deleted_at = None
        self.save()
        self.after_restore()
        if cascade:
            self.restore_related_objects()
        # TODO: Call soft_delete_signals

    def hard_delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

    def get_related_objects(self):
        related_models = {}
        # first get all related models
        for field in self._meta.get_fields():
            if isinstance(field, models.OneToOneRel):
                related_models[field.field.name] = field.related_model
            elif isinstance(field, models.ManyToOneRel):
                related_models[field.field.name] = field.related_model

        # Then get all related instances of related models of the current object
        related_objects = []
        for key, related_model in related_models.items():
            try:
                related = related_model.objects.filter(**{key: self.pk})
                related_objects.extend(related)
            except Exception as e:
                print(e)

        return related_objects

    def delete_related_objects(self):
        for obj in self.get_related_objects():
            obj.delete()

    def restore_related_objects(self):
        for obj in self.get_related_objects():
            print(obj)
            obj.restore()

    def after_delete(self):
        pass

    def after_restore(self):
        pass
