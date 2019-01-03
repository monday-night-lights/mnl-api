from django.forms import ModelForm, ModelMultipleChoiceField
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import Group

from .models import User


class GroupAdminForm(ModelForm):
    users = ModelMultipleChoiceField(
        queryset=User.objects.filter(is_staff=True),
        widget=FilteredSelectMultiple('Users', False),
        required=False)

    class Meta:
        model = Group
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        if instance is not None:
            initial = kwargs.get('initial', {})
            initial['users'] = instance.user_set.all()
            kwargs['initial'] = initial
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        group = super().save(commit=commit)

        if commit:
            group.user_set = self.cleaned_data['users']
        else:
            old_save_m2m = self.save_m2m

            def new_save_m2m():
                old_save_m2m()
                group.user_set = self.cleaned_data['users']
            self.save_m2m = new_save_m2m

        return group
