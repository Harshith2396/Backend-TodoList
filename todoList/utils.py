from rest_framework_jwt.utils import jwt_decode_handler
def getEmail(request):
    tokens=request.META.get('HTTP_AUTHORIZATION','').split()[1]
    payload=jwt_decode_handler(tokens)
    return payload['user_id']