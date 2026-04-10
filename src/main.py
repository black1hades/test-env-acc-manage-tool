# -*- coding: utf-8 -*-
import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from loguru import logger
from PySide6.QtWidgets import QApplication, QWidget, QInputDialog, QFileDialog
from PySide6.QtCore import Qt, QTimer

from ui_mainwindow import Ui_Form
from app_controller import AppController
from logger_config import setup_logger


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.controller = AppController()
        self.is_top = False
        
        self.init_ui()
        self.connect_signals()
        
        self.setFocus()
        logger.info("主窗口初始化完成")
    
    def init_ui(self):
        self.load_environments()
        self.load_accounts()
        self.load_cards()
        self.load_notes()
        self.load_env_details()
        self.load_card_details()
        self.load_note_content()
    
    def connect_signals(self):
        self.ui.comboBox_env.currentIndexChanged.connect(self.on_env_changed)
        self.ui.comboBox_account.currentIndexChanged.connect(self.on_account_changed)
        
        self.ui.pushButton_host_copy.clicked.connect(self.on_copy_host)
        self.ui.pushButton_account_copy.clicked.connect(self.on_copy_account)
        self.ui.pushButton_possword_copy.clicked.connect(self.on_copy_password)
        self.ui.pushButton_manage_save.clicked.connect(self.on_save_env)
        self.ui.pushButton_manage_new.clicked.connect(self.on_new_env)
        self.ui.pushButton_manage_delete.clicked.connect(self.on_delete_env)
        
        self.ui.comboBox_card_single.currentIndexChanged.connect(self.on_card_changed)
        self.ui.pushButton_card_copy.clicked.connect(self.on_copy_card)
        self.ui.pushButton_card_save.clicked.connect(self.on_save_card)
        self.ui.pushButton_card_new.clicked.connect(self.on_new_card)
        self.ui.pushButton_card_delete.clicked.connect(self.on_delete_card)
        
        self.ui.pushButton_note_save.clicked.connect(self.on_save_note)
        self.ui.pushButton_note_env.clicked.connect(self.on_switch_note)
        self.ui.pushButton_src_dir.clicked.connect(self.on_open_note_dir)
        
        self.ui.pushButton_top.clicked.connect(self.on_toggle_top)
    
    def load_environments(self):
        envs = self.controller.get_environments()
        self.ui.comboBox_env.clear()
        self.ui.comboBox_env.addItems(envs)
        logger.debug(f"加载环境列表: {envs}")
    
    def load_accounts(self):
        accounts = self.controller.get_accounts()
        self.ui.comboBox_account.clear()
        self.ui.comboBox_account.addItems(accounts)
        logger.debug(f"加载账号列表: {accounts}")
    
    def load_cards(self):
        cards = self.controller.get_cards()
        self.ui.comboBox_card_single.clear()
        self.ui.comboBox_card_single.addItems(cards)
        logger.debug(f"加载名片列表: {cards}")
    
    def load_notes(self):
        files = self.controller.get_notes()
        if not files:
            files = ["note.txt"]
            self.controller.switch_note("note.txt")
        logger.debug(f"加载笔记列表: {files}")
    
    def load_env_details(self):
        data = self.controller.get_current_env_data()
        self.ui.lineEdit_host.setText(data["host"])
        self.ui.lineEdit_account.setText(data["account"])
        self.ui.lineEdit_possword.setText(data["password"])
        logger.debug(f"加载环境详情: {data['env_name']} - {data['account_name']}")
    
    def load_card_details(self):
        data = self.controller.get_current_card_data()
        self.ui.lineEdit_card_single.setText(data["content"])
        logger.debug(f"加载名片内容: {data['title']}")
    
    def load_note_content(self):
        content = self.controller.get_note_content()
        self.ui.plainTextEdit_note.setPlainText(content)
        self.ui.label_note_name.setText(self.controller.current_note)
        logger.debug(f"加载笔记内容: {self.controller.current_note}")
    
    def on_env_changed(self, index: int):
        self.controller.set_env_index(index)
        self.load_accounts()
        self.load_env_details()
        logger.info(f"切换环境: {index}")
    
    def on_account_changed(self, index: int):
        self.controller.set_account_index(index)
        self.load_env_details()
        logger.info(f"切换账号: {index}")
    
    def on_copy_host(self):
        text = self.ui.lineEdit_host.text()
        if text:
            self.controller.copy_to_clipboard(text)
            logger.info("复制地址")
    
    def on_copy_account(self):
        text = self.ui.lineEdit_account.text()
        if text:
            self.controller.copy_to_clipboard(text)
            logger.info("复制账号")
    
    def on_copy_password(self):
        text = self.ui.lineEdit_possword.text()
        if text:
            self.controller.copy_to_clipboard(text)
            logger.info("复制密码")
    
    def on_save_env(self):
        env_name = self.ui.comboBox_env.currentText()
        account_name = self.ui.comboBox_account.currentText()
        host = self.ui.lineEdit_host.text()
        account = self.ui.lineEdit_account.text()
        password = self.ui.lineEdit_possword.text()
        
        env_idx = self.ui.comboBox_env.currentIndex()
        account_idx = self.ui.comboBox_account.currentIndex()
        
        old_account_name = self.controller.get_current_env_data()["account_name"]
        
        if account_name != old_account_name:
            from PySide6.QtWidgets import QMessageBox
            reply = QMessageBox.question(
                None, "确认", f"账户名称已修改，是否新增账户 '{account_name}'？\n\n新增后账户内容和密码将为空，请手动填写。",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if reply == QMessageBox.StandardButton.Yes:
                host = self.ui.lineEdit_host.text()
                self.controller.add_new_account(account_name, host)
                logger.info(f"确认新增账户: {account_name}")
                
                self.load_environments()
                self.load_accounts()
                self.ui.comboBox_env.setCurrentIndex(env_idx)
                self.ui.comboBox_account.setCurrentIndex(self.ui.comboBox_account.count() - 1)
                self.load_env_details()
            else:
                self.ui.comboBox_account.setCurrentIndex(account_idx)
                logger.info("取消新增账户")
        else:
            self.controller.save_env_name(env_name, account_name)
            self.controller.save_env_data(host, account, password)
            logger.info(f"保存环境账号: {env_name} - {account_name}")
            
            self.load_environments()
            self.load_accounts()
            self.ui.comboBox_env.setCurrentIndex(env_idx)
            self.ui.comboBox_account.setCurrentIndex(account_idx)
    
    def on_new_env(self):
        if self.controller.add_new_env():
            self.load_environments()
            self.load_accounts()
            self.ui.comboBox_env.setCurrentIndex(self.ui.comboBox_env.count() - 1)
            self.load_env_details()
            logger.info("新增环境")
    
    def on_delete_env(self):
        reply = self.controller.delete_current_env()
        if reply:
            self.load_environments()
            self.load_accounts()
            self.load_env_details()
            logger.info("删除环境")
    
    def on_card_changed(self, index: int):
        self.controller.set_card_index(index)
        self.load_card_details()
        logger.info(f"切换名片: {index}")
    
    def on_copy_card(self):
        text = self.ui.lineEdit_card_single.text()
        if text:
            self.controller.copy_to_clipboard(text)
            logger.info("复制名片内容")
    
    def on_save_card(self):
        title = self.ui.comboBox_card_single.currentText()
        content = self.ui.lineEdit_card_single.text()
        
        card_idx = self.ui.comboBox_card_single.currentIndex()
        
        self.controller.save_card_title(title)
        self.controller.save_card_data(title, content)
        
        self.load_cards()
        self.ui.comboBox_card_single.setCurrentIndex(card_idx)
        logger.info("保存名片")
    
    def on_new_card(self):
        if self.controller.add_new_card():
            self.load_cards()
            self.ui.comboBox_card_single.setCurrentIndex(self.ui.comboBox_card_single.count() - 1)
            self.load_card_details()
            logger.info("新增名片")
    
    def on_delete_card(self):
        reply = self.controller.delete_current_card()
        if reply:
            self.load_cards()
            self.load_card_details()
            logger.info("删除名片")
    
    def on_save_note(self):
        content = self.ui.plainTextEdit_note.toPlainText()
        self.controller.save_note_content(content)
        logger.info("保存笔记")
    
    def on_switch_note(self):
        files = self.controller.get_notes()
        if not files:
            return
        
        current = files.index(self.controller.current_note) if self.controller.current_note in files else 0
        files_str = "\n".join(files)
        items = files
        item, ok = QInputDialog.getItem(None, "选择笔记", "请选择笔记文件:", items, current, False)
        
        if ok and item:
            self.on_save_note()
            self.controller.switch_note(item)
            self.load_note_content()
            logger.info(f"切换笔记: {item}")
    
    def on_open_note_dir(self):
        import os
        from pathlib import Path
        notes_dir = Path(__file__).parent.parent / "notes"
        os.startfile(notes_dir)
        logger.info(f"打开笔记目录: {notes_dir}")
    
    def on_toggle_top(self):
        self.is_top = not self.is_top
        if self.is_top:
            self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)
            self.ui.pushButton_top.setText("取消置顶")
        else:
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowType.WindowStaysOnTopHint)
            self.ui.pushButton_top.setText("窗口置顶")
        self.show()
        logger.info(f"窗口置顶: {self.is_top}")


if __name__ == "__main__":
    setup_logger()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("测试环境管理工具")
    window.show()
    sys.exit(app.exec())