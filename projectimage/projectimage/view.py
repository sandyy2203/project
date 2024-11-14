from django.shortcuts import render

def LandingPage(request):
    return  render(request, "landingPage/landingPage.html")


def saveImage(request):
    return "Hi"