from dstr_common_lib import responses
from dstr_common_lib.consts import HTTP_STATUS_OK, HTTP_STATUS_ERROR


class CommonMixin(object):
    def common_health_check(self, additional_info={}):
        return responses.common(
            HTTP_STATUS_OK,
            {
                "en": "Service is healthy",
                "pt-br": "O serviço está saudável"
            },
            additional_info
        )
