# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QApplication, QMessageBox, QInputDialog
from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices

from data_store import load_data, save_data, get_note_files, load_note, save_note, DEFAULT_CARDS
from logger_config import logger


class AppController:
    def __init__(self):
        self.data = load_data()
        self.current_env_index = 0
        self.current_account_index = 0
        self.current_card_index = 0
        self.current_note = "note.txt"
        self.is_top = False
        logger.info("应用控制器初始化完成")
    
    def get_environments(self) -> list:
        return [env["name"] for env in self.data.get("environments", [])]
    
    def get_accounts(self) -> list:
        env = self.data["environments"][self.current_env_index]
        return [acc["name"] for acc in env["accounts"]]
    
    def get_cards(self) -> list:
        return [card["title"] for card in self.data.get("cards", [])]
    
    def get_notes(self) -> list:
        return get_note_files()
    
    def get_current_env_data(self) -> dict:
        env = self.data["environments"][self.current_env_index]
        acc = env["accounts"][self.current_account_index]
        return {
            "env_name": env["name"],
            "account_name": acc["name"],
            "host": acc["host"],
            "account": acc["account"],
            "password": acc["password"]
        }
    
    def get_current_card_data(self) -> dict:
        return self.data["cards"][self.current_card_index]
    
    def set_env_index(self, index: int):
        self.current_env_index = index
        self.current_account_index = 0
        logger.info(f"切换环境: {self.get_environments()[index]}")
    
    def set_account_index(self, index: int):
        self.current_account_index = index
        logger.info(f"切换账号: {self.get_accounts()[index]}")
    
    def set_card_index(self, index: int):
        self.current_card_index = index
        logger.info(f"切换名片: {self.get_cards()[index]}")
    
    def save_env_data(self, host: str, account: str, password: str):
        env = self.data["environments"][self.current_env_index]
        acc = env["accounts"][self.current_account_index]
        acc["host"] = host
        acc["account"] = account
        acc["password"] = password
        save_data(self.data)
        logger.info(f"保存环境账号: {env['name']} - {acc['name']}")
    
    def add_new_account(self, account_name: str, host: str):
        env = self.data["environments"][self.current_env_index]
        env["accounts"].append({
            "name": account_name,
            "host": host,
            "account": "",
            "password": ""
        })
        save_data(self.data)
        self.current_account_index = len(env["accounts"]) - 1
        logger.info(f"新增账户: {env['name']} - {account_name}")
        return True
    
    def save_env_name(self, new_name: str, new_account_name: str):
        if not new_name or not new_account_name:
            QMessageBox.warning(None, "警告", "环境名称和账号名称不能为空")
            return False
        
        old_env_name = self.data["environments"][self.current_env_index]["name"]
        old_account_name = self.data["environments"][self.current_env_index]["accounts"][self.current_account_index]["name"]
        
        if new_name != old_env_name:
            for env in self.data["environments"]:
                if env["name"] == new_name:
                    QMessageBox.warning(None, "警告", "环境名称已存在")
                    return False
            self.data["environments"][self.current_env_index]["name"] = new_name
            logger.info(f"更新环境名称: {old_env_name} -> {new_name}")
        
        if new_account_name != old_account_name:
            self.data["environments"][self.current_env_index]["accounts"][self.current_account_index]["name"] = new_account_name
            logger.info(f"更新账号名称: {old_account_name} -> {new_account_name}")
        
        save_data(self.data)
        return True
    
    def save_card_title(self, new_title: str):
        if not new_title:
            QMessageBox.warning(None, "警告", "名片标题不能为空")
            return False
        
        old_title = self.data["cards"][self.current_card_index]["title"]
        
        if new_title != old_title:
            for card in self.data["cards"]:
                if card["title"] == new_title:
                    QMessageBox.warning(None, "警告", "名片标题已存在")
                    return False
            self.data["cards"][self.current_card_index]["title"] = new_title
            logger.info(f"更新名片标题: {old_title} -> {new_title}")
            save_data(self.data)
        return True
    
    def add_new_env(self):
        name, ok = QInputDialog.getText(None, "新增环境", "请输入环境名称:")
        if ok and name:
            self.data["environments"].append({
                "name": name,
                "accounts": [{"name": "admin", "host": "", "account": "", "password": ""}]
            })
            save_data(self.data)
            logger.info(f"新增环境: {name}")
            return True
        return False
    
    def delete_current_env(self):
        if len(self.data["environments"]) <= 1:
            QMessageBox.warning(None, "警告", "至少保留一个环境")
            return False
        
        env_name = self.data["environments"][self.current_env_index]["name"]
        reply = QMessageBox.question(
            None, "确认", f"确定要删除环境 '{env_name}' 吗?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            del self.data["environments"][self.current_env_index]
            self.current_env_index = max(0, self.current_env_index - 1)
            save_data(self.data)
            logger.info(f"删除环境: {env_name}")
            return True
        return False
    
    def save_card_data(self, title: str, content: str):
        card = self.data["cards"][self.current_card_index]
        card["title"] = title
        card["content"] = content
        save_data(self.data)
        logger.info(f"保存名片: {title}")
    
    def add_new_card(self):
        title, ok = QInputDialog.getText(None, "新增名片", "请输入名片标题:")
        if ok and title:
            self.data["cards"].append({
                "title": title,
                "content": ""
            })
            save_data(self.data)
            logger.info(f"新增名片: {title}")
            return True
        return False
    
    def delete_current_card(self):
        if self.current_card_index < len(DEFAULT_CARDS):
            QMessageBox.warning(None, "警告", "默认名片不能删除")
            return False
        
        card_title = self.data["cards"][self.current_card_index]["title"]
        reply = QMessageBox.question(
            None, "确认", f"确定要删除名片 '{card_title}' 吗?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            del self.data["cards"][self.current_card_index]
            self.current_card_index = max(0, self.current_card_index - 1)
            save_data(self.data)
            logger.info(f"删除名片: {card_title}")
            return True
        return False
    
    def open_card_url(self):
        card = self.data["cards"][self.current_card_index]
        url = QUrl(card["content"])
        if url.isValid():
            QDesktopServices.openUrl(url)
            logger.info(f"打开链接: {card['content']}")
        else:
            QMessageBox.warning(None, "警告", "无效的链接地址")
    
    def get_note_content(self) -> str:
        return load_note(self.current_note)
    
    def save_note_content(self, content: str):
        save_note(self.current_note, content)
        logger.info(f"保存笔记: {self.current_note}")
    
    def switch_note(self, filename: str):
        self.current_note = filename
        logger.info(f"切换笔记: {filename}")
    
    def add_new_note(self):
        name, ok = QInputDialog.getText(None, "新增笔记", "请输入笔记文件名:")
        if ok and name:
            if not name.endswith(".txt"):
                name += ".txt"
            save_note(name, "")
            logger.info(f"新增笔记: {name}")
            return True
        return False
    
    def copy_to_clipboard(self, text: str):
        clipboard = QApplication.clipboard()
        clipboard.setText(text)
        logger.debug(f"复制到剪贴板: {text[:20]}...")