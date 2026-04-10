# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_tools.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(369, 640)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_manage = QVBoxLayout()
        self.verticalLayout_manage.setObjectName(u"verticalLayout_manage")
        self.label_manage = QLabel(Form)
        self.label_manage.setObjectName(u"label_manage")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_manage.setFont(font)
        self.label_manage.setFrameShape(QFrame.Shape.NoFrame)
        self.label_manage.setTextFormat(Qt.TextFormat.AutoText)
        self.label_manage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_manage.setWordWrap(False)

        self.verticalLayout_manage.addWidget(self.label_manage)

        self.horizontalLayout_env = QHBoxLayout()
        self.horizontalLayout_env.setObjectName(u"horizontalLayout_env")
        self.label_env = QLabel(Form)
        self.label_env.setObjectName(u"label_env")

        self.horizontalLayout_env.addWidget(self.label_env)

        self.comboBox_env = QComboBox(Form)
        self.comboBox_env.setObjectName(u"comboBox_env")
        self.comboBox_env.setEditable(True)
        self.comboBox_env.setMinimumSize(QSize(285, 0))
        self.comboBox_env.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_env.addWidget(self.comboBox_env)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_env.addItem(self.horizontalSpacer)


        self.verticalLayout_manage.addLayout(self.horizontalLayout_env)

        self.horizontalLayout_host = QHBoxLayout()
        self.horizontalLayout_host.setObjectName(u"horizontalLayout_host")
        self.label_host = QLabel(Form)
        self.label_host.setObjectName(u"label_host")

        self.horizontalLayout_host.addWidget(self.label_host)

        self.lineEdit_host = QLineEdit(Form)
        self.lineEdit_host.setObjectName(u"lineEdit_host")
        self.lineEdit_host.setMinimumSize(QSize(200, 0))
        self.lineEdit_host.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_host.addWidget(self.lineEdit_host)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_host.addItem(self.horizontalSpacer_3)

        self.pushButton_host_copy = QPushButton(Form)
        self.pushButton_host_copy.setObjectName(u"pushButton_host_copy")

        self.horizontalLayout_host.addWidget(self.pushButton_host_copy)


        self.verticalLayout_manage.addLayout(self.horizontalLayout_host)

        self.horizontalLayout_user = QHBoxLayout()
        self.horizontalLayout_user.setObjectName(u"horizontalLayout_user")
        self.label_user = QLabel(Form)
        self.label_user.setObjectName(u"label_user")

        self.horizontalLayout_user.addWidget(self.label_user)

        self.comboBox_account = QComboBox(Form)
        self.comboBox_account.setObjectName(u"comboBox_account")
        self.comboBox_account.setEditable(True)
        self.comboBox_account.setMinimumSize(QSize(285, 0))
        self.comboBox_account.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_user.addWidget(self.comboBox_account)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_user.addItem(self.horizontalSpacer_2)


        self.verticalLayout_manage.addLayout(self.horizontalLayout_user)

        self.horizontalLayout_account = QHBoxLayout()
        self.horizontalLayout_account.setObjectName(u"horizontalLayout_account")
        self.label_account = QLabel(Form)
        self.label_account.setObjectName(u"label_account")

        self.horizontalLayout_account.addWidget(self.label_account)

        self.lineEdit_account = QLineEdit(Form)
        self.lineEdit_account.setObjectName(u"lineEdit_account")
        self.lineEdit_account.setMinimumSize(QSize(200, 0))
        self.lineEdit_account.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_account.addWidget(self.lineEdit_account)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_account.addItem(self.horizontalSpacer_4)

        self.pushButton_account_copy = QPushButton(Form)
        self.pushButton_account_copy.setObjectName(u"pushButton_account_copy")

        self.horizontalLayout_account.addWidget(self.pushButton_account_copy)


        self.verticalLayout_manage.addLayout(self.horizontalLayout_account)

        self.horizontalLayout_password = QHBoxLayout()
        self.horizontalLayout_password.setObjectName(u"horizontalLayout_password")
        self.label_password = QLabel(Form)
        self.label_password.setObjectName(u"label_password")

        self.horizontalLayout_password.addWidget(self.label_password)

        self.lineEdit_possword = QLineEdit(Form)
        self.lineEdit_possword.setObjectName(u"lineEdit_possword")
        self.lineEdit_possword.setMinimumSize(QSize(200, 0))
        self.lineEdit_possword.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_possword.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_password.addWidget(self.lineEdit_possword)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_password.addItem(self.horizontalSpacer_5)

        self.pushButton_possword_copy = QPushButton(Form)
        self.pushButton_possword_copy.setObjectName(u"pushButton_possword_copy")

        self.horizontalLayout_password.addWidget(self.pushButton_possword_copy)


        self.verticalLayout_manage.addLayout(self.horizontalLayout_password)

        self.horizontalLayout_manage_button = QHBoxLayout()
        self.horizontalLayout_manage_button.setObjectName(u"horizontalLayout_manage_button")
        self.pushButton_manage_save = QPushButton(Form)
        self.pushButton_manage_save.setObjectName(u"pushButton_manage_save")

        self.horizontalLayout_manage_button.addWidget(self.pushButton_manage_save)

        self.pushButton_manage_new = QPushButton(Form)
        self.pushButton_manage_new.setObjectName(u"pushButton_manage_new")

        self.horizontalLayout_manage_button.addWidget(self.pushButton_manage_new)

        self.pushButton_manage_delete = QPushButton(Form)
        self.pushButton_manage_delete.setObjectName(u"pushButton_manage_delete")

        self.horizontalLayout_manage_button.addWidget(self.pushButton_manage_delete)


        self.verticalLayout_manage.addLayout(self.horizontalLayout_manage_button)


        self.gridLayout.addLayout(self.verticalLayout_manage, 0, 0, 1, 1)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)

        self.verticalLayout_card = QVBoxLayout()
        self.verticalLayout_card.setObjectName(u"verticalLayout_card")
        self.label_card = QLabel(Form)
        self.label_card.setObjectName(u"label_card")
        self.label_card.setFont(font)
        self.label_card.setFrameShape(QFrame.Shape.NoFrame)
        self.label_card.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_card.addWidget(self.label_card)

        self.horizontalLayout_card_single = QHBoxLayout()
        self.horizontalLayout_card_single.setObjectName(u"horizontalLayout_card_single")
        self.comboBox_card_single = QComboBox(Form)
        self.comboBox_card_single.setObjectName(u"comboBox_card_single")
        self.comboBox_card_single.setEditable(True)

        self.horizontalLayout_card_single.addWidget(self.comboBox_card_single)

        self.lineEdit_card_single = QLineEdit(Form)
        self.lineEdit_card_single.setObjectName(u"lineEdit_card_single")

        self.horizontalLayout_card_single.addWidget(self.lineEdit_card_single)

        self.pushButton_card_copy = QPushButton(Form)
        self.pushButton_card_copy.setObjectName(u"pushButton_card_copy")

        self.horizontalLayout_card_single.addWidget(self.pushButton_card_copy)


        self.verticalLayout_card.addLayout(self.horizontalLayout_card_single)

        self.horizontalLayout_card_button = QHBoxLayout()
        self.horizontalLayout_card_button.setObjectName(u"horizontalLayout_card_button")
        self.pushButton_card_save = QPushButton(Form)
        self.pushButton_card_save.setObjectName(u"pushButton_card_save")

        self.horizontalLayout_card_button.addWidget(self.pushButton_card_save)

        self.pushButton_card_new = QPushButton(Form)
        self.pushButton_card_new.setObjectName(u"pushButton_card_new")

        self.horizontalLayout_card_button.addWidget(self.pushButton_card_new)

        self.pushButton_card_delete = QPushButton(Form)
        self.pushButton_card_delete.setObjectName(u"pushButton_card_delete")

        self.horizontalLayout_card_button.addWidget(self.pushButton_card_delete)


        self.verticalLayout_card.addLayout(self.horizontalLayout_card_button)


        self.gridLayout.addLayout(self.verticalLayout_card, 2, 0, 1, 1)

        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 1)

        self.verticalLayout_note = QVBoxLayout()
        self.verticalLayout_note.setObjectName(u"verticalLayout_note")
        self.label_note = QLabel(Form)
        self.label_note.setObjectName(u"label_note")
        self.label_note.setFont(font)
        self.label_note.setFrameShape(QFrame.Shape.NoFrame)
        self.label_note.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_note.addWidget(self.label_note)

        self.label_note_name = QLabel(Form)
        self.label_note_name.setObjectName(u"label_note_name")
        font1 = QFont()
        font1.setItalic(True)
        font1.setUnderline(False)
        self.label_note_name.setFont(font1)
        self.label_note_name.setFrameShape(QFrame.Shape.NoFrame)
        self.label_note_name.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_note_name.setMargin(0)
        self.label_note_name.setIndent(10)

        self.verticalLayout_note.addWidget(self.label_note_name)

        self.plainTextEdit_note = QPlainTextEdit(Form)
        self.plainTextEdit_note.setObjectName(u"plainTextEdit_note")
        self.plainTextEdit_note.setAutoFillBackground(False)

        self.verticalLayout_note.addWidget(self.plainTextEdit_note)

        self.horizontalLayout_note_button = QHBoxLayout()
        self.horizontalLayout_note_button.setObjectName(u"horizontalLayout_note_button")
        self.pushButton_note_save = QPushButton(Form)
        self.pushButton_note_save.setObjectName(u"pushButton_note_save")

        self.horizontalLayout_note_button.addWidget(self.pushButton_note_save)

        self.pushButton_note_env = QPushButton(Form)
        self.pushButton_note_env.setObjectName(u"pushButton_note_env")

        self.horizontalLayout_note_button.addWidget(self.pushButton_note_env)

        self.pushButton_src_dir = QPushButton(Form)
        self.pushButton_src_dir.setObjectName(u"pushButton_src_dir")

        self.horizontalLayout_note_button.addWidget(self.pushButton_src_dir)


        self.verticalLayout_note.addLayout(self.horizontalLayout_note_button)


        self.gridLayout.addLayout(self.verticalLayout_note, 4, 0, 1, 1)

        self.line_3 = QFrame(Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_3, 5, 0, 1, 1)

        self.pushButton_top = QPushButton(Form)
        self.pushButton_top.setObjectName(u"pushButton_top")

        self.gridLayout.addWidget(self.pushButton_top, 6, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_manage.setText(QCoreApplication.translate("Form", u"\u8d26\u6237\u7ba1\u7406", None))
        self.label_env.setText(QCoreApplication.translate("Form", u"\u73af\u5883\u540d\u79f0", None))
        self.label_user.setText(QCoreApplication.translate("Form", u"\u8d26\u6237\u540d\u79f0", None))
        self.label_host.setText(QCoreApplication.translate("Form", u"\u7f51\u5740\u5185\u5bb9", None))
        self.pushButton_host_copy.setText(QCoreApplication.translate("Form", u"\u590d\u5236", None))
        self.label_account.setText(QCoreApplication.translate("Form", u"\u8d26\u6237\u5185\u5bb9", None))
        self.pushButton_account_copy.setText(QCoreApplication.translate("Form", u"\u590d\u5236", None))
        self.label_password.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801\u5185\u5bb9", None))
        self.pushButton_possword_copy.setText(QCoreApplication.translate("Form", u"\u590d\u5236", None))
        self.pushButton_manage_save.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58", None))
        self.pushButton_manage_new.setText(QCoreApplication.translate("Form", u"\u65b0\u589e", None))
        self.pushButton_manage_delete.setText(QCoreApplication.translate("Form", u"\u5220\u9664", None))
        self.label_card.setText(QCoreApplication.translate("Form", u"\u5e38\u7528\u540d\u7247", None))
        self.pushButton_card_copy.setText(QCoreApplication.translate("Form", u"\u590d\u5236", None))
        self.pushButton_card_save.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58", None))
        self.pushButton_card_new.setText(QCoreApplication.translate("Form", u"\u65b0\u589e", None))
        self.pushButton_card_delete.setText(QCoreApplication.translate("Form", u"\u5220\u9664", None))
        self.label_note.setText(QCoreApplication.translate("Form", u"\u8bb0\u4e8b\u672c", None))
        self.label_note_name.setText(QCoreApplication.translate("Form", u"note.txt", None))
        self.pushButton_note_save.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58", None))
        self.pushButton_note_env.setText(QCoreApplication.translate("Form", u"\u5207\u6362\u7b14\u8bb0", None))
        self.pushButton_src_dir.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u76ee\u5f55", None))
        self.pushButton_top.setText(QCoreApplication.translate("Form", u"\u7a97\u53e3\u7f6e\u9876", None))
    # retranslateUi

