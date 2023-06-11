#!/usr/bin/env python3

from typing import Any
from chatLLM.types import LLMSettings
from typing import List, Optional

def run_langchain_agent(agent: Any, input_str: str):
    if hasattr(agent, "input_keys"):
        input_key = agent.input_keys[0]
        raw_res = agent({input_key: input_str})
    else:
        raw_res = agent(input_str)
    
    if hasattr(agent, "output_keys"):
        output_key = agent.output_keys[0]
    else:
        output_key = None

    return raw_res, output_key