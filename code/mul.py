import functions_framework
from flask import jsonify

@functions_framework.http
def mul(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The sum of the provided numbers
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)

    x = request_json['X']
    y = request_json['Y']
    mul_result = x * y
    result = jsonify({'X': x, 'Y': y, 'Result': mul_result})
    return result
