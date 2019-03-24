from consts import (
    CONFIG,
    HTTP_STATUS_OK,
    HTTP_STATUS_NOT_IMPLEMENTED,
    HTTP_STATUS_SERVER_ERROR
)


def common(status, messages, additional_info=None):
    return {
        "status": status,
        "data": dict(
            {"messages": messages},
            **({} if additional_info is None else {"additional_information": additional_info})
        )
    }


def handle_service_request(service_name, method_name, param=None, **kwargs):
    try:
        rpc_response = get_rpc_response(service_name, method_name, param, **kwargs)
        http_status = rpc_response.get("status")
        response_body = fix_service_response(rpc_response)
        if not is_service_response_valid(response_body):
            return get_bad_service_response(response_body)
        return get_service_response(http_status, response_body)

    except UnknownService:
        return get_not_implemented_service_response()


# if caller sends `param` not None, assume that service accepts an additional parameter
def get_rpc_response(service_name, method_name, param=None, **kwargs):
    if param is None:
        return get_rpc_service_response(service_name, method_name, **kwargs)
    return get_rpc_service_response(service_name, method_name, param, **kwargs)


def get_rpc_service_response(service_name, method_name, *args, **kwargs):
    with ServiceRpcProxy(service_name, CONFIG) as service:
        method = getattr(service, method_name)
        return method(*args, **kwargs)


def get_not_implemented_service_response():
    return get_service_response(
        HTTP_STATUS_NOT_IMPLEMENTED,
        build_response_body("ERROR",  "Not implemented service",  "Serviço não implementado")
    )


def get_bad_service_response(response):
    return get_service_response(
        HTTP_STATUS_SERVER_ERROR,
        build_response_body(
            "ERROR",
            "Service response not compliant with API standards",
            "Resposta do serviço solicitado fora do padrão da API",
            response,
        )
    )


def get_service_response(http_status, body):
    return {
        "http_status": http_status,
        "body": body,
    }


def is_service_response_valid(response):
    if type(response) != dict:
        return False
    # valid_status = "status" in response and response["status"] in ["OK", "ERROR"]
    valid_data = "data" in response and \
        "messages" in response["data"] and \
        "en" in response["data"]["messages"] and "pt-br" in response["data"]["messages"]
    # return valid_status and valid_data
    return valid_data


def fix_service_response(response):
    if type(response) == str:
        return build_response_body("OK", response, response)
    return response


def build_response_body(status, message_en, message_ptbr, additional_info=None):
    return {
        "status": status,
        "data": dict(
            {"messages": {"en": message_en, "pt-br": message_ptbr}},
            **({} if additional_info is None else {"additional_information": additional_info})
        )
    }
