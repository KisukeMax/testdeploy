from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse , JsonResponse
import os
from django.conf import settings
import json



@csrf_exempt
def whatsAppWebhook(request):
    target_directory = os.path.join(settings.BASE_DIR, 'static', 'your_target_directory')

        # Ensure the target directory exists, creating it if necessary
    os.makedirs(target_directory, exist_ok=True)

    # Define the target file path
    target_file_path = os.path.join(target_directory, 'your_filename.txt')

    # Copy or move the source data to the target file
    with open(target_file_path, 'ab') as target_file:
        target_file.write(request.body)
    if request.method == 'GET':
        # print(request.GET)  # Debugging line to check request.GET contents
        VERIFY_TOKEN = "a36563b3-800a-43ec-ad4a-7043005b488c"
        mode = request.GET.get('hub.mode', '')
        token = request.GET.get('hub.verify_token', '')
        challenge = request.GET.get('hub.challenge', '')
        # sendWhatsAppMessage("9956929372", "get auisas")

        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return HttpResponse(challenge, status=200)
        else:   
            return HttpResponse('error', status=403)

    if request.method == 'POST':
        print("data recvd")
        # data = json.loads(request.body)
        target_directory = os.path.join(settings.BASE_DIR, 'static', 'your_target_directory')

        # Ensure the target directory exists, creating it if necessary
        os.makedirs(target_directory, exist_ok=True)

        # Define the target file path
        target_file_path = os.path.join(target_directory, 'your_filename.txt')

        # Copy or move the source data to the target file
        with open(target_file_path, 'ab') as target_file:
            target_file.write(request.body)


        return HttpResponse('success', status=200)


