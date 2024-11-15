from django.shortcuts import render
import os
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from .domains.image_data import image_data


def LandingPage(request):
    return  render(request, "landingPage/landingPage.html")


from django.shortcuts import render
import base64

def saveImage(request):
    if request.method == 'POST' and request.FILES['image']:
        # Get the uploaded image from the request
        uploaded_image = request.FILES['image']
        
        # Define a path to store the image
        image_name = uploaded_image.name  # Get the image name
        image_path = os.path.join(settings.MEDIA_ROOT, image_name)  # Construct the full file path
        
        # Save the image to the local file system
        with open(image_path, 'wb') as image_file:
            for chunk in uploaded_image.chunks():
                image_file.write(chunk)
        
        # Convert image to Base64
        with open(image_path, 'rb') as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')
        
        # Store the file path and image name in MongoDB
        image_data_ins = image_data(image_path=image_path, image_name=image_name)
        image_data_ins.save()

        # Render the HTML page
        return render(request, 'imageDisplay/image_display.html', {
            'image_url': f'/images/{image_name}',  # Assuming MEDIA_URL is set up
            'base64_image': f"data:image/{image_name.split('.')[-1]};base64,{base64_image}"
        })

    
    return JsonResponse({'status': 'error', 'message': 'No image uploaded'}, status=400)