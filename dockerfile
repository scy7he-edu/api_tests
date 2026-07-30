FROM python:3.11-slim

ARG ALLURE_VERSION=2.44.1
ARG WORK_DIR=/usr/src/api_tests

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y  --no-install-recommends \
    openjdk-21-jre-headless \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -o allure.tgz -L https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/allure-${ALLURE_VERSION}.tgz \
    && tar -zxf allure.tgz -C /opt/ \
    && ln -s /opt/allure-${ALLURE_VERSION}/bin/allure /usr/bin/allure \
    && rm allure.tgz

RUN useradd -m -u 1000 runner

WORKDIR ${WORK_DIR}

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 4040

RUN chown -R runner:runner ${WORK_DIR}

USER runner

ENTRYPOINT ["./entrypoint.sh"]
