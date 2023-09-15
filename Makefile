MODULE = ~/Language/Language_Project

sort-imports:
	isort $(MODULE)

black-sort:
	black $(MODULE)

flake-lint:
	flake8 $(MODULE)

sort: sort-imports black-sort flake-lint