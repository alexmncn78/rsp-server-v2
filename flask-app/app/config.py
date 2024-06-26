"""Application configuration."""

from environs import Env

env = Env()
env.read_env()


HOSTNAME = env.str("HOSTNAME")

SECRET_KEY = env.str("SECRET_KEY")

JWT_SECRET_KEY = env.str("JWT_SECRET_KEY")

SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'


SQLALCHEMY_DATABASE_URI = env.str("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = False

ACCESS_LOG_DATABASE_URI = env.str("ACCESS_LOG_DATABASE_URI")


PC_ON_ROUTE = env.str("PC_ON_ROUTE")


PUSHOVER_APP_TOKEN = env.str("PUSHOVER_APP_TOKEN")
PUSHOVER_USER_KEY = env.str("PUSHOVER_USER_KEY")
PUSHOVER_EXCEPTIONS = env.str("PUSHOVER_EXCEPTIONS")


ESP32_PC_ON_KEY = env.str("ESP32_PC_ON_KEY")


THINKSPEAK_API_KEY = env.str("THINKSPEAK_API_KEY")


class MQTT_Service:
    HOST = env.str("MQTT_HOST")
    PORT = env.int("MQTT_PORT")
    CA_CERTIFICATE = env.str("MQTT_CA_CERTIFICATE")
    CLIENT_ID = env.str("MQTT_CLIENT_ID")
    TOPIC = env.str("MQTT_TOPIC")
    
    
class NOIP_DNS:
    URL = env.str("NOIP_DNS_URL")
    HOSTNAME = HOSTNAME
    USERNAME = env.str("NOIP_DNS_USERNAME")
    PASSWORD = env.str("NOIP_DNS_PASSWORD")