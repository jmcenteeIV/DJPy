from django.http import HttpResponse
from django.template import loader

class MusicView():
    col = 8
    row = 8
    def get_response(self):
        return HttpResponse("Hello, world. You're at the music view page.")

    def index(request):
        title = 'musicbox'
        header_string = 'welcome to the musicbox'
        template = loader.get_template('music/musicbox.html')
        context = {
            'title': title,
            'header_string': header_string,
        }   
        return HttpResponse(template.render(context, request))

    # def time_segment(item):
