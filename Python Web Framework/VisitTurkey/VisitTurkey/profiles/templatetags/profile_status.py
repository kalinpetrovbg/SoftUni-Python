from django.template import Library
from VisitTurkey.profiles.models import Profile

register = Library()

@register.inclusion_tag('tags/profile_status.html', takes_context=True)
def profile_status(context):
    current_user = context.request.user.id
    profile = Profile.objects.get(pk=current_user)
    return {'is_complete': profile.is_complete}
