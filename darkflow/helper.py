import tempfile
import requests
from django.core import files
from rest_framework import status


class Response:
    def __init__(self, result, status):
        self.result = result
        self.status = status


class MusicStyle:
    def __init__(self):
        self.STYLES = [
            ('R', 'Rap'),
            ('HP', 'Hip-hop'),
            ('P', 'Pop'),
            ('C', 'Classical'),
            ('CO', 'Country'),
            ('ED', 'EDM'),
            ('M', 'Metal'),
            ('RB', 'R&B'),
            ('JZ', 'Jazz'),
            ('O', 'Oldies'),
            ('OT', 'Other'),
        ]


def create_file_by_url(file_url, file_field):
    response = requests.get(file_url, stream=True)
    if response.status_code != requests.codes.ok:
        return None

    file_name = file_url.split('/')[-1]
    lf = tempfile.NamedTemporaryFile()

    for block in response.iter_content(1024 * 8):
        if not block:
            break
        lf.write(block)
    file_field.save(file_name, files.File(lf))


def get_object_or_404(Object, serializer, id):
    try:
        obj = Object.objects.get(pk=id)
        srz_data = serializer(obj, many=False)
        res = Response(srz_data.data, status.HTTP_200_OK)
        return res
    except:
        res = Response({'message':'404 error object is not found'}, status.HTTP_404_NOT_FOUND)
        return res


music_style = MusicStyle()