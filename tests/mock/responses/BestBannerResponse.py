import time

def BestBannerResponse(input):
    return {
        'result': [
            {
                'id': 'aaaaaaaaaaaaaaaaaaaaaaaaaaa' + str(i),
                'userId': 'zoyqq4zkwdZLiBgH0eyhx4fcN9b2',
                'text': e['text'],
                'plainText': None,
                'title': 'Skyrocket Your Productivity: Unlock Success in Fast-Paced Times\n',
                'style': None,
                'description': "Master the art of time management to thrive in today's rapid world.",
                'resolution': {
                    'width': 1024,
                    'height': 1024
                },
                'banners': [{
                    'id': 'aaaaaaaaaaaaaaaaaaaaaaaaaaa' + str(i),
                    'url': 'https://picsum.photos/1024'
                } for _ in range(4)],
                'createdAt': {
                    'nanoseconds': 821654000,
                    'seconds': 1688627912
                },
                'status': 'SUCCESS',
                'metaData': {}
            }
            for i, e in enumerate(input["data"])
        ]
    }