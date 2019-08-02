from import_export import resources
from newsletter.models import Subscriber


class PersonResource(resources.ModelResource):
    class Meta:
        model = Subscriber