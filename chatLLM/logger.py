#!/usr/bin/env python3

import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)

logging.getLogger("socketio").setLevel(logging.ERROR)
logging.getLogger("engineio").setLevel(logging.ERROR)
logging.getLogger("geventwebsocket.handler").setLevel(logging.ERROR)
logging.getLogger("numexpr").setLevel(logging.ERROR)

logger = logging.getLogger("chatllm")