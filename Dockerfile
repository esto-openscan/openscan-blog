ARG RUBY_VERSION=3.3
FROM ruby:${RUBY_VERSION}-bookworm

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=${USER_UID}

ENV BUNDLE_PATH=/usr/local/bundle \
    BUNDLE_BIN=/usr/local/bundle/bin \
    GEM_HOME=/usr/local/bundle \
    PATH=/usr/local/bundle/bin:/usr/local/bundle/gems/bin:${PATH}

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
      bash \
      build-essential \
      ca-certificates \
      curl \
      git \
      gosu \
      nodejs \
      npm \
      procps \
    && rm -rf /var/lib/apt/lists/*

RUN git config --system --add safe.directory /workspace

RUN groupadd --gid "${USER_GID}" "${USERNAME}" \
    && useradd --uid "${USER_UID}" --gid "${USER_GID}" --create-home --shell /bin/bash "${USERNAME}" \
    && mkdir -p /workspace "${BUNDLE_PATH}" \
    && chown -R "${USERNAME}:${USERNAME}" /workspace "${BUNDLE_PATH}"

WORKDIR /workspace

EXPOSE 4000 35729

ENTRYPOINT ["bash", "-lc", "HOST_UID=\"$(stat -c '%u' /workspace)\"; HOST_GID=\"$(stat -c '%g' /workspace)\"; groupmod --gid \"${HOST_GID}\" vscode 2>/dev/null || true; usermod --uid \"${HOST_UID}\" --gid \"${HOST_GID}\" vscode 2>/dev/null || true; chown -R \"$(id -u vscode):$(id -g vscode)\" /usr/local/bundle /home/vscode; exec gosu vscode \"$@\"", "entrypoint"]

CMD ["bash", "-lc", "bundle install && exec bundle exec jekyll serve --host 0.0.0.0 --port 4000 --livereload --livereload-port 35729 --drafts"]
