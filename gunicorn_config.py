command = '/home/jariya_pro/venv/bin/gunicorn'
pythonpath = '/home/jariya_pro/jariya'
bind = '127.0.0.1:8003'
workers = 5
user = 'root'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=jariya.settings'

