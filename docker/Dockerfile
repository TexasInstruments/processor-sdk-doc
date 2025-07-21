# SPDX-License-Identifier: MIT
# Copyright (C) 2024 Texas Instruments Incorporated - https://www.ti.com

FROM alpine:3

RUN apk add --no-cache \
		bash \
		diffutils \
		dumb-init \
		git \
		make \
		py3-pip \
		ripgrep \
		shadow \
		su-exec \
		tar \
		vale \
		zip \
	&& echo "**** create abc user and make our folders ****" \
	&& useradd -u 1000 -U -d /config -s /bin/false abc \
	&& usermod -G users abc \
	&& mkdir /build && chown abc:abc /build \
	&& mkdir /config && chown abc:abc /config

RUN --mount=type=bind,source=requirements.txt,target=/tmp/requirements.txt \
	python3 -m pip install -r /tmp/requirements.txt --no-cache-dir \
		--break-system-packages

COPY root/ /

WORKDIR /build
VOLUME /build

ENTRYPOINT ["/init"]
CMD ["/bin/bash"]
