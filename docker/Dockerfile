# SPDX-License-Identifier: MIT
# Copyright (C) 2024 Texas Instruments Incorporated - https://www.ti.com

FROM debian:stable-slim

RUN apt-get update \
	&& DEBIAN_FRONTEND=noninteractive apt-get install -y \
		--no-install-recommends \
		dumb-init \
		git \
		gosu \
		make \
		python3-pip \
		ripgrep \
		zip \
	&& echo "**** create abc user and make our folders ****" \
	&& useradd -u 1000 -U -d /config -s /bin/false abc \
	&& usermod -G users abc \
	&& mkdir /build && chown abc:abc /build \
	&& mkdir /config && chown abc:abc /config \
	&& echo "**** cleanup ****" \
	&& apt-get autoremove \
	&& apt-get clean \
	&& rm -rf \
		/tmp/* \
		/var/cache/debconf/*-old \
		/var/lib/apt/lists/* \
		/var/lib/dpkg/status-old \
		/var/lib/sgml-base/supercatalog.old \
		/var/log/apt/term.log \
		/var/tmp/*

RUN --mount=type=bind,source=requirements.txt,target=/tmp/requirements.txt \
	python3 -m pip install -r /tmp/requirements.txt --no-cache-dir \
		--break-system-packages

COPY root/ /

WORKDIR /build
VOLUME /build

ENTRYPOINT ["/init"]
CMD ["/bin/bash"]
