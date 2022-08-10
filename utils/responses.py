def success_response(msg, status: int, data=None) -> dict:
    response = {
        "status": status,
        "success": True,
        "msg": msg
    }
    
    if data:
        response['data'] = data
    return response


def fail_response(msg, status: int, data=None) -> dict:
    response = {
        "status": status,
        "success": False,
        "msg": msg
    }
    
    if data:
        response['data'] = data
    return response
