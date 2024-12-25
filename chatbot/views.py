from django.shortcuts import render

# Create your views here.
# chatbot/views.py
# chatbot/views.py
import json
import os
import random
from django.http import JsonResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def chat(request):
    user_message = request.GET.get('message').lower()
    
    # Load the JSON file
    json_path = os.path.join(os.path.dirname(__file__), 'responses.json')
    with open(json_path, 'r') as f:
        responses = json.load(f)
    
    # Check if user message has a response
    if user_message in responses:
        bot_responses = responses[user_message]
    else:
        bot_responses = responses['default']
    
    # Randomize the response
    bot_response = random.choice(bot_responses)
    
    return JsonResponse({"response": bot_response})
