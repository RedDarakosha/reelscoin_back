#!/bin/bash

sleep 10s

dbmate -u "${POSTGRES_URL}" up

python main.py
