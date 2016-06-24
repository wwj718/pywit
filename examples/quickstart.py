import sys
from wit import Wit

if len(sys.argv) != 2:
    print('usage: python ' + sys.argv[0] + ' <wit-token>')
    exit(1)
access_token = sys.argv[1]

# Quickstart example
# See https://wit.ai/l5t/Quickstart

def first_entity_value(entities, entity):
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val

def send(request, response):
    print(response['text'])

def merge(request):
    context = request['context']
    entities = request['entities']

    loc = first_entity_value(entities, 'location')
    if loc:
        context['loc'] = loc
    return context

def fetch_weather(request):
    context = request['context']

    context['forecast'] = 'sunny'
    return context

actions = {
    'send': send,
    'merge': merge,
    'fetch-weather': fetch_weather,
}

client = Wit(access_token=access_token, actions=actions)
client.interactive()
