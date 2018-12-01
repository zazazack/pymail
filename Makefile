.PHONY clean help test deploy

__init__:
	pipenv check

help:
	@echo "clean	remove temporary files from the current directory."

clean:
	rm -rf ./tmp ./temp ./__pycache__ ./*.egg-info ./build ./dist

test:
	pipenv update
	docker-compose build
	docker-compose up

deploy:
	docker stack deploy -c stack.yml pymail
