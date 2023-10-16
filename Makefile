format:
	black *.py

lint:
	pylint --disable=R,C *.py
