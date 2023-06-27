import time

def JinaChatResponse(input):
    return {
        'chatId': input.get('chatId', 'aaaaaaaaaaaaaaaaaaaaaaaaaaa'),
        'inputMessageId': 'aaaaaaaaaaaaaaaaaaaaaaaaaaa',
        'responseMessageId': 'aaaaaaaaaaaaaaaaaaaaaaaaaaa',
        'choices': [{
            'index': 0,
            'message': {
                'role': 'assistant',
                'content': '-'.join([message['content'] for message in input['messages']])
            },
            'finish_reason': 'stop'
        }],
        'usage': {
            'prompt_tokens': 7,
            'completion_tokens': 18,
            'total_tokens': 25
        }
    }
