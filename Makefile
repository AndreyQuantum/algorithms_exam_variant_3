ROOT_PATH = algorithms_exam/src

utest:
	@echo "Run unit tests"
	poetry run pytest algorithms_exam/tests

format:
	@echo "formating"
	poetry run ruff format $(ROOT_PATH)

lint:
	@echo "check PEP8"
	poetry run ruff check .

run:
	@echo "run algorithm"
	python3 $(ROOT_PATH)/main.py