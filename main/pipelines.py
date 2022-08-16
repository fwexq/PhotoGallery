import requests
from collections import OrderedDict
from urllib.parse import urlunparse, urlencode
from django.core.files.base import ContentFile
from django.utils import timezone
from main.models import CustomUser

def save_user_profile(backend, request, user, response, *args, **kwargs):
    if backend.name == 'google-oauth2':
        date = timezone.now().date()
        today = CustomUser.objects.filter(day=date)
        if today:
            user.day = timezone.now()
            user.count += 1
        else:
            user.dayTime = date
            user.count = 1
        user.save()

        # https://www.googleapis.com//oauth2/v2/userinfo?access_token=ya29.A0AVA9y1vsQ89Y_g78qO7ird_2lBfhlBKjZ4ItT1ReMYtW8viUJZYz2EBamOoXHxm2C_1_KTcXkhck1mwagZZ6RdWbh9OvN7m3ht8uWMJOd0qUtqMILTVWUzkKLSgcaVXWRXbgaRg_GfxHVwXvgbDNu48EeMfiqwYUNnWUtBVEFTQVRBU0ZRRTY1ZHI4NXhEZWtkZFlHSXBNWVk4WkdKc2pVdw0165
        resp = requests.get('https://www.googleapis.com//oauth2/v2/userinfo?access_token=' + response['access_token'])
        print(resp)

        if resp.status_code != 200:
            return
        data = resp.json()
        if data['picture']:
            photo_link = data['picture']
            photo_response = requests.get(photo_link)
            path_photo = f'user/images/google/{user.pk}.jpg'
            with open(f'media/{path_photo}', 'wb') as photo:
                photo.write(photo_response.content)
            user.avatar = path_photo
        user.save()

    elif backend.name == 'vk-oauth2':

        date = timezone.now().date()
        today = CustomUser.objects.filter(day=date)
        if today:
            user.count += 1
        else:
            day_visits = CustomUser()
            day_visits.dayTime = date
            day_visits.count = 1
        user.save()

        api_url = urlunparse(('http', 'api.vk.com', 'method/photos.get', None,
                          urlencode(
                              OrderedDict(album_id='profile', access_token=response['access_token'],
                                          v=5.131)), None))
        resp = requests.get(api_url)
        print(resp)
        avatar_url = sorted(resp.json()['response']['items'][0]['sizes'], key=lambda x: x['width'], reverse=True)[0]['url']
        # data1 = resp1.json()['response'][0]

        if resp.status_code != 200:
            return

        # api_key = data['access_token']
        # user.api_key = api_key

        if avatar_url:
            photo = ContentFile(requests.get(avatar_url).content)
            # photo_response = requests.get(avatar_url)
            # path_photo = f'user/images/{user.pk}.jpg'
            # with open(f'media/{path_photo}', 'wb') as ph:  #запись в байтах
            #     ph.write(photo_response.content)
            user.avatar.save(f'media/user/images/vk/{user.pk}.jpg', photo, save=True)

