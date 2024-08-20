from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.core.exceptions import PermissionDenied
from accounts.models import Usuario


def group_required(groups, login_url=None, raise_exception=False):
    user = Usuario

    def check_perms(user):
        if user.is_superuser:
            return True

        if isinstance(groups, list):
            group_names = groups
        else:
            group_names = [groups]

        if user.groups.filter(name__in=group_names).exists():
            return True

        if raise_exception:
            raise PermissionDenied

        return False

    return user_passes_test(check_perms, login_url=login_url)

def create_groups():
    if not Group.objects.exists():
        groupAdmin = Group(name='vendedor')
        groupAdmin.save()

        groupAdmin = Group(name='caixa')
        groupAdmin.save()

        groupAdmin = Group(name='administrador')
        groupAdmin.save()






