import time

DESC = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec convallis ipsum est, et iaculis lacus tincidunt eget. Sed dictum diam ex, eget aliquam urna porta a.'

def SceneXResponse(input):
    return {
        'result': [
            {
                'id': 'aaaaaaaaaaaaaaaaaaaaaaaaaaa' + str(i),
                'image': e['image'],
                'features': e['features'],
                'uid': 'aaaaaaaaaaaaaaaaaaaaaaaaaaa' + str(i),
                'algorithm': e.get('algorithm', 'Aqua'),
                'text': DESC,
                'userId': 'zoyqq4zkwdZLiBgH0eyhx4fcN9b2',
                'createdAt': int(time.time() * 1000),
                'optOut': True if 'opt-out' in e['features'] else False,
                'i18n': {
                    l: DESC[:e['output_length'] if e.get('output_length') else len(DESC)] for l in e.get('languages', ['en'])
                } if e.get('algorithm', 'Aqua') != 'Hearth' else {
                    l: [{
                            'isNarrator': True,
                            'message': DESC[:e['output_length'] if e.get('output_length') else len(DESC)],
                            'name': 'Narrator'
                        },
                        {
                            'isNarrator': False,
                            'message': DESC[:e['output_length'] if e.get('output_length') else len(DESC)],
                            'name': 'BobbyBoy'
                    }] for l in e.get('languages', ['en'])
                },
                'answer': DESC if 'question_answer' in e['features'] else None,
                'tts': {
                    l: f"https://someurl/to/the/{l}/tts/file" for l in e.get('languages', ['en'])
                } if e.get('algorithm', 'Aqua') == 'Hearth' else None,
                'dialog': {
                    'names': ['Narrator', 'BobbyBoy'],
                    'ssml': {
                        l: f"https://someurl/to/the/{l}/ssml/file" for l in e.get('languages', ['en'])
                    }
                } if e.get('algorithm', 'Aqua') == 'Hearth' else None,
            }
            for i, e in enumerate(input["data"])
        ]
    }