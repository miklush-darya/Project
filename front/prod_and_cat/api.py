
from flask import session
import requests

from config import Config
# from app.utils import check_response_errors


CURRENT_USER_URL = f"{Config.API_URL}/products/"
CREATE_USER_URL = f"{Config.API_URL}/category/"