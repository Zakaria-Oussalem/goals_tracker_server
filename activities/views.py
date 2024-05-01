from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Rule, Log
from .serializers import LogSerializer


@api_view(["GET"])
def get_rules(request):
    rules = Rule.objects.all()
    rules_dict = {
        rule.name.name: {"reward": rule.reward, "punishment": rule.punishment}
        for rule in rules
    }
    return Response({"rules": rules_dict})


@api_view(["GET"])
def log_list(request):
    logs = Log.objects.all()
    serializer = LogSerializer(logs, many=True)
    return Response(serializer.data)
