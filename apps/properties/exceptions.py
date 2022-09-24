from rest_framework.exceptions import APIException


class PropertyNotFound(APIException):
    status_code = 404
    default_detail = "The requested property does not exist"


class NotYourProperty(APIException):
    status_code = 403
    default_detail = "You can't edit a property that doesn't belong to you"
