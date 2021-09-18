from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Search
from .serializers import SearchSerializer


class SearchView(APIView):
    
    def get(self, request):
        keyword = request.query_params.get('keyword')
        search = Search(keyword)
        result = search.search_engine()
        serializer = SearchSerializer(result, many=False)
        return Response(serializer.data)
