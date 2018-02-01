from django.contrib.admin import AdminSite as DefaultAdminSite
from django.utils.translation import gettext as _, gettext_lazy


class AdminSite(DefaultAdminSite):
    '''
    https://github.com/django/django/blob/master/django/contrib/admin/sites.py#L30
    '''
    title = 'Monday Night Lights'
    site_title = gettext_lazy(title)
    site_header = gettext_lazy(title)
    index_title = gettext_lazy('Admin')
    # site_url = '/'
    # _empty_value_display = '-'
    # login_form = None
    # index_template = None
    # app_index_template = None
    # login_template = None
    # logout_template = None
    # password_change_template = None
    # password_change_done_template = None


mnl_admin = AdminSite(name='admin')
