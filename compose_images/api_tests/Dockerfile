FROM python:3.12-slim

ARG WORK_DIR=/usr/src/api_tests

ENV PYTHONUNBUFFERED=1

RUN useradd -m -u 1000 runner && \
    mkdir -p ${WORK_DIR}/allure-results && \
    chown -R runner:runner ${WORK_DIR}

WORKDIR ${WORK_DIR}

COPY --chown=runner:runner requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=runner:runner . .

RUN chmod +x ./entrypoint.sh

USER runner

ENTRYPOINT ["./entrypoint.sh"]
