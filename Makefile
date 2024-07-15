VERSION=$(shell cat version)
ARTIFACT=python-playground
REPO=rodrigorootrj/service
TAG=${REPO}:${ARTIFACT}-${VERSION}
LABEL=playground
DIR=$(shell pwd -P)

echo:
	@echo ${TAG}
	@echo ${LABEL}
build:
	@docker build . -t ${TAG}
shell:
	@docker run -it --rm --name ${LABEL} --mount type=bind,source=${DIR}/src,target=/app/ --entrypoint /bin/bash ${TAG}
## debug
compose:
	@docker-compose up	