from imgurpython import ImgurClient
from config import client_id, client_secret, album_id, access_token, refresh_token

if __name__ == "__main__":
    client = ImgurClient(client_id, client_secret, access_token, refresh_token)
    config = {
        'album': album_id,
        'name': 'test-name!',
        'title': 'test-title',
        'description': 'test-description'
    }
    print("Uploading image... ")
    image = client.upload_from_path('static/test.jpg', config=config, anon=False)
    print("Done")
