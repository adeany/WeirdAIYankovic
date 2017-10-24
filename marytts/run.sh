#!/bin/bash

echo "run"
./gradlew run

sleep 5 & python txt2wav.py

wait

echo "done"

