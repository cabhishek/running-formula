export PATH  := node_modules/.bin:$(PATH)

setup:
	brew install pkg-config
	virtualenv .venv && source .venv/bin/activate
	echo "Installing dependancies from requirements.txt"
	.venv/bin/pip install -r requirements.txt

notebook:
	ipython notebook

tests:
	nosetests -w analytics/tests

.PHONY: all setup notebook
