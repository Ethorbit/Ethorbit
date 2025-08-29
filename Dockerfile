FROM python:3.11 AS github-readme-terminal

ARG UID=1000
ARG GID=1000

RUN apt update -y &&\
    apt install -y ffmpeg &&\
    groupadd -g "${GID}" python &&\
    useradd -g python -u "${UID}" python &&\
    python -m pip install --upgrade github-readme-terminal &&\
    mkdir -p /home/python/.config/gifos &&\
    chown -R python:python /home/python/

WORKDIR /home/python


FROM github-readme-terminal AS my-awesome-readme

ARG FIRACODE_URL="https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/FiraCode.zip"

RUN curl -L "${FIRACODE_URL}" -o /tmp/firacode.zip && \
    unzip /tmp/firacode.zip -d /tmp/firacode_extracted && \
    mkdir -p /usr/share/fonts/opentype &&\
    install -Dm644 /tmp/firacode_extracted/*.ttf -t /usr/share/fonts/truetype

COPY --chown=python:python --chmod=0755 ./src src
COPY --chown=python:python --chmod=0755 ./config .config/gifos
USER python
ENTRYPOINT [ "python" ]
CMD [ "src/main.py" ]
