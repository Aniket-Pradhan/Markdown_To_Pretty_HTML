build:
	python setup.py build

install:
	pip install .

make all:
	pip install .
	rm -rf *egg* build/ dist/

remove:
	python -m pip uninstall beautdown

clean:
	rm -rf *egg* build/ dist/
