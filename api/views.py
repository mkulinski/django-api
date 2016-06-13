from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer


# Setup as a class based-view
# available at stocks/
class StockList(APIView):
    # returns all stocks when they submit a get request
    def get(self, request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)

    # creates a new stock with a  post request
    def post(self):
        pass
