#!/bin/sh

pytest "$@"
RC=$?

if [ "$SERVE_REPORT" = "1" ]; then
    allure generate allure-results -o allure-report --clean
    exec python -m http.server 4040 --bind 0.0.0.0 --directory allure-report
fi

exit $RC
