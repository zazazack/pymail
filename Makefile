.PHONY clean help

__init__:
	pipenv check
	pipenv lock -r > requirements.txt

help:
	@echo "clean	remove temporary files from the current directory."

clean:
	rm -rf ./tmp ./temp ./__pycache__ ./*.egg-info ./build ./dist
