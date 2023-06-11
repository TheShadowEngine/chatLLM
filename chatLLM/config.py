#!/usr/bin/env python3

import os
import sys
import tomli

from typing import Optional, Any, Callable, List, Dict, TYPE_CHECKING
from pydantic.dataclasses import dataclass
from importlib import machinery
from chatLLM.logger import logger

if TYPE_CHECKING:
    from chatLLM.action import Action

root = os.getcwd()

@dataclass()
class ChainlitConfig:
    chatllm_server: str
    chatbot_name: str
    description: str
    public: bool
    enable_telemetry: bool
    user_env: List[str]
    hide_cot: bool
    lc_cache_path: str
    action_callbacks: Dict[str, Callable[["Action"], Any]]
    root = root
    github: Optional[str] = None

def init_config(log=False):
    if not os.path.exists(config_file):
        os.makedirs(config_dir, exist_ok=True)
        with open(config_file, "w", encoding="utf-8") as f:
            f.write(DEFAULT_CONFIG_STR)
            logger.info(f"Created default config file {config_file}")
    elif log:
        logger.info(f"Config file already exists: {config_file}")

def reset_module_config():
    if not config:
        return
    
    module_files = [
        "on_stop",
        "on_chat_server",
        "on_message",
        "lc_run"
    ]