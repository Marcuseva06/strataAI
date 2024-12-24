#!/usr/bin/env python
# -*- coding: utf-8 -*-

from StrataAI.actions import Action
from StrataAI.schema import Message


class ExecuteTask(Action):
    name: str = "ExecuteTask"
    i_context: list[Message] = []

    async def run(self, *args, **kwargs):
        pass
