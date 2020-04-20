#!/bin/bash
	source /home/jariya_pro/venv/bin/activate
	source /home/jariya_pro/venv/bin/postactivate
	exec gunicorn  -c "/home/jariya_pro/jariya/gunicorn_config.py" jariya.wsgi


