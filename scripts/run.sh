#!/bin/bash

sleep 10s

dbmate -u "${POSTGRES_URL}" up

echo "${POSTGRES_URL}"
echo "zxc"

python main.py