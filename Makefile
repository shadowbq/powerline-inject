
.PHONY: help
# target: help - Display callable targets
help:
	@egrep "^# target:" [Mm]akefile

.PHONY: clean
# target: clean - Clean all elements except wiping the VIRTENV
clean:
	python3 setup.py clean --dist --eggs --build --pycache

.PHONY: register
# target: register - Register module on PyPi
register:
	python3 setup.py register

.PHONY: upload
# target: upload - Upload module on PyPi
upload: clean
	python3 setup.py clean --dist
	python3 setup.py sdist bdist_wheel
	twine upload dist/*

.PHONY: test-upload
# target: test-upload - Upload module on PyPitest (deprecated)
test-upload:
	python3 setup.py sdist upload -r pypitest

.PHONY: install
# target: install - Build and Install it locally only
install: 
	python3 setup.py install
