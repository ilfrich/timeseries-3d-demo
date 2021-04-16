SHELL:=/bin/bash


start:
	python3 runner.py

install:
	pip3 install -r requirements.txt
	npm install

frontend:
	npm run hot-client

build:
	npm run build