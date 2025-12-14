ROOT_PATH = poetry_python_template/src

utest:
	@echo "Run unit tests"
	poetry

format:
	@echo "formating"
	poetry run ruff format $(ROOT_PATH)