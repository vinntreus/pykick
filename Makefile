clean :
	find . -name '*.pyc' ! -path "./venv/*" -exec rm -f {} \;
