from rest_framework.response import Response


def restResponse(code, msg, data, status):
    rest_data = {
        'code': code,
        'msg': msg,
        'data': data
    }
    return Response(rest_data, status)
