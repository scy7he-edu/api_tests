FROM python:3.12-slim

ARG ALLURE_VERSION=2.44.1
ARG WORK_DIR=/usr/src/allure_web

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-21-jre-headless \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -o allure.tgz -L https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/allure-${ALLURE_VERSION}.tgz \
    && tar -zxf allure.tgz -C /opt/ \
    && ln -s /opt/allure-${ALLURE_VERSION}/bin/allure /usr/bin/allure \
    && rm allure.tgz

WORKDIR ${WORK_DIR}

COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

EXPOSE 4040

ENTRYPOINT [ "./entrypoint.sh" ]
