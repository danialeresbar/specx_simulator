shell:
	poetry shell

coverage-tests:
	poetry run coverage run -m unittest discover tests --failfast

coverage-pattern:
	poetry run coverage run -m unittest discover tests -p "test_*$(pattern).py" --failfast

coverage-report:
	poetry run coverage report

coverage-html:
	poetry run coverage html

coverage: coverage-tests coverage-report coverage-html
