#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum

from StrataAI.actions.action import Action
from StrataAI.actions.action_output import ActionOutput
from StrataAI.actions.add_requirement import UserRequirement
from StrataAI.actions.debug_error import DebugError
from StrataAI.actions.design_api import WriteDesign
from StrataAI.actions.design_api_review import DesignReview
from StrataAI.actions.project_management import WriteTasks
from StrataAI.actions.research import CollectLinks, WebBrowseAndSummarize, ConductResearch
from StrataAI.actions.run_code import RunCode
from StrataAI.actions.search_and_summarize import SearchAndSummarize
from StrataAI.actions.write_code import WriteCode
from StrataAI.actions.write_code_review import WriteCodeReview
from StrataAI.actions.write_prd import WritePRD
from StrataAI.actions.write_prd_review import WritePRDReview
from StrataAI.actions.write_test import WriteTest
from StrataAI.actions.di.execute_nb_code import ExecuteNbCode
from StrataAI.actions.di.write_analysis_code import WriteAnalysisCode
from StrataAI.actions.di.write_plan import WritePlan


class ActionType(Enum):
    """All types of Actions, used for indexing."""

    ADD_REQUIREMENT = UserRequirement
    WRITE_PRD = WritePRD
    WRITE_PRD_REVIEW = WritePRDReview
    WRITE_DESIGN = WriteDesign
    DESIGN_REVIEW = DesignReview
    WRTIE_CODE = WriteCode
    WRITE_CODE_REVIEW = WriteCodeReview
    WRITE_TEST = WriteTest
    RUN_CODE = RunCode
    DEBUG_ERROR = DebugError
    WRITE_TASKS = WriteTasks
    SEARCH_AND_SUMMARIZE = SearchAndSummarize
    COLLECT_LINKS = CollectLinks
    WEB_BROWSE_AND_SUMMARIZE = WebBrowseAndSummarize
    CONDUCT_RESEARCH = ConductResearch
    EXECUTE_NB_CODE = ExecuteNbCode
    WRITE_ANALYSIS_CODE = WriteAnalysisCode
    WRITE_PLAN = WritePlan


__all__ = [
    "ActionType",
    "Action",
    "ActionOutput",
]
