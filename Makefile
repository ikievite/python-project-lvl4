install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

task_manager:
	poetry run gunicorn task_manager.wsgi

run_dev_server:
	poetry run python manage.py runserver

lint:
	poetry run flake8 --exclude .venv

test:
	poetry run pytest --cov=page_loader --cov-report xml tests/	

.PHONY: install build package-install task_manager task_manager_dev lint test
