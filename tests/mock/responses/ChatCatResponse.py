import time

def ChatCatResponse(input):
    return {
        'chatId': input.get('chatId', 'aaaaaaaaaaaaaaaaaaaaaaaaaaa'),
        'inputMessageId': 'aaaaaaaaaaaaaaaaaaaaaaaaaaa',
        'responseMessageId': 'aaaaaaaaaaaaaaaaaaaaaaaaaaa',
        'responseContent': '-'.join([message['content'] for message in input['messages']]),
        'usage': {
            'inputTokenCount': 1,
            'responseTokenCount': 5
        }
    }
