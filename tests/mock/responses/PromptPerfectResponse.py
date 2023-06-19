import time

def PromptPerfectResponse(input):
    return {
        'result': [
            {
                'prompt': e.get('prompt') or e.get('imagePrompt') or '',
                'imagePrompt': e.get('imagePrompt') or None,
                'targetModel': e['targetModel'],
                'features': e['features'],
                'iterations': e.get('iterations', 1),
                'previewSettings': e.get('previewSettings', {}),
                'previewVariables': e.get('previewVariables', {}),
                'timeout': e.get('timeout', 20000),
                'targetLanguage': e.get('target_language'),
                'promptOptimized': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec convallis ipsum est, et iaculis lacus tincidunt eget. Sed dictum diam ex, eget aliquam urna porta a.',
                'credits': 1,
                'language': e.get('target_language', 'en'),
                'intermediateResults': [{
                    'promptOptimized': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec convallis ipsum est, et iaculis lacus tincidunt eget. Sed dictum diam ex, eget aliquam urna porta a.',
                    'explain': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec convallis ipsum est, et iaculis lacus tincidunt eget. Sed dictum diam ex, eget aliquam urna porta a.'
                }],
                'explain': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec convallis ipsum est, et iaculis lacus tincidunt eget. Sed dictum diam ex, eget aliquam urna porta a.',
                'createdAt': int(time.time() * 1000),
                'userId': 'zoyqq4zkwdZLiBgH0eyhx4fcN9b2',
                'id': 'aaaaaaaaaaaaaaaaaaaaaaaaaaa' + str(i)
            }
            for i, e in enumerate(input["data"])
        ]
    }