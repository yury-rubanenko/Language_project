MODULE = ~/Language/Language_Project

sort-imports:
	isort $(MODULE) 

flake-lint:
	flake8 $(MODULE)

mypy-check:
	mypy $(MODULE)

black-sort:
	black $(MODULE)

sort: sort-imports flake-lint mypy-check black-sort