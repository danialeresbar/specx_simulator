qt-designer:
	poetry run pyside6-designer

install-dependencies:
	poetry install

shell:
	poetry shell

run:
	poetry run python -m main

coverage-tests:
	poetry run coverage run -m unittest discover tests --verbose --failfast

coverage-pattern:
	poetry run coverage run -m unittest discover tests -p "test_*$(pattern).py" --failfast

coverage-report:
	poetry run coverage report

coverage-html:
	poetry run coverage html

coverage: coverage-tests coverage-report coverage-html
