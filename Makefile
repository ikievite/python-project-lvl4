install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

task_manager:
	poetry run gunicorn task_manager.wsgi

lint:
	poetry run flake8 page_loader

test:
	poetry run pytest --cov=page_loader --cov-report xml tests/	

.PHONY: install build package-install task_manager lint test
