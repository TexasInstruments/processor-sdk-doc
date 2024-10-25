# SPDX-License-Identifier: MIT
# Copyright (C) 2024 Texas Instruments Incorporated - https://www.ti.com

ifeq ($(CONTAINER_TOOL),)
  $(info CONTAINER_TOOL unset, checking if docker is present...)
  ifneq ($(shell which docker 2> /dev/null),)
    $(info Using docker for build...)
    CONTAINER_TOOL := docker
  else ifneq ($(shell which podman 2> /dev/null),)
    $(info Using podman for build...)
    CONTAINER_TOOL := podman
  endif
endif

.PHONY: all setup
all: Dockerfile setup
	$(CONTAINER_TOOL) build . -t texasinstruments/processor-sdk-doc \
		$(BUILD_ARGS)

setup: requirements.txt

requirements.txt:
	cp -ar ../requirements.txt .
