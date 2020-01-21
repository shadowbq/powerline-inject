
.PHONY: help
# target: help - Display callable targets
help:
	@egrep "^# target:" [Mm]akefile

.PHONY: clean
# target: clean - Clean all elements except wiping the VIRTENV
clean:
	python3 setup.py clean --dist --eggs --build --pycache

.PHONY: upload
# target: upload - Upload module on PyPi
upload: clean
	python3 setup.py clean --dist
	python3 setup.py sdist bdist_wheel
	twine upload dist/*

.PHONY: install
# target: install - Build and Install it locally only
install: 
	python3 setup.py install
