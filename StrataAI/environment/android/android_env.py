#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pydantic import Field

from StrataAI.environment.android.android_ext_env import AndroidExtEnv
from StrataAI.environment.base_env import Environment


class AndroidEnv(AndroidExtEnv, Environment):
    """in order to use actual `reset`&`observe`, inherited order: AndroidExtEnv, Environment"""

    rows: int = Field(default=0, description="rows of a grid on the screenshot")
    cols: int = Field(default=0, description="cols of a grid on the screenshot")
