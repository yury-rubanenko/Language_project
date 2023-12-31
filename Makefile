MODULE = ~/Language/Language_Project

sort-imports:
	isort $(MODULE)

black-sort:
	black $(MODULE)

flake-lint:
	flake8 $(MODULE) --format=pylint

fixlint: sort-imports black-sort flake-lint