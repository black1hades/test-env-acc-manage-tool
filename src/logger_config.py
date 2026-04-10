# -*- coding: utf-8 -*-
import sys
from pathlib import Path
from loguru import logger

BASE_DIR = Path(__file__).parent.parent
LOG_DIR = BASE_DIR / "log"
LOG_FILE = LOG_DIR / "app.log"


def setup_logger():
    logger.remove()
    
    if not LOG_DIR.exists():
        LOG_DIR.mkdir(parents=True)
    
    logger.add(
        sys.stderr,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>",
        level="DEBUG"
    )
    
    logger.add(
        LOG_FILE,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        level="INFO",
        rotation="10 MB",
        retention="7 days",
        encoding="utf-8"
    )
    
    logger.info("日志系统初始化完成")
    return logger


logger = setup_logger()