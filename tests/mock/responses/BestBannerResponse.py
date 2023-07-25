import time

def BestBannerResponse(input):
    return {
        'result': [
            {
                'id': 'aaaaaaaaaaaaaaaaaaaaaaaaaaa' + str(i),
                'userId': 'zoyqq4zkwdZLiBgH0eyhx4fcN9b2',
                'text': e['text'],
                'plainText': None,
                'algorithms': ['PICO'] * (4 if not e.get('bannerCount') or e['bannerCount'] < 4 else e['bannerCount']),
                'resolution': {
                    'width': 1024,
                    'height': 1024
                },
                'banners': [{
                    'id': 'aaaaaaaaaaaaaaaaaaaaaaaaaaa' + str(i),
                    'url': 'https://picsum.photos/1024'
                } for _ in range(4 if not e.get('bannerCount') or e['bannerCount'] < 4 else e['bannerCount'])],
                'createdAt': {
                    'nanoseconds': 821654000,
                    'seconds': 1688627912
                },
                'metaData': {}
            }
            for i, e in enumerate(input["data"])
        ]
    }