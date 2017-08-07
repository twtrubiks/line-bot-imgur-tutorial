from auth import authenticate
from config import album_id


def upload(client_data):
    config = {
        'album': album_id,
        'name': 'test-name!',
        'title': 'test-title',
        'description': 'test-description'
    }

    print("Uploading image... ")
    client_data.upload_from_path('static/test.jpg', config=config, anon=False)
    print("Done")

    return image


if __name__ == "__main__":
    client = authenticate()
    image = upload(client)
