from pyramid.security import Allow, Everyone, Authenticated


class EntryFactory(object):
    __acl__ = [
        (Allow, Everyone, 'view'),
        (Allow, Authenticated, 'create'),
        (Allow, Authenticated, 'edit'),
    ]

    # Does nothing, but here to show that we could have done something with
    # the incoming request.
    def __init__(self, request):
        pass
