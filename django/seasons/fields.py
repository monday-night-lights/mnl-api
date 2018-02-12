from django.contrib.postgres.fields import ArrayField
from django.forms import MultipleChoiceField


class ChoiceArrayField(ArrayField):
    '''
    A field that allows us to store an array of choices.

    Uses Django's Postgres ArrayField and a MultipleChoiceField for its formfield.

    Usage:

        choices = ChoiceArrayField(
            models.CharField(max_length=..., choices=(...,)), default=[...])
    '''

    def formfield(self, **kwargs):
        defaults = {
            'form_class': MultipleChoiceField,
            'choices': self.base_field.choices,
        }
        defaults.update(kwargs)
        return super(ArrayField, self).formfield(**defaults)
