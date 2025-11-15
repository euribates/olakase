#!/usr/bin/env bash

python -Xutf8 ./manage.py dumpdata tasks --indent 4 > tasks/fixtures/tasks.json
