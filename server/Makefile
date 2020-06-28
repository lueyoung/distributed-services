ZK_SERVERS=192.168.31.241:2181,192.168.31.242:2181,192.168.31.243:2181
PORT=8080
IMAGE=lowyard/python:3_kazoo
PWD=$(shell pwd)
CMD=/workspace/entrypoint.sh

all: run

test:
	docker run -it --rm -e ZK_SERVERS=$(ZK_SERVERS) -e PORT=${PORT} -v ${PWD}/src:/workspace $(IMAGE) ${CMD} 

run:
	docker $@ -d --rm -e ZK_SERVERS=$(ZK_SERVERS) -e PORT=${PORT} -v ${PWD}/src:/workspace $(IMAGE) ${CMD} 

.PHONY: all run test
