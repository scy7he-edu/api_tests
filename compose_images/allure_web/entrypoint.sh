#!/bin/sh

allure generate /allure-results --clean -o /allure-report


exec python3 -m http.server 4040 --bind 0.0.0.0  --directory /allure-report
