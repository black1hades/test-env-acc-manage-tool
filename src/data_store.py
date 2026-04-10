# -*- coding: utf-8 -*-
import json
import os
from pathlib import Path
from loguru import logger

BASE_DIR = Path(__file__).parent.parent
CONF_DIR = BASE_DIR / "conf"
DATA_FILE = CONF_DIR / "data.json"
NOTES_DIR = BASE_DIR / "notes"

DEFAULT_ENVIRONMENTS = [
    {"name": "dev", "accounts": [{"name": "admin", "host": "http://dev.example.com", "account": "admin", "password": "123456"}]},
    {"name": "test", "accounts": [{"name": "admin", "host": "http://test.example.com", "account": "admin", "password": "123456"}]},
    {"name": "staging", "accounts": [{"name": "admin", "host": "http://staging.example.com", "account": "admin", "password": "123456"}]}
]

DEFAULT_CARDS = [
    {"title": "测试数据生成", "content": "https://www.mockaroo.com/"},
    {"title": "测试文件生成", "content": "https://samplelib.com/zh/"}
]


def ensure_directories():
    if not NOTES_DIR.exists():
        NOTES_DIR.mkdir(parents=True)
        logger.info(f"创建笔记目录: {NOTES_DIR}")
    if not CONF_DIR.exists():
        CONF_DIR.mkdir(parents=True)
        logger.info(f"创建配置目录: {CONF_DIR}")


def load_data() -> dict:
    ensure_directories()
    if not DATA_FILE.exists():
        save_data({
            "environments": DEFAULT_ENVIRONMENTS,
            "cards": DEFAULT_CARDS
        })
        logger.info("数据文件不存在，已创建默认数据")
        return load_data()
    
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            logger.debug("数据加载成功")
            return data
    except Exception as e:
        logger.error(f"加载数据失败: {e}")
        return {"environments": DEFAULT_ENVIRONMENTS, "cards": DEFAULT_CARDS}


def save_data(data: dict):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        logger.info("数据保存成功")
    except Exception as e:
        logger.error(f"保存数据失败: {e}")


def get_note_files() -> list:
    ensure_directories()
    notes = []
    for f in NOTES_DIR.glob("*.txt"):
        notes.append(f.name)
    logger.debug(f"获取笔记文件列表: {notes}")
    return sorted(notes)


def load_note(filename: str) -> str:
    note_path = NOTES_DIR / filename
    if note_path.exists():
        try:
            with open(note_path, "r", encoding="utf-8") as f:
                content = f.read()
                logger.debug(f"加载笔记: {filename}")
                return content
        except Exception as e:
            logger.error(f"加载笔记失败 {filename}: {e}")
            return ""
    return ""


def save_note(filename: str, content: str):
    note_path = NOTES_DIR / filename
    try:
        with open(note_path, "w", encoding="utf-8") as f:
            f.write(content)
        logger.info(f"保存笔记: {filename}")
    except Exception as e:
        logger.error(f"保存笔记失败 {filename}: {e}")