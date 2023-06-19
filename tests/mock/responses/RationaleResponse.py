import time

ProsConsOutput = {
    'pros': {
        'Lorem': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec convallis ipsum est, et iaculis lacus tincidunt eget. Sed dictum diam ex, eget aliquam urna porta a.'
    },
    'cons': {
        'Ipsum': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec convallis ipsum est, et iaculis lacus tincidunt eget. Sed dictum diam ex, eget aliquam urna porta a.'
    },
    'bestChoice': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec convallis ipsum est, et iaculis lacus tincidunt eget. Sed dictum diam ex, eget aliquam urna porta a.',
    'conclusion': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec convallis ipsum est, et iaculis lacus tincidunt eget. Sed dictum diam ex, eget aliquam urna porta a.',
    'confidenceScore': 1
}

SWOTOutput = {
    'strengths': {
        'Lorem': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec convallis ipsum est, et iaculis lacus tincidunt eget. Sed dictum diam ex, eget aliquam urna porta a.'
    },
    'weaknesses': {
        'Ipsum': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec convallis ipsum est, et iaculis lacus tincidunt eget. Sed dictum diam ex, eget aliquam urna porta a.'
    },
    'opportunities': {
        'Dolor': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec convallis ipsum est, et iaculis lacus tincidunt eget. Sed dictum diam ex, eget aliquam urna porta a.'
    },
    'threats': {
        'Sit': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec convallis ipsum est, et iaculis lacus tincidunt eget. Sed dictum diam ex, eget aliquam urna porta a.'
    },
    'bestChoice': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec convallis ipsum est, et iaculis lacus tincidunt eget. Sed dictum diam ex, eget aliquam urna porta a.',
    'conclusion': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec convallis ipsum est, et iaculis lacus tincidunt eget. Sed dictum diam ex, eget aliquam urna porta a.',
    'confidenceScore': 1
}

MultichoiceOutput = {
    'Lorem': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec convallis ipsum est, et iaculis lacus tincidunt eget. Sed dictum diam ex, eget aliquam urna porta a.',
    'Ipsum': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec convallis ipsum est, et iaculis lacus tincidunt eget. Sed dictum diam ex, eget aliquam urna porta a.',
    'Dolor': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec convallis ipsum est, et iaculis lacus tincidunt eget. Sed dictum diam ex, eget aliquam urna porta a.'
}

OutcomesOutput = [
    {
        'children': [],
        'labal': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec convallis ipsum est, et iaculis lacus tincidunt eget. Sed dictum diam ex, eget aliquam urna porta a.',
        'sentiment': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec convallis ipsum est, et iaculis lacus tincidunt eget. Sed dictum diam ex, eget aliquam urna porta a.'
    }
]

def RationaleResponse(input):
    return {
        'result': {
            'result': [
                {
                    'decision': e['decision'],
                    'decisionUserQuery': e['decision'],
                    'writingStyle': e.get('style', 'concise'),
                    'hasUserProfile': False,
                    'analysis': e.get('analysis', 'proscons'),
                    'sourceLang': 'en',
                    'keyResults': SWOTOutput if e.get('analysis') == 'swot' else MultichoiceOutput if e.get('analysis') == 'multichoice' else OutcomesOutput if e.get('analysis') == 'outcomes' else ProsConsOutput,
                    'keyResultsConclusion': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec convallis ipsum est, et iaculis lacus tincidunt eget. Sed dictum diam ex, eget aliquam urna porta a.',
                    'keyResultsBestChoice': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec convallis ipsum est, et iaculis lacus tincidunt eget. Sed dictum diam ex, eget aliquam urna porta a.',
                    'confidence': 1,
                    'createdAt': int(time.time() * 1000),
                    'profileId': None,
                    'isQuality': False,
                    'nonGibberish': False,
                    'id': 'aaaaaaaaaaaaaaaaaaaaaaaaaaa' + str(i)
                }
                for i, e in enumerate(input['data'])
            ]
        }
    }

