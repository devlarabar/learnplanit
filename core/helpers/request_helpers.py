def prepare_context(request, **kwargs):

    user = request.user
    logged_in = user.is_authenticated
    context = {}

    if not logged_in:
        context.update({
            'theme': 'dark',
            'logged_in': False,
        })
        return context

    request.session.set_expiry(1209600)

    context.update({
        'logged_in': True,
        'theme': 'dark',
        'username': str(request.user),
        'admin': request.user.is_superuser
    })
    return context


def get_user_id(request):
    logged_in = request.user.is_authenticated
    if logged_in:
        return request.user.id
    else:
        return None
