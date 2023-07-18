from flask_swagger_ui import get_swaggerui_blueprint


SWAGGER_URL = '/swagger'
API_URL = 'http://127.0.0.1:8000/swagger1.json'

swaggerui_blueprint = get_swaggerui_blueprint(
  SWAGGER_URL,
  API_URL,
  config={
    'app_name': 'Sample API'
  }
)