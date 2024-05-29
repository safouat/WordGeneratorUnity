from django.shortcuts import render
from openai import OpenAI
import json

from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator






class GetWords(APIView):
    @method_decorator(cache_page(20))
    def get(self, request):
        client = OpenAI(api_key='********************')


        messages = [
    {"role": "system", "content": """
As a helper for children struggling with dyslexia, please provide a JSON  List structure containing the following:


this an exemple of how should the json list format to be follow it but you should change all words on the answer and make it longer as the list grows:
{"words": [
    "cat", "dog", "sun", "run", "ball",
    "cake", "book", "fish", "milk", "tree",
    "house", "happy", "sleep", "apple", "chair",
    "flower", "pencil", "music", "rabbit", "cookie",
    "elephant", "guitar", "pizza", "spider", "butterfly",
    "umbrella", "mountain", "dragon", "fireworks", "telephone",
    "skyscraper", "astronaut", "microscope", "helicopter", "watermelon",
    "whale", "volcano", "telescope", "electricity", "motorcycle",
    "kangaroo", "parachute", "zookeeper", "xylophone", "quicksand",
    "hurricane", "razzmatazz", "rhinoceros", "xylophonist", "jackhammer",
    "abracadabra", "acropolis", "algorithm", "barracuda", "blacksmith",
    "catastrophe", "chocolate", "doppelganger", "flabbergasted", "gobbledygook",
    "haphazardly", "heliocentric", "insurmountable", "juxtaposition", "kleptomaniac",
    "labyrinthine", "mnemonic", "onomatopoeia", "pandemonium", "quintessential",
    "sesquipedalian", "tintinnabulation", "unprecedented", "vexatious", "wunderkind",
    "xenophobic", "yesterday", "zoologically", "aphrodisiac", "bureaucracy",
    "cannibalistic", "dystopian", "eccentricity", "flibbertigibbet", "gastropod",
    "hallucinogenic", "indubitably", "juggernaut", "kaleidoscope", "laconically",
    "magnanimous", "nefarious", "obfuscation", "peregrination", "quixotically",
    "recalcitrant", "serendipity", "transmogrify", "ubiquitous", "verisimilitude"
        ]}

"""},
    {"role": "user", "content": "provide me a json structure of some words from your knowledge to avoid dyslexia.  "}
]

        response = client.chat.completions.create(model="gpt-3.5-turbo",messages=messages)
        print(response.choices[0].message.content)

# Print the generated text
        return Response(json.loads(response.choices[0].message.content))



