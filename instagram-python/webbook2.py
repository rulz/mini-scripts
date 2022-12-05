## funciona bien
from instagrapi import Client
from instagrapi.types import Usertag, Location

import threading

cl = Client()
cl.login('elrulz', 'Elrulz1212!')
# user = cl.user_info_by_username('rulzcl')

for i in range(1, 4):
    path = '/Users/raulsepulveda/Proyectos/TIClass/instagram-python/img/e-test-1.jpeg'
    caption = 'FF Prueba {}'.format(i)
    extra_data = {
        'custom_accessibility_caption': 'alt FF prueba {}'.format(i),
        'like_and_view_counts_disabled': False,
        'disable_comments':False,
    }
    medio = cl.photo_upload(
        path=path,
        caption=caption,
        extra_data=extra_data
    )

    # process = threading.Thread(
    #     target=cl.photo_upload,
    #     args=[path, caption, extra_data]
    # )
    # process.start()
