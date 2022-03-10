install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black scripts/*.py main.py app.py

lint:
	pylint --disable=R,C scripts/*.py main.py app.py

clean: format lint
all: install format lint
ci: format lint
