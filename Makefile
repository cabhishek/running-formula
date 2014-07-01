export PATH  := node_modules/.bin:$(PATH)

setup:
	brew install pkg-config
	virtualenv .venv && source .venv/bin/activate
	echo "Installing dependancies from requirements.txt"
	.venv/bin/pip install -r requirements.txt
	echo "Installing npm dependancies from package.json"
	npm install

tests:
	nosetests -w analytics/tests

.PHONY: all setup
