#!/usr/bin/env bash

find StrataAI | grep "\.py" | grep -Ev "(__init__|pyc)" | xargs grep -E "(^class| def )" 2>/dev/null | grep -v -E "(grep|tests|examples)"