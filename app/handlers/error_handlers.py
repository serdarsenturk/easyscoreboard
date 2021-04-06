import json

def handle_not_found(e):
    response = e.get_response()

    response.data = json.dumps({
        "code": e.code,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response