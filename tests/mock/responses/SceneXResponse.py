import time

def SceneXResponse(input):
    return {
        'result': [
            {
                'id': 'aaaaaaaaaaaaaaaaaaaaaaaaaaa' + str(i),
                'image': e['image'],
                'features': e['features'],
                'uid': 'aaaaaaaaaaaaaaaaaaaaaaaaaaa' + str(i),
                'algorithm': e.get('algorithm', 'Aqua'),
                'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec convallis ipsum est, et iaculis lacus tincidunt eget. Sed dictum diam ex, eget aliquam urna porta a.',
                'userId': 'zoyqq4zkwdZLiBgH0eyhx4fcN9b2',
                'createdAt': int(time.time() * 1000),
                'i18n': {l: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec convallis ipsum est, et iaculis lacus tincidunt eget. Sed dictum diam ex, eget aliquam urna porta a.' for l in e.get('languages', ['en'])}
            }
            for i, e in enumerate(input["data"])
        ]
    }