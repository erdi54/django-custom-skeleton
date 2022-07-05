import os
import subprocess
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.conf import settings


@api_view(["POST"])
@permission_classes((AllowAny,))
def git_hook(request):
    try:
        token = request.headers.get('X-Gitlab-Token')
        if token == settings.GIT_WEBHOOK_TOKEN:
            subprocess.Popen(["sh", os.path.join(settings.BASE_DIR, '.refresh.sh')])
            return Response({
                "status": True,
                "message": "Success"
            })
        else:
            return Response({
                "status": False,
                "message": "Invalid Token"
            })

    except Exception as e:
        return Response({
            "status": False,
            "message": str(e)
        })
