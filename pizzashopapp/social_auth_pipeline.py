from pizzashopapp import Client

def create_client(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        avatar = 'https://graph.facebook.com/%s/picture?type=large' & response['id']

    Client.objects.create(user_id, avatar = avatar)
