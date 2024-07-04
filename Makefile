make black:
	black .

make flake:
	flake8 .

make isort:
	isort .

make linters:
	make black
	make isort
	make flake
	
make black-check:
	black --check .

make isort-check:
	isort --check .

make linters-check:
	make black-check
	make isort-check
	make flake


make restart:
	docker-compose down
	docker-compose up