# common constants
import os


HTTP_STATUS_OK = 200
HTTP_STATUS_ERROR = 400
HTTP_STATUS_SERVER_ERROR = 500
HTTP_STATUS_NOT_IMPLEMENTED = 501

RABBIT_USER = os.environ.get("RABBIT_USER", "guest")
RABBIT_PASSWORD = os.environ.get("RABBIT_PASSWORD", "guest")
RABBIT_HOST = os.environ.get("RABBIT_HOST", "localhost")
RABBIT_PORT = os.environ.get("RABBIT_PORT", "5672")


AMQP_URI = "amqp://{username}:{password}@{host}:{port}".format(
    username=RABBIT_USER,
    password=RABBIT_PASSWORD,
    host=RABBIT_HOST,
    port=RABBIT_PORT,
)
CONFIG = {"AMQP_URI": AMQP_URI}
