from rest_framework.exceptions import NotAcceptable

def get_query_param_filters(request):
    """
    Filter by query params
    """

    filters = {}
    for param in request.query_params.keys():
        try:
            filters[param] = request.query_params[param]
        except Exception as e:
            raise NotAcceptable(detail='{0} - {1}'.format(param, e))
    return filters