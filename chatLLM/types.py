#!/usr/bin/env python3

from typing import List, TypedDict, Optional, Literal, Dict, Union
from pydantic.dataclasses import dataclass
from dataclasses_json import dataclass_json

ElementType = Literal["image", "text", "pdf"]
ElementDisplay = Literal["inline", "side", "page"]
ElementSize = Literal["small", "medium", "large"]

@dataclass_json
@dataclass
class AskSpec:
    timeout: int
    type: Literal["text", "file"]

@dataclass_json
@dataclass
class AskFileSpec(AskSpec):
    accept: Union[List[str], Dict[str, List[str]]]
    max_size_mb: int

class AskResponse(TypedDict):
    content: str
    author: str

@dataclass
class AskFileResponse:
    name: str
    path: str
    type: str
    size: int
    content: bytes