from django.db import models
from django.utils import timezone

from auditable.models import Auditable

from .Credential import Credential


class Person(Auditable):
    credential = models.ManyToManyField(Credential, related_name="people")
    full_name = models.TextField()
    type = models.TextField()

    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(blank=True, null=True)
