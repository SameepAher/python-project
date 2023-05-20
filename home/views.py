from django.shortcuts import render, HttpResponse
# import openai
# from .secret_key import API_KEY

# openai.api_key = API_KEY

# Create your views here.
def index(request):
    # output = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {
    #             "role": "user",
    #             "content": "How delete photos from phone gallery"
    #         }
    #     ]
    # )
    # context = {
    #     "output": output,
    # }
    return render(request, 'index.html')

def about(index):
    return HttpResponse("This is about")