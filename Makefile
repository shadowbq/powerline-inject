test-upload:
	python3 setup.py sdist upload -r pypitest

upload:
	python3 setup.py sdist upload -r pypi

install: 
	python3 setup.py install

clean:
	python3 setup.py clean --dist --eggs --build --pycache