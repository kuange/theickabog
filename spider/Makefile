GIT_VERSION=$(shell git rev-parse --short HEAD)
DATE_VERSION=$(shell date +%Y%m%d%H%M)
PWD=$(shell pwd)

build:
	echo $(GIT_VERSION)_$(DATE_VERSION) > version.txt
	pipenv run pyinstaller -F -m version.txt main.py
	mv $(PWD)/dist/main $(PWD)/main
	rm -rf $(PWD)/build
	rm -rf $(PWD)/dist
	rm -rf $(PWD)/*.spec

push:
	git add ../
	git commit -am 'update'
	git push