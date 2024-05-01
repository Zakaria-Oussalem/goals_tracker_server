from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Rule, Log
from .serializers import LogSerializer


@api_view(["GET"])
def rule_count(request):
    rule_count = Rule.objects.count()
    return Response({"rule_count": rule_count})


@api_view(["GET"])
def log_list(request):
    logs = Log.objects.all()
    serializer = LogSerializer(logs, many=True)
    return Response(serializer.data)
