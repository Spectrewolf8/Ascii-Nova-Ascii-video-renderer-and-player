# Created by: PyQt5 UI code generator 5.15.9
# AsciiNovaUiV2 with minor changes implemented
import os
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
import easygui
from natsort import natsort


class Ui_MainWindow(object):
    _translate = QtCore.QCoreApplication.translate

    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.sidebar_container = QtWidgets.QFrame(self.centralwidget)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.sidebar_container)
        self.sidebar_subcontainer = QtWidgets.QFrame(self.sidebar_container)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.sidebar_subcontainer)
        self.sidebar_subframe_2 = QtWidgets.QFrame(self.sidebar_subcontainer)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.sidebar_subframe_2)
        self.home_btn = QtWidgets.QPushButton(self.sidebar_subframe_2)
        self.play_ascii_video_btn = QtWidgets.QPushButton(self.sidebar_subframe_2)
        self.convert_video_to_ascii_btn = QtWidgets.QPushButton(self.sidebar_subframe_2)
        self.realtime_play_btn = QtWidgets.QPushButton(self.sidebar_subframe_2)
        self.sidebar_subframe_3 = QtWidgets.QFrame(self.sidebar_subcontainer)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.sidebar_subframe_3)
        self.help_btn = QtWidgets.QPushButton(self.sidebar_subframe_3)
        self.main_container = QtWidgets.QFrame(self.centralwidget)
        self.gridLayout = QtWidgets.QGridLayout(self.main_container)
        self.system_message_label = QtWidgets.QLabel(self.main_container)
        self.main_continer_stack = QtWidgets.QStackedWidget(self.main_container)
        self.stack_page_0 = QtWidgets.QWidget()
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.stack_page_0)
        self.home_screen_logo_label = QtWidgets.QLabel(self.stack_page_0)
        self.home_screen_text_label = QtWidgets.QLabel(self.stack_page_0)
        self.stack_page_1 = QtWidgets.QWidget()
        self.windows_title_label = QtWidgets.QLabel(self.stack_page_1)
        self.path_textBrowser = QtWidgets.QTextBrowser(self.stack_page_1)
        self.browse_file_btn = QtWidgets.QPushButton(self.stack_page_1)
        self.path_label = QtWidgets.QLabel(self.stack_page_1)
        self.render_font_label = QtWidgets.QLabel(self.stack_page_1)
        self.line_height_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.stack_page_1)
        self.line_height_label = QtWidgets.QLabel(self.stack_page_1)
        self.font_size_spinBox = QtWidgets.QSpinBox(self.stack_page_1)
        self.font_size_label = QtWidgets.QLabel(self.stack_page_1)
        self.show_fps_checkBox = QtWidgets.QCheckBox(self.stack_page_1)
        self.render_color_hex_lineEdit = QtWidgets.QLineEdit(self.stack_page_1)
        self.render_color_hex_label = QtWidgets.QLabel(self.stack_page_1)
        self.start_playing_ascii_video_btn = QtWidgets.QPushButton(self.stack_page_1)
        self.choose_fontComboBox = QtWidgets.QComboBox(self.stack_page_1)
        self.stack_page_2 = QtWidgets.QWidget()
        self.path_textBrowser_2 = QtWidgets.QTextBrowser(self.stack_page_2)
        self.render_chars_label = QtWidgets.QLabel(self.stack_page_2)
        self.threads_spinBox = QtWidgets.QSpinBox(self.stack_page_2)
        self.render_ascii_btn = QtWidgets.QPushButton(self.stack_page_2)
        self.threads_label = QtWidgets.QLabel(self.stack_page_2)
        self.path_label_2 = QtWidgets.QLabel(self.stack_page_2)
        self.ascii_image_width_label = QtWidgets.QLabel(self.stack_page_2)
        self.windows_title_label_2 = QtWidgets.QLabel(self.stack_page_2)
        self.browse_file_btn_2 = QtWidgets.QPushButton(self.stack_page_2)
        self.message_label_2 = QtWidgets.QLabel(self.stack_page_2)
        self.ascii_image_width_spinBox = QtWidgets.QSpinBox(self.stack_page_2)
        self.render_ascii_image_width_warning_label = QtWidgets.QLabel(
            self.stack_page_2
        )
        self.threads_warning_label = QtWidgets.QLabel(self.stack_page_2)
        self.render_chars_warning_label = QtWidgets.QLabel(self.stack_page_2)
        self.status_label = QtWidgets.QLabel(self.stack_page_2)
        self.render_progressBar = QtWidgets.QProgressBar(self.stack_page_2)
        self.render_chars_lineEdit = QtWidgets.QLineEdit(self.stack_page_2)
        self.stack_page_3 = QtWidgets.QWidget()
        self.render_chars_lineEdit_2 = QtWidgets.QLineEdit(self.stack_page_3)
        self.browse_file_btn_3 = QtWidgets.QPushButton(self.stack_page_3)
        self.ascii_image_width_label_2 = QtWidgets.QLabel(self.stack_page_3)
        self.path_textBrowser_3 = QtWidgets.QTextBrowser(self.stack_page_3)
        self.render_chars_label_2 = QtWidgets.QLabel(self.stack_page_3)
        self.rt_play_btn = QtWidgets.QPushButton(self.stack_page_3)
        self.path_label_3 = QtWidgets.QLabel(self.stack_page_3)
        self.ascii_image_width_warning_label = QtWidgets.QLabel(self.stack_page_3)
        self.render_color_hex_lineEdit_2 = QtWidgets.QLineEdit(self.stack_page_3)
        self.font_size_spinBox_2 = QtWidgets.QSpinBox(self.stack_page_3)
        self.render_color_hex_label_2 = QtWidgets.QLabel(self.stack_page_3)
        self.font_size_label_2 = QtWidgets.QLabel(self.stack_page_3)
        self.show_fps_checkBox_2 = QtWidgets.QCheckBox(self.stack_page_3)
        self.line_height_doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.stack_page_3)
        self.stack_page_4 = QtWidgets.QWidget()
        self.help_label = QtWidgets.QLabel(self.stack_page_4)
        self.render_font_label_2 = QtWidgets.QLabel(self.stack_page_3)
        self.line_height_label_2 = QtWidgets.QLabel(self.stack_page_3)
        self.windows_title_label_3 = QtWidgets.QLabel(self.stack_page_3)
        self.rt_play_warning_label = QtWidgets.QLabel(self.stack_page_3)
        self.render_chars_warning_label_2 = QtWidgets.QLabel(self.stack_page_3)
        self.choose_fontComboBox_2 = QtWidgets.QComboBox(self.stack_page_3)
        self.render_color_hex_label_3 = QtWidgets.QLabel(self.stack_page_3)

    def setupUi(self):
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(975, 750)
        self.MainWindow.setMinimumSize(QtCore.QSize(600, 750))
        self.MainWindow.setMaximumSize(QtCore.QSize(975, 750))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/Assets /2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.MainWindow.setWindowIcon(icon)
        self.MainWindow.setWindowOpacity(1.0)
        self.MainWindow.setStyleSheet(
            "*{\n"
            "    border:none;\n"
            "    padding:0;\n"
            "    border-radius:20;\n"
            "    background-color: rgb(247, 68, 78);\n"
            "}\n"
            "QPushButton{\n"
            "padding:5px 5px;\n"
            "text-align:left;\n"
            "}\n"
            "\n"
            ""
        )
        self.centralwidget.setStyleSheet("border-radius:20;")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sidebar_container.sizePolicy().hasHeightForWidth()
        )
        self.sidebar_container.setSizePolicy(sizePolicy)
        self.sidebar_container.setMinimumSize(QtCore.QSize(90, 0))
        self.sidebar_container.setMaximumSize(QtCore.QSize(155, 16777215))
        self.sidebar_container.setAutoFillBackground(False)
        self.sidebar_container.setStyleSheet(
            "*{\n"
            "    background-color: rgb(242, 244, 240);\n"
            "    padding:0;\n"
            "}\n"
            "#sidebar_container:hover{\n"
            "background-color:rgb(249, 240, 107)\n"
            "}\n"
            "\n"
            ""
        )
        self.sidebar_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sidebar_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sidebar_container.setObjectName("sidebar_container")
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sidebar_subcontainer.setStyleSheet("*{\n" "    padding:0;\n" "}\n" "")
        self.sidebar_subcontainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sidebar_subcontainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sidebar_subcontainer.setObjectName("sidebar_subcontainer")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.sidebar_subframe_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sidebar_subframe_2.sizePolicy().hasHeightForWidth()
        )
        self.sidebar_subframe_2.setSizePolicy(sizePolicy)
        self.sidebar_subframe_2.setStyleSheet(
            "QPushButton{\n"
            "    padding:5px 7px;\n"
            "    border-radius:5;\n"
            "    border: 1px solid transparent;\n"
            "}\n"
            "QPushButton:hover{\n"
            "border: 1px solid rgb(222, 221, 218);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "    background-color: rgb(192, 191, 188)\n"
            "}"
        )
        self.sidebar_subframe_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sidebar_subframe_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sidebar_subframe_2.setObjectName("sidebar_subframe_2")
        self.verticalLayout_3.setContentsMargins(-1, 12, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.home_btn.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/InterfaceIcons/ALL Doodle Icons/home.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.home_btn.setIcon(icon1)
        self.home_btn.setIconSize(QtCore.QSize(28, 28))
        self.home_btn.setObjectName("home_btn")
        self.verticalLayout_3.addWidget(self.home_btn)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(":/InterfaceIcons/ALL Doodle Icons/play.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.play_ascii_video_btn.setIcon(icon2)
        self.play_ascii_video_btn.setIconSize(QtCore.QSize(28, 28))
        self.play_ascii_video_btn.setObjectName("play_ascii_video_btn")
        self.verticalLayout_3.addWidget(self.play_ascii_video_btn)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap(":/InterfaceIcons/ALL Doodle Icons/png.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.convert_video_to_ascii_btn.setIcon(icon3)
        self.convert_video_to_ascii_btn.setIconSize(QtCore.QSize(28, 28))
        self.convert_video_to_ascii_btn.setObjectName("convert_video_to_ascii_btn")
        self.verticalLayout_3.addWidget(self.convert_video_to_ascii_btn)
        font = QtGui.QFont()
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.realtime_play_btn.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap(":/InterfaceIcons/ALL Doodle Icons/shape.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.realtime_play_btn.setIcon(icon4)
        self.realtime_play_btn.setIconSize(QtCore.QSize(28, 28))
        self.realtime_play_btn.setObjectName("realtime_play_btn")
        self.verticalLayout_3.addWidget(self.realtime_play_btn)
        self.verticalLayout_2.addWidget(self.sidebar_subframe_2)
        self.sidebar_subframe_3.setStyleSheet(
            "QPushButton{\n"
            "    padding:5px 7px;\n"
            "    border-radius:5;\n"
            "    border: 1px solid transparent;\n"
            "}\n"
            "QPushButton:hover{\n"
            "border: 1px solid rgb(222, 221, 218);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "    background-color: rgb(192, 191, 188)\n"
            "}"
        )
        self.sidebar_subframe_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sidebar_subframe_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sidebar_subframe_3.setObjectName("sidebar_subframe_3")
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(
            QtGui.QPixmap(":/InterfaceIcons/ALL Doodle Icons/Info.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.help_btn.setIcon(icon5)
        self.help_btn.setIconSize(QtCore.QSize(28, 28))
        self.help_btn.setObjectName("help_btn")
        self.verticalLayout_5.addWidget(self.help_btn)
        self.verticalLayout_2.addWidget(
            self.sidebar_subframe_3, 0, QtCore.Qt.AlignBottom
        )
        self.verticalLayout.addWidget(self.sidebar_subcontainer)
        self.horizontalLayout.addWidget(self.sidebar_container)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.main_container.sizePolicy().hasHeightForWidth()
        )
        self.main_container.setSizePolicy(sizePolicy)
        self.main_container.setStyleSheet(
            "*{\n"
            "    border-top-right-radius:0;\n"
            "    background-color: rgb(242, 244, 240);\n"
            "    padding:0;\n"
            "}\n"
            "#main_container:hover{\n"
            "    background-color: rgb(249, 240, 107)\n"
            "}\n"
            "\n"
            ""
        )
        self.main_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_container.setObjectName("main_container")
        self.gridLayout.setContentsMargins(7, 7, 7, 7)
        self.gridLayout.setObjectName("gridLayout")
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.system_message_label.sizePolicy().hasHeightForWidth()
        )
        self.system_message_label.setSizePolicy(sizePolicy)
        self.system_message_label.setMinimumSize(QtCore.QSize(100, 65))
        self.system_message_label.setStyleSheet(
            "*{\n"
            "color: rgb(224, 27, 36);\n"
            'font: 75 10pt "Noto Sans Medium";\n'
            "background-color: rgb(230, 230, 230);\n"
            "border-radius:20px;\n"
            "padding: 8px;\n"
            "}"
        )
        self.system_message_label.setText("No system message yet...")
        self.system_message_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )
        self.system_message_label.setWordWrap(True)
        self.system_message_label.setObjectName("message_label")
        self.gridLayout.addWidget(self.system_message_label, 2, 0, 1, 1)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_continer_stack.setFont(font)
        self.main_continer_stack.setStyleSheet("")
        self.main_continer_stack.setObjectName("main_continer_stack")
        self.stack_page_0.setStyleSheet(
            "* {\n"
            "    border-top-right-radius: 0;\n"
            "    border-top-left-radius: 20px;\n"
            "    border-bottom-right-radius: 20px;\n"
            "    border-bottom-left-radius: 20px;\n"
            "}\n"
            "QPushButton{\n"
            "    background-color: rgb(248, 228, 92);\n"
            "    padding:5px 7px;\n"
            "    border-radius:5;\n"
            "    border: 1px solid transparent;\n"
            "}\n"
            "QPushButton:hover{\n"
            "border: 1px solid rgb(222, 221, 218);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "    background-color: rgb(192, 191, 188)\n"
            "}\n"
            "\n"
            ""
        )
        self.stack_page_0.setObjectName("stack_page_0")
        self.verticalLayout_4.setContentsMargins(-1, 26, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.home_screen_logo_label.setObjectName("home_screen_logo_label")
        self.verticalLayout_4.addWidget(self.home_screen_logo_label)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.home_screen_text_label.sizePolicy().hasHeightForWidth()
        )
        self.home_screen_text_label.setSizePolicy(sizePolicy)
        self.home_screen_text_label.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.home_screen_text_label.setFont(font)
        self.home_screen_text_label.setStyleSheet("*{\n" "color:rgb(36, 31, 49);\n" "}")
        self.home_screen_text_label.setWordWrap(True)
        self.home_screen_text_label.setObjectName("home_screen_text_label")
        self.verticalLayout_4.addWidget(self.home_screen_text_label)
        self.main_continer_stack.addWidget(self.stack_page_0)
        self.stack_page_1.setStyleSheet(
            "QPushButton{\n"
            "border:1px solid transparent;\n"
            "}\n"
            "QPushButton:hover{\n"
            "border:1px solid gray;\n"
            "}\n"
            "QComboBox:hover{\n"
            "border:1px solid gray;\n"
            "}\n"
            "\n"
            "QComboBox{\n"
            "border:1px solid transparent;\n"
            "}\n"
            "QComboBox:hover{\n"
            "border:1px solid gray;\n"
            "}\n"
            "\n"
            ""
        )
        self.stack_page_1.setObjectName("stack_page_1")
        self.windows_title_label.setGeometry(QtCore.QRect(341, 12, 101, 31))
        self.windows_title_label.setObjectName("windows_title_label")
        self.path_textBrowser.setGeometry(QtCore.QRect(30, 90, 300, 61))
        self.path_textBrowser.setStyleSheet(
            "*{\n"
            "border-radius:5;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QTextBrowser:hover{\n"
            "background-color:rgb(220, 220, 220);\n"
            "}"
        )
        self.path_textBrowser.setObjectName("path_textBrowser")
        self.browse_file_btn.setGeometry(QtCore.QRect(30, 155, 105, 33))
        self.browse_file_btn.setMaximumSize(QtCore.QSize(150, 16777215))
        self.browse_file_btn.setStyleSheet(
            "QPushButton{\n"
            "background-color:rgb(249, 240, 107);\n"
            "border-radius:5;\n"
            "padding:5;\n"
            "}\n"
            "QPushButton:pressed{\n"
            "background-color: rgb(192, 191, 188)\n"
            "}"
        )
        self.browse_file_btn.setObjectName("browse_file_btn")
        self.path_label.setGeometry(QtCore.QRect(30, 60, 191, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.path_label.setFont(font)
        self.path_label.setObjectName("path_label")
        self.render_font_label.setGeometry(QtCore.QRect(30, 210, 191, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.render_font_label.setFont(font)
        self.render_font_label.setObjectName("render_font_label")
        self.line_height_doubleSpinBox.setGeometry(QtCore.QRect(29, 321, 69, 32))
        self.line_height_doubleSpinBox.setStyleSheet(
            "\n"
            "QDoubleSpinBox {\n"
            "    border:1px solid rgb(192, 191, 188);\n"
            "    background-color: rgb(220, 220, 220);\n"
            "    border-radius: 10px;\n"
            "     subcontrol-origin: padding;\n"
            "    subcontrol-position: center right;\n"
            "}\n"
            "QDoubleSpinBox::up-button {\n"
            "    padding-right:2px;\n"
            "    image: url(:/InterfaceIcons/ALL Doodle Icons/arrow-single-up.svg);\n"
            "    width: 13px;\n"
            "    height: 13px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "\n"
            "QDoubleSpinBox::down-button {\n"
            "    padding-right:2px;\n"
            "    image: url(:/InterfaceIcons/ALL Doodle Icons/arrow-single-down.svg);\n"
            "    width: 13px;\n"
            "    height: 13px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            ""
        )
        self.line_height_doubleSpinBox.setMaximum(2.0)
        self.line_height_doubleSpinBox.setMinimum(0.20)
        self.line_height_doubleSpinBox.setSingleStep(0.1)
        self.line_height_doubleSpinBox.setObjectName("line_height_doubleSpinBox")
        self.line_height_label.setGeometry(QtCore.QRect(30, 291, 81, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_height_label.setFont(font)
        self.line_height_label.setObjectName("line_height_label")
        self.font_size_spinBox.setGeometry(QtCore.QRect(29, 387, 70, 32))
        self.font_size_spinBox.setStyleSheet(
            "\n"
            "QSpinBox {\n"
            "    border:1px solid rgb(192, 191, 188);\n"
            "    background-color: rgb(220, 220, 220);\n"
            "    border-radius: 10px;\n"
            "     subcontrol-origin: padding;\n"
            "    subcontrol-position: center right;\n"
            "}\n"
            "QSpinBox::up-button {\n"
            "    padding-right:2px;\n"
            "    image: url(:/InterfaceIcons/ALL Doodle Icons/arrow-single-up.svg);\n"
            "    width: 13px;\n"
            "    height: 13px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "\n"
            "QSpinBox::down-button {\n"
            "    padding-right:2px;\n"
            "    image: url(:/InterfaceIcons/ALL Doodle Icons/arrow-single-down.svg);\n"
            "    width: 13px;\n"
            "    height: 13px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            ""
        )
        self.font_size_spinBox.setMinimum(2)
        self.font_size_spinBox.setMaximum(96)
        self.font_size_spinBox.setSingleStep(2)
        self.font_size_spinBox.setObjectName("font_size_spinBox")
        self.font_size_label.setGeometry(QtCore.QRect(30, 357, 71, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.font_size_label.setFont(font)
        self.font_size_label.setObjectName("font_size_label")
        self.show_fps_checkBox.setGeometry(QtCore.QRect(33, 500, 120, 29))
        self.show_fps_checkBox.setStyleSheet(
            "QCheckBox{\n"
            "border:1px solid gray;\n"
            "border-radius:5px;\n"
            "padding:5px;\n"
            "}\n"
            "QCheckBox:hover{\n"
            "background-color:rgb(220, 220, 220);\n"
            "}"
        )
        self.show_fps_checkBox.setObjectName("show_fps_checkBox")
        self.render_color_hex_lineEdit.setGeometry(QtCore.QRect(30, 453, 80, 31))
        self.render_color_hex_lineEdit.setStyleSheet(
            "QLineEdit{\n"
            "border-radius:5px;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QLineEdit:hover{\n"
            "background-color: rgb(220, 220, 220);\n"
            "}"
        )
        self.render_color_hex_lineEdit.setMaxLength(7)
        self.render_color_hex_lineEdit.setObjectName("render_color_hex_lineEdit")
        self.render_color_hex_label.setGeometry(QtCore.QRect(30, 423, 121, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.render_color_hex_label.setFont(font)
        self.render_color_hex_label.setObjectName("render_color_hex_label")
        self.start_playing_ascii_video_btn.setGeometry(QtCore.QRect(30, 544, 250, 80))
        self.start_playing_ascii_video_btn.setMaximumSize(
            QtCore.QSize(16777215, 16777215)
        )
        font = QtGui.QFont()
        font.setFamily("Noto Sans Medium")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.start_playing_ascii_video_btn.setFont(font)
        self.start_playing_ascii_video_btn.setStyleSheet(
            "QPushButton{\n"
            'font: 75 16pt "Consolas";\n'
            "background-color: rgb(220, 138, 221);\n"
            "border-radius:5;\n"
            "padding:5;\n"
            "text-align:center;\n"
            "}\n"
            "QPushButton:pressed{\n"
            "background-color: rgb(192, 191, 188)\n"
            "}"
        )
        self.start_playing_ascii_video_btn.setIcon(icon2)
        self.start_playing_ascii_video_btn.setIconSize(QtCore.QSize(28, 28))
        self.start_playing_ascii_video_btn.setObjectName("play_ascii_video_pushButton")
        self.choose_fontComboBox.setGeometry(QtCore.QRect(30, 240, 180, 30))
        self.choose_fontComboBox.setStyleSheet(
            "/*For combo box*/\n"
            "QComboBox{\n"
            "padding-left:5px;\n"
            'font: 75 14pt "Ms Shell Dg";\n'
            "background-color:rgb(255, 117, 117);\n"
            "border:1px solid transparent;\n"
            "border-radius:5px;\n"
            "}\n"
            "QComboBox:hover{\n"
            "border:1px solid gray;\n"
            "}\n"
            "QComboBox QAbstractItemView {\n"
            "    background-color: white;\n"
            "    border-radius:1px;\n"
            "    selection-background-color: lightgray;\n"
            "}\n"
            "QComboBox::drop-down {\n"
            "    image: none;\n"
            "}\n"
            "QComboBox::down-arrow {\n"
            "    padding-top: 5px;\n"
            "    padding-left:4px;\n"
            "    padding-right:6px;\n"
            "    padding-bottom:5px;\n"
            "    border-radius:3px;\n"
            "    image: url(:/InterfaceIcons/ALL Doodle Icons/chevrons-down.svg);\n"
            "    width: 18px;\n"
            "    height: 18px;\n"
            "}\n"
            "QComboBox::down-arrow:hover{\n"
            "  border:1px solid gray;\n"
            "}\n"
            "/* For Scroll bar*/\n"
            "ComboBox QScrollBar:vertical {\n"
            "background-color:rgb(255, 117, 117);\n"
            "    width: 12px;\n"
            "    margin: 0px 0px 0px 0px;\n"
            "}\n"
            "\n"
            "QComboBox QScrollBar::handle:vertical {\n"
            "    background-color: gray;\n"
            "    border-radius: 10px;\n"
            "}\n"
            "\n"
            "QComboBox QScrollBar::add-line:vertical {\n"
            "    border: none;\n"
            "    background: none;\n"
            "    color: #555;\n"
            "    height: 16px;\n"
            "    subcontrol-position: bottom;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "\n"
            "QComboBox QScrollBar::sub-line:vertical {\n"
            "    border: none;\n"
            "    background: none;\n"
            "    color: #555;\n"
            "    height: 16px;\n"
            "    subcontrol-position: top;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "\n"
            "QComboBox QScrollBar::add-page:vertical, QComboBox QScrollBar::sub-page:vertical {\n"
            "    background: none;\n"
            "}"
        )
        self.choose_fontComboBox.setObjectName("choose_fontComboBox")
        self.main_continer_stack.addWidget(self.stack_page_1)
        self.stack_page_2.setStyleSheet(
            "QPushButton{\n"
            "border:1px solid transparent;\n"
            "}\n"
            "QPushButton:hover{\n"
            "border:1px solid gray;\n"
            "}\n"
            "QComboBox:hover{\n"
            "border:1px solid gray;\n"
            "}\n"
            "\n"
            "QComboBox{\n"
            "border:1px solid transparent;\n"
            "}\n"
            "QComboBox:hover{\n"
            "border:1px solid gray;\n"
            "}\n"
            ""
        )
        self.stack_page_2.setObjectName("stack_page_2")
        self.path_textBrowser_2.setGeometry(QtCore.QRect(30, 80, 300, 61))
        self.path_textBrowser_2.setStyleSheet(
            "*{\n"
            "border-radius:5;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QTextBrowser:hover{\n"
            "background-color:rgb(220, 220, 220);\n"
            "}"
        )
        self.path_textBrowser_2.setObjectName("path_textBrowser_2")
        self.render_chars_label.setGeometry(QtCore.QRect(30, 288, 121, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.render_chars_label.setFont(font)
        self.render_chars_label.setObjectName("rennder_chars_label")
        self.threads_spinBox.setGeometry(QtCore.QRect(32, 465, 70, 32))
        self.threads_spinBox.setStyleSheet(
            "\n"
            "QSpinBox {\n"
            "    border:1px solid rgb(192, 191, 188);\n"
            "    background-color: rgb(220, 220, 220);\n"
            "    border-radius: 10px;\n"
            "     subcontrol-origin: padding;\n"
            "    subcontrol-position: center right;\n"
            "}\n"
            "QSpinBox::up-button {\n"
            "    padding-right:2px;\n"
            "    image: url(:/InterfaceIcons/ALL Doodle Icons/arrow-single-up.svg);\n"
            "    width: 13px;\n"
            "    height: 13px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "\n"
            "QSpinBox::down-button {\n"
            "    padding-right:2px;\n"
            "    image: url(:/InterfaceIcons/ALL Doodle Icons/arrow-single-down.svg);\n"
            "    width: 13px;\n"
            "    height: 13px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            ""
        )
        self.threads_spinBox.setMinimum(1)
        self.threads_spinBox.setMaximum(128)
        self.threads_spinBox.setSingleStep(8)
        self.threads_spinBox.setObjectName("threads_spinBox")
        self.render_ascii_btn.setGeometry(QtCore.QRect(30, 531, 150, 91))
        self.render_ascii_btn.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.render_ascii_btn.setFont(font)
        self.render_ascii_btn.setStyleSheet(
            "QPushButton{\n"
            'font: 75 16pt "Consolas";\n'
            "background-color: rgb(87, 227, 137);\n"
            "border-radius:10px;\n"
            "text-align:center;\n"
            "padding:10px;\n"
            "\n"
            "}\n"
            "QPushButton:hover{\n"
            "border:1px solid gray;\n"
            "}\n"
            "QPushButton:pressed{\n"
            "background-color: rgb(192, 191, 188)\n"
            "}"
        )
        icon6 = QtGui.QIcon()
        icon6.addPixmap(
            QtGui.QPixmap(":/InterfaceIcons/ALL Doodle Icons/fire.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.render_ascii_btn.setIcon(icon6)
        self.render_ascii_btn.setIconSize(QtCore.QSize(32, 32))
        self.render_ascii_btn.setObjectName("render_ascii_btn")
        self.threads_label.setGeometry(QtCore.QRect(33, 441, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.threads_label.setFont(font)
        self.threads_label.setWordWrap(True)
        self.threads_label.setObjectName("threads_label")
        self.path_label_2.setGeometry(QtCore.QRect(30, 50, 191, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.path_label_2.setFont(font)
        self.path_label_2.setObjectName("path_label_2")
        self.ascii_image_width_label.setGeometry(QtCore.QRect(31, 195, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ascii_image_width_label.setFont(font)
        self.ascii_image_width_label.setToolTip("")
        self.ascii_image_width_label.setStyleSheet("")
        self.ascii_image_width_label.setWordWrap(True)
        self.ascii_image_width_label.setObjectName("ascii_image_width_label")
        self.windows_title_label_2.setGeometry(QtCore.QRect(330, 11, 130, 31))
        self.windows_title_label_2.setObjectName("windows_title_label_2")
        self.browse_file_btn_2.setGeometry(QtCore.QRect(30, 145, 140, 33))
        self.browse_file_btn_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.browse_file_btn_2.setStyleSheet(
            "QPushButton{\n"
            "background-color:rgb(249, 240, 107);\n"
            "border-radius:5;\n"
            "padding:5;\n"
            "}\n"
            "QPushButton:pressed{\n"
            "background-color: rgb(192, 191, 188)\n"
            "}"
        )
        self.browse_file_btn_2.setObjectName("browse_file_btn_2")
        self.message_label_2.setGeometry(QtCore.QRect(201, 543, 530, 50))
        self.message_label_2.setStyleSheet(
            "*{\n"
            "border:1px solid rgb(220, 138, 221);\n"
            "border-radius:5px;\n"
            "background-color:rgb(246, 245, 244);\n"
            "padding:10px;\n"
            "color: rgb(224, 27, 36);\n"
            "}\n"
            ""
        )
        self.message_label_2.setObjectName("message_label_2")
        self.ascii_image_width_spinBox.setGeometry(QtCore.QRect(31, 240, 70, 32))
        self.ascii_image_width_spinBox.setToolTip("")
        self.ascii_image_width_spinBox.setStyleSheet(
            "\n"
            "QSpinBox {\n"
            "    border:1px solid rgb(192, 191, 188);\n"
            "    background-color: rgb(220, 220, 220);\n"
            "    border-radius: 10px;\n"
            "     subcontrol-origin: padding;\n"
            "    subcontrol-position: center right;\n"
            "}\n"
            "QSpinBox::up-button {\n"
            "    padding-right:2px;\n"
            "    image: url(:/InterfaceIcons/ALL Doodle Icons/arrow-single-up.svg);\n"
            "    width: 13px;\n"
            "    height: 13px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "\n"
            "QSpinBox::down-button {\n"
            "    padding-right:2px;\n"
            "    image: url(:/InterfaceIcons/ALL Doodle Icons/arrow-single-down.svg);\n"
            "    width: 13px;\n"
            "    height: 13px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            ""
        )
        self.ascii_image_width_spinBox.setMinimum(20)
        self.ascii_image_width_spinBox.setMaximum(998)
        self.ascii_image_width_spinBox.setSingleStep(10)
        self.ascii_image_width_spinBox.setObjectName("ascii_image_width_spinBox")
        self.render_ascii_image_width_warning_label.setGeometry(
            QtCore.QRect(370, 190, 201, 80)
        )
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.render_ascii_image_width_warning_label.setFont(font)
        self.render_ascii_image_width_warning_label.setStyleSheet(
            "*{\n"
            "border:1px solid rgb(220, 138, 221);\n"
            "border-radius:5px;\n"
            "background-color:rgb(246, 245, 244);\n"
            "padding:10px;\n"
            "color: rgb(224, 27, 36);\n"
            "}\n"
            ""
        )
        self.render_ascii_image_width_warning_label.setWordWrap(True)
        self.render_ascii_image_width_warning_label.setObjectName(
            "render_ascii_image_width_warning_label"
        )
        self.threads_warning_label.setGeometry(QtCore.QRect(351, 435, 250, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.threads_warning_label.setFont(font)
        self.threads_warning_label.setStyleSheet(
            "*{\n"
            "border:1px solid rgb(220, 138, 221);\n"
            "border-radius:5px;\n"
            "background-color:rgb(246, 245, 244);\n"
            "padding:10px;\n"
            "color: rgb(224, 27, 36);\n"
            "}\n"
            ""
        )
        self.threads_warning_label.setWordWrap(True)
        self.threads_warning_label.setObjectName("threads_warning_label")
        self.render_chars_warning_label.setGeometry(QtCore.QRect(30, 357, 500, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.render_chars_warning_label.setFont(font)
        self.render_chars_warning_label.setStyleSheet(
            "*{\n"
            "border:1px solid rgb(220, 138, 221);\n"
            "border-radius:5px;\n"
            "background-color:rgb(246, 245, 244);\n"
            "padding:10px;\n"
            "color: rgb(224, 27, 36);\n"
            "}\n"
            ""
        )
        self.render_chars_warning_label.setWordWrap(True)
        self.render_chars_warning_label.setObjectName("render_chars_warning_label")
        self.status_label.setGeometry(QtCore.QRect(203, 521, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.status_label.setFont(font)
        self.status_label.setWordWrap(True)
        self.status_label.setObjectName("status_label")
        self.render_progressBar.setGeometry(QtCore.QRect(202, 596, 530, 25))
        self.render_progressBar.setStyleSheet(
            "QProgressBar {\n"
            "    border: 1px solid rgb(220, 138, 221);\n"
            "    border-radius: 5px;\n"
            "    background-color: rgb(246, 245, 244);\n"
            "    color: rgb(224, 27, 36);\n"
            "    text-align: center;\n"
            "    padding: 0px;\n"
            "}\n"
            "\n"
            "QProgressBar::chunk {\n"
            "    background-color: rgb(192, 97, 203);\n"
            "    border-radius: 5px;\n"
            "    border:1px solid transparent;\n"
            "}\n"
            "\n"
            ""
        )
        self.render_progressBar.setObjectName("render_progressBar")
        self.render_chars_lineEdit.setGeometry(QtCore.QRect(30, 318, 501, 31))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.render_chars_lineEdit.setFont(font)
        self.render_chars_lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.render_chars_lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.render_chars_lineEdit.setStyleSheet(
            "QLineEdit{\n"
            "border-radius:5px;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QLineEdit:hover{\n"
            "background-color: rgb(220, 220, 220);\n"
            "}"
        )
        self.render_chars_lineEdit.setMaxLength(21)
        self.render_chars_lineEdit.setReadOnly(False)
        self.render_chars_lineEdit.setObjectName("render_chars_lineEdit")
        self.main_continer_stack.addWidget(self.stack_page_2)
        self.stack_page_3.setObjectName("stack_page_3")
        self.render_chars_lineEdit_2.setGeometry(QtCore.QRect(30, 311, 500, 31))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.render_chars_lineEdit_2.setFont(font)
        self.render_chars_lineEdit_2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.render_chars_lineEdit_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.render_chars_lineEdit_2.setStyleSheet(
            "QLineEdit{\n"
            "border-radius:5px;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QLineEdit:hover{\n"
            "background-color: rgb(220, 220, 220);\n"
            "}"
        )
        self.render_chars_lineEdit_2.setMaxLength(21)
        self.render_chars_lineEdit_2.setReadOnly(False)
        self.render_chars_lineEdit_2.setObjectName("render_chars_lineEdit_2")
        self.browse_file_btn_3.setGeometry(QtCore.QRect(30, 145, 140, 33))
        self.browse_file_btn_3.setMaximumSize(QtCore.QSize(150, 16777215))
        self.browse_file_btn_3.setStyleSheet(
            "QPushButton{\n"
            "background-color:rgb(249, 240, 107);\n"
            "border-radius:5;\n"
            "border: 1px solid transparent;\n"
            "padding:5;\n"
            "}\n"
            "QPushButton:pressed{\n"
            "background-color: rgb(192, 191, 188)\n"
            "}"
            "QPushButton:hover\n"
            "{"
            "border: 1px solid gray;\n"
            "}"
        )
        self.browse_file_btn_3.setObjectName("browse_file_btn_3")
        self.ascii_image_width_label_2.setGeometry(QtCore.QRect(31, 195, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ascii_image_width_label_2.setFont(font)
        self.ascii_image_width_label_2.setToolTip("")
        self.ascii_image_width_label_2.setStyleSheet("")
        self.ascii_image_width_label_2.setWordWrap(True)
        self.ascii_image_width_label_2.setObjectName("ascii_image_width_label_2")
        self.path_textBrowser_3.setGeometry(QtCore.QRect(30, 80, 260, 61))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.path_textBrowser_3.setFont(font)
        self.path_textBrowser_3.setStyleSheet(
            "*{\n"
            "border-radius:5;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QTextBrowser:hover{\n"
            "background-color:rgb(220, 220, 220);\n"
            "}"
        )
        self.path_textBrowser_3.setObjectName("path_textBrowser_3")
        self.render_chars_label_2.setGeometry(QtCore.QRect(30, 281, 121, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.render_chars_label_2.setFont(font)
        self.render_chars_label_2.setObjectName("render_chars_label_2")
        self.rt_play_btn.setGeometry(QtCore.QRect(30, 558, 720, 70))
        self.rt_play_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.rt_play_btn.setFont(font)
        self.rt_play_btn.setStyleSheet(
            "QPushButton{\n"
            'font: 75 16pt "Consolas";\n'
            "background-color: rgb(87, 227, 137);\n"
            "border-radius:10px;\n"
            "text-align:center;\n"
            "padding:10px;\n"
            "\n"
            "}\n"
            "QPushButton:hover{\n"
            "border:1px solid gray;\n"
            "}\n"
            "QPushButton:pressed{\n"
            "background-color: rgb(192, 191, 188)\n"
            "}"
        )
        self.rt_play_btn.setIcon(icon6)
        self.rt_play_btn.setIconSize(QtCore.QSize(32, 32))
        self.rt_play_btn.setObjectName("rt_play_btn")
        self.ascii_image_width_spinBox_2 = QtWidgets.QSpinBox(self.stack_page_3)
        self.ascii_image_width_spinBox_2.setGeometry(QtCore.QRect(31, 240, 70, 32))
        self.ascii_image_width_spinBox_2.setToolTip("")
        self.ascii_image_width_spinBox_2.setStyleSheet(
            "\n"
            "QSpinBox {\n"
            "    border:1px solid rgb(192, 191, 188);\n"
            "    background-color: rgb(220, 220, 220);\n"
            "    border-radius: 10px;\n"
            "     subcontrol-origin: padding;\n"
            "    subcontrol-position: center right;\n"
            "}\n"
            "QSpinBox::up-button {\n"
            "    padding-right:2px;\n"
            "    image: url(:/InterfaceIcons/ALL Doodle Icons/arrow-single-up.svg);\n"
            "    width: 13px;\n"
            "    height: 13px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "\n"
            "QSpinBox::down-button {\n"
            "    padding-right:2px;\n"
            "    image: url(:/InterfaceIcons/ALL Doodle Icons/arrow-single-down.svg);\n"
            "    width: 13px;\n"
            "    height: 13px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            ""
        )
        self.ascii_image_width_spinBox_2.setMinimum(20)
        self.ascii_image_width_spinBox_2.setMaximum(998)
        self.ascii_image_width_spinBox_2.setSingleStep(10)
        self.ascii_image_width_spinBox_2.setObjectName("ascii_image_width_spinBox_2")
        self.path_label_3.setGeometry(QtCore.QRect(30, 50, 191, 30))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(10)
        self.path_label_3.setFont(font)
        self.path_label_3.setObjectName("path_label_3")
        self.ascii_image_width_warning_label.setGeometry(
            QtCore.QRect(330, 191, 201, 80)
        )
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ascii_image_width_warning_label.setFont(font)
        self.ascii_image_width_warning_label.setStyleSheet(
            "*{\n"
            "border:1px solid rgb(220, 138, 221);\n"
            "border-radius:5px;\n"
            "background-color:rgb(246, 245, 244);\n"
            "padding:10px;\n"
            "color: rgb(224, 27, 36);\n"
            "}\n"
            ""
        )
        self.ascii_image_width_warning_label.setWordWrap(True)
        self.ascii_image_width_warning_label.setObjectName(
            "ascii_image_width_warning_label"
        )
        self.render_color_hex_lineEdit_2.setGeometry(QtCore.QRect(222, 508, 110, 31))
        self.render_color_hex_lineEdit_2.setStyleSheet(
            "QLineEdit{\n"
            "border-radius:5px;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QLineEdit:hover{\n"
            "background-color: rgb(220, 220, 220);\n"
            "}"
        )
        self.render_color_hex_lineEdit_2.setMaxLength(7)
        self.render_color_hex_lineEdit_2.setObjectName("render_color_hex_lineEdit_2")
        self.font_size_spinBox_2.setGeometry(QtCore.QRect(455, 506, 70, 32))
        self.font_size_spinBox_2.setStyleSheet(
            "\n"
            "QSpinBox {\n"
            "    border:1px solid rgb(192, 191, 188);\n"
            "    background-color: rgb(220, 220, 220);\n"
            "    border-radius: 10px;\n"
            "     subcontrol-origin: padding;\n"
            "    subcontrol-position: center right;\n"
            "}\n"
            "QSpinBox::up-button {\n"
            "    padding-right:2px;\n"
            "    image: url(:/InterfaceIcons/ALL Doodle Icons/arrow-single-up.svg);\n"
            "    width: 13px;\n"
            "    height: 13px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "\n"
            "QSpinBox::down-button {\n"
            "    padding-right:2px;\n"
            "    image: url(:/InterfaceIcons/ALL Doodle Icons/arrow-single-down.svg);\n"
            "    width: 13px;\n"
            "    height: 13px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            ""
        )
        self.font_size_spinBox_2.setMinimum(2)
        self.font_size_spinBox_2.setMaximum(96)
        self.font_size_spinBox_2.setSingleStep(2)
        self.font_size_spinBox_2.setObjectName("font_size_spinBox_2")
        self.render_color_hex_label_2.setGeometry(QtCore.QRect(221, 478, 121, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.render_color_hex_label_2.setFont(font)
        self.render_color_hex_label_2.setObjectName("render_color_hex_label_2")
        self.font_size_label_2.setGeometry(QtCore.QRect(455, 476, 71, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.font_size_label_2.setFont(font)
        self.font_size_label_2.setObjectName("font_size_label_2")
        self.show_fps_checkBox_2.setGeometry(QtCore.QRect(30, 508, 170, 31))
        self.show_fps_checkBox_2.setStyleSheet(
            "QCheckBox{\n"
            "border:1px solid gray;\n"
            "border-radius:5px;\n"
            "padding:5px;\n"
            "}\n"
            "QCheckBox:hover{\n"
            "background-color:rgb(220, 220, 220);\n"
            "}"
        )
        self.show_fps_checkBox_2.setObjectName("show_fps_checkBox_2")
        self.line_height_doubleSpinBox_2.setGeometry(QtCore.QRect(360, 506, 69, 32))
        self.line_height_doubleSpinBox_2.setStyleSheet(
            "\n"
            "QDoubleSpinBox {\n"
            "    border:1px solid rgb(192, 191, 188);\n"
            "    background-color: rgb(220, 220, 220);\n"
            "    border-radius: 10px;\n"
            "     subcontrol-origin: padding;\n"
            "    subcontrol-position: center right;\n"
            "}\n"
            "QDoubleSpinBox::up-button {\n"
            "    padding-right:2px;\n"
            "    image: url(:/InterfaceIcons/ALL Doodle Icons/arrow-single-up.svg);\n"
            "    width: 13px;\n"
            "    height: 13px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "\n"
            "QDoubleSpinBox::down-button {\n"
            "    padding-right:2px;\n"
            "    image: url(:/InterfaceIcons/ALL Doodle Icons/arrow-single-down.svg);\n"
            "    width: 13px;\n"
            "    height: 13px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            ""
        )
        self.line_height_doubleSpinBox_2.setMaximum(2.0)
        self.line_height_doubleSpinBox_2.setSingleStep(0.1)
        self.line_height_doubleSpinBox_2.setObjectName("line_height_doubleSpinBox_2")
        self.render_font_label_2.setGeometry(QtCore.QRect(30, 421, 91, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.render_font_label_2.setFont(font)
        self.render_font_label_2.setObjectName("render_font_label_2")
        self.line_height_label_2.setGeometry(QtCore.QRect(360, 476, 81, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_height_label_2.setFont(font)
        self.line_height_label_2.setObjectName("line_height_label_2")
        self.windows_title_label_3.setGeometry(QtCore.QRect(310, 0, 170, 31))
        self.windows_title_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.windows_title_label_3.setObjectName("windows_title_label_3")
        self.rt_play_warning_label.setGeometry(QtCore.QRect(330, 75, 421, 90))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.rt_play_warning_label.setFont(font)
        self.rt_play_warning_label.setStyleSheet(
            "*{\n"
            "border:1px solid rgb(220, 138, 221);\n"
            "border-radius:5px;\n"
            "background-color:rgb(255, 138, 138);\n"
            "padding:10px;\n"
            "color: rgb(36, 31, 49);\n"
            "}\n"
            ""
        )
        self.rt_play_warning_label.setWordWrap(True)
        self.rt_play_warning_label.setObjectName("rt_play_warning_label")
        self.render_chars_warning_label_2.setGeometry(QtCore.QRect(30, 351, 500, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.render_chars_warning_label_2.setFont(font)
        self.render_chars_warning_label_2.setStyleSheet(
            "*{\n"
            "border:1px solid rgb(220, 138, 221);\n"
            "border-radius:5px;\n"
            "background-color:rgb(246, 245, 244);\n"
            "padding:10px;\n"
            "color: rgb(224, 27, 36);\n"
            "}\n"
            ""
        )
        self.render_chars_warning_label_2.setWordWrap(True)
        self.render_chars_warning_label_2.setObjectName("render_chars_warning_label_2")
        self.choose_fontComboBox_2.setGeometry(QtCore.QRect(30, 448, 171, 30))
        self.choose_fontComboBox_2.setStyleSheet(
            "/*For combo box*/\n"
            "QComboBox{\n"
            "padding-left:5px;\n"
            'font: 75 14pt "Ms Shell Dg";\n'
            "background-color:rgb(255, 117, 117);\n"
            "border:1px solid transparent;\n"
            "border-radius:5px;\n"
            "}\n"
            "QComboBox:hover{\n"
            "border:1px solid gray;\n"
            "}\n"
            "QComboBox QAbstractItemView {\n"
            "    background-color: white;\n"
            "    border-radius:1px;\n"
            "    selection-background-color: lightgray;\n"
            "}\n"
            "QComboBox::drop-down {\n"
            "    image: none;\n"
            "}\n"
            "QComboBox::down-arrow {\n"
            "    padding-top: 5px;\n"
            "    padding-left:4px;\n"
            "    padding-right:6px;\n"
            "    padding-bottom:5px;\n"
            "    border-radius:3px;\n"
            "    image: url(:/InterfaceIcons/ALL Doodle Icons/chevrons-down.svg);\n"
            "    width: 18px;\n"
            "    height: 18px;\n"
            "}\n"
            "QComboBox::down-arrow:hover{\n"
            "  border:1px solid gray;\n"
            "}\n"
            "/* For Scroll bar*/\n"
            "ComboBox QScrollBar:vertical {\n"
            "background-color:rgb(255, 117, 117);\n"
            "    width: 12px;\n"
            "    margin: 0px 0px 0px 0px;\n"
            "}\n"
            "\n"
            "QComboBox QScrollBar::handle:vertical {\n"
            "    background-color: gray;\n"
            "    border-radius: 10px;\n"
            "}\n"
            "\n"
            "QComboBox QScrollBar::add-line:vertical {\n"
            "    border: none;\n"
            "    background: none;\n"
            "    color: #555;\n"
            "    height: 16px;\n"
            "    subcontrol-position: bottom;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "\n"
            "QComboBox QScrollBar::sub-line:vertical {\n"
            "    border: none;\n"
            "    background: none;\n"
            "    color: #555;\n"
            "    height: 16px;\n"
            "    subcontrol-position: top;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "\n"
            "QComboBox QScrollBar::add-page:vertical, QComboBox QScrollBar::sub-page:vertical {\n"
            "    background: none;\n"
            "}"
        )
        self.choose_fontComboBox_2.setObjectName("choose_fontComboBox_3")
        self.render_color_hex_label_3.setGeometry(QtCore.QRect(30, 478, 121, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.render_color_hex_label_3.setFont(font)
        self.render_color_hex_label_3.setObjectName("render_color_hex_label_3")
        self.render_color_hex_label_3.raise_()
        self.render_chars_lineEdit_2.raise_()
        self.browse_file_btn_3.raise_()
        self.ascii_image_width_label_2.raise_()
        self.path_textBrowser_3.raise_()
        self.render_chars_label_2.raise_()
        self.rt_play_btn.raise_()
        self.ascii_image_width_spinBox_2.raise_()
        self.path_label_3.raise_()
        self.ascii_image_width_warning_label.raise_()
        self.render_color_hex_lineEdit_2.raise_()
        self.font_size_spinBox_2.raise_()
        self.render_color_hex_label_2.raise_()
        self.font_size_label_2.raise_()
        self.show_fps_checkBox_2.raise_()
        self.line_height_doubleSpinBox_2.raise_()
        self.render_font_label_2.raise_()
        self.line_height_label_2.raise_()
        self.windows_title_label_3.raise_()
        self.rt_play_warning_label.raise_()
        self.render_chars_warning_label_2.raise_()
        self.choose_fontComboBox_2.raise_()
        self.main_continer_stack.addWidget(self.stack_page_3)
        self.stack_page_4.setObjectName("stack_page_4")
        self.help_label.setGeometry(QtCore.QRect(39, 39, 600, 100))
        self.help_label.setMaximumSize(QtCore.QSize(600, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.help_label.setFont(font)
        self.help_label.setStyleSheet(
            "*{\n"
            "border:1px solid rgb(220, 138, 221);\n"
            "border-radius:10px;\n"
            "background-color:rgb(246, 245, 244);\n"
            "padding:10px;\n"
            "color: rgb(224, 27, 36);\n"
            "}\n"
            ""
        )
        self.help_label.setWordWrap(True)
        self.help_label.setOpenExternalLinks(True)
        self.help_label.setObjectName("help_label")
        self.main_continer_stack.addWidget(self.stack_page_4)
        self.gridLayout.addWidget(self.main_continer_stack, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.main_container)
        self.MainWindow.setCentralWidget(self.centralwidget)

        self.MainWindow.setWindowTitle(self._translate("MainWindow", "MainWindow"))
        self.home_btn.setToolTip(self._translate("MainWindow", "Home"))
        self.home_btn.setText(self._translate("MainWindow", "Home"))
        self.home_btn.clicked.connect(
            lambda: self.main_continer_stack.setCurrentIndex(0)
        )

        self.play_ascii_video_btn.setToolTip(self._translate("MainWindow", "Play"))
        self.play_ascii_video_btn.setText(self._translate("MainWindow", "Play"))
        self.play_ascii_video_btn.clicked.connect(self.initializeAsciiPlayer)

        self.convert_video_to_ascii_btn.setToolTip(
            self._translate("MainWindow", "Convert")
        )
        self.convert_video_to_ascii_btn.setText(
            self._translate("MainWindow", "Convert")
        )
        self.convert_video_to_ascii_btn.clicked.connect(self.initializeAsciiRenderer)

        self.realtime_play_btn.setToolTip(
            self._translate("MainWindow", "RealTime player")
        )
        self.realtime_play_btn.setText(self._translate("MainWindow", "RT_Play"))
        self.realtime_play_btn.clicked.connect(
            lambda: self.main_continer_stack.setCurrentIndex(3)
        )

        self.help_btn.setToolTip(self._translate("MainWindow", "Help"))
        self.help_btn.setText(self._translate("MainWindow", "help"))
        self.help_btn.clicked.connect(
            lambda: self.main_continer_stack.setCurrentIndex(4)
        )

        self.system_message_label.setToolTip(
            self._translate("MainWindow", "system message bar")
        )
        self.home_screen_logo_label.setText(
            self._translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Cascadia Code'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Cascadia Code\'; font-size:10pt; font-weight:600;">      ___           ___           ___                             </span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:Cascadia Code\'; font-size:10pt; font-weight:600;">       /\\  \\         /\\  \\         /\\  \\          ___         ___   </span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Cascadia Code\'; font-size:10pt; font-weight:600;">    /::\\  \\       /::\\  \\       /::\\  \\        /\\  \\       /\\  \\  </span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Cascadia Code\'; font-size:10pt; font-weight:600;">   /:/\\:\\  \\     /:/\\ \\  \\     /:/\\:\\  \\       \\:\\  \\      \\:\\  \\ </span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Cascadia Code\'; font-size:10pt; font-weight:600;">  /::\\~\\:\\  \\   _\\:\\~\\ \\  \\   /:/  \\:\\  \\      /::\\__\\     /::\\__\\</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Cascadia Code\'; font-size:10pt; font-weight:600;"> /:/\\:\\ \\:\\__\\ /\\ \\:\\ \\ \\__\\ /:/__/ \\:\\__\\  __/:/\\/__/  __/:/\\/__/</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Cascadia Code\'; font-size:10pt; font-weight:600;"> \\/__\\:\\/:/  / \\:\\ \\:\\ \\/__/ \\:\\  \\  \\/__/ /\\/:/  /    /\\/:/  /   </span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Cascadia Code\'; font-size:10pt; font-weight:600;">      \\::/  /   \\:\\ \\:\\__\\    \\:\\  \\       \\::/__/     \\::/__/    </span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Cascadia Code\'; font-size:10pt; font-weight:600;">      /:/  /     \\:\\/:/  /     \\:\\  \\       \\:\\__\\      \\:\\__\\    </span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:Cascadia Code\'; font-size:10pt; font-weight:600;">     /:/  /       \\::/  /       \\:\\__\\       \\/__/       \\/__/    </span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Cascadia Code\'; font-size:10pt; font-weight:600;">     \\/__/         \\/__/         \\/__/                            </span></p>\n'
                '<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Cascadia Code\'; font-size:10pt; font-weight:600;"><br /></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Cascadia Code\'; font-size:10pt; font-weight:600;">     ___           ___           ___           ___     </span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Cascadia Code\'; font-size:10pt; font-weight:600;">    /\\__\\         /\\  \\         /\\__\\         /\\  \\    </span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Cascadia Code\'; font-size:10pt; font-weight:600;">   /::|  |       /::\\  \\       /:/  /        /::\\  \\   </span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Cascadia Code\'; font-size:10pt; font-weight:600;">  /:|:|  |      /:/\\:\\  \\     /:/  /        /:/\\:\\  \\  </span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Cascadia Code\'; font-size:10pt; font-weight:600;"> /:/|:|  |__   /:/  \\:\\  \\   /:/__/  ___   /::\\~\\:\\  \\ </span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Cascadia Code\'; font-size:10pt; font-weight:600;">/:/ |:| /\\__\\ /:/__/ \\:\\__\\  |:|  | /\\__\\ /:/\\:\\ \\:\\__\\</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Cascadia Code\'; font-size:10pt; font-weight:600;">\\/__|:|/:/  / \\:\\  \\ /:/  /  |:|  |/:/  / \\/__\\:\\/:/  /</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Cascadia Code\'; font-size:10pt; font-weight:600;">    |:/:/  /   \\:\\  /:/  /   |:|__/:/  /       \\::/  / </span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Cascadia Code\'; font-size:10pt; font-weight:600;">    |::/  /     \\:\\/:/  /     \\::::/__/        /:/  /  </span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Cascadia Code\'; font-size:10pt; font-weight:600;">    /:/  /       \\::/  /       ~~~~           /:/  /   </span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Cascadia Code\'; font-size:10pt; font-weight:600;">    \\/__/         \\/__/                       \\/__/    </span></p></body></html>',
            )
        )
        self.home_screen_text_label.setText(
            self._translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-weight:600;">ASCII Nova:</span> a lightweight and open source ASCII video              renderer and player</p></body></html>',
            )
        )
        self.windows_title_label.setText(self._translate("MainWindow", "ASCII player"))

        self.browse_file_btn.setText(self._translate("MainWindow", "Browse File"))
        self.path_label.setText(
            self._translate("MainWindow", "JSON gzip file location:")
        )
        self.render_font_label.setText(self._translate("MainWindow", "Render Font:"))
        self.line_height_label.setText(self._translate("MainWindow", "Line Height:"))
        self.font_size_label.setText(self._translate("MainWindow", "Font Size:"))
        self.show_fps_checkBox.setText(self._translate("MainWindow", "Show FPS*"))
        self.render_color_hex_label.setText(
            self._translate("MainWindow", "Render Color Hex:")
        )
        self.start_playing_ascii_video_btn.setText(
            self._translate("MainWindow", "Play Ascii Video!")
        )

        self.render_chars_label.setText(self._translate("MainWindow", "Render CHARS:"))
        self.render_ascii_btn.setText(self._translate("MainWindow", "Render!"))
        self.threads_label.setText(self._translate("MainWindow", "Threads:"))
        self.path_label_2.setText(self._translate("MainWindow", "mp4 file location:"))
        self.ascii_image_width_label.setText(
            self._translate("MainWindow", "Rendered ASCII image width:")
        )
        self.windows_title_label_2.setText(
            self._translate("MainWindow", "ASCII Renderer")
        )
        self.browse_file_btn_2.setText(self._translate("MainWindow", "Browse mp4 File"))
        self.render_ascii_image_width_warning_label.setText(
            self._translate(
                "MainWindow",
                "⚠️ Height calculated using width. Aspect-ratio preserved. Defaults to 120 chars",
            )
        )
        self.threads_warning_label.setText(
            self._translate(
                "MainWindow",
                "⚠️Defines number of threads to use for render. More threads mean lesser time and more CPU load",
            )
        )
        self.render_chars_warning_label.setText(
            self._translate(
                "MainWindow",
                "⚠️Choose the character for ASCII video render. 11 characters SEPARATED BY A WHITESPACE must be chosen. String structure MUST NOT BE ALTERED.",
            )
        )
        self.status_label.setText(self._translate("MainWindow", "status:"))
        self.browse_file_btn_3.setText(self._translate("MainWindow", "Browse mp4 File"))
        self.ascii_image_width_label_2.setText(
            self._translate("MainWindow", "Rendered ASCII image width:")
        )
        self.render_chars_label_2.setText(
            self._translate("MainWindow", "Render CHARS:")
        )
        self.rt_play_btn.setText(self._translate("MainWindow", "Play!"))
        self.path_label_3.setText(self._translate("MainWindow", "mp4 file location:"))
        self.ascii_image_width_warning_label.setText(
            self._translate(
                "MainWindow",
                "⚠️ Height calculated using width. Aspect-ratio preserved. Defaults to 120 chars",
            )
        )
        self.render_color_hex_label_2.setText(
            self._translate("MainWindow", "Render Color Hex:")
        )
        self.font_size_label_2.setText(self._translate("MainWindow", "Font Size:"))
        self.show_fps_checkBox_2.setText(self._translate("MainWindow", "Show FPS*"))
        self.render_font_label_2.setText(self._translate("MainWindow", "Render Font:"))
        self.line_height_label_2.setText(self._translate("MainWindow", "Line Height:"))
        self.windows_title_label_3.setText(
            self._translate("MainWindow", "ASCII Realtime Player")
        )
        self.rt_play_warning_label.setText(
            self._translate(
                "MainWindow",
                "⚠️ RT play warning: RT play renders and plays frames in realtime. Expect potential CPU load and lag.",
            )
        )
        self.render_chars_warning_label_2.setText(
            self._translate(
                "MainWindow",
                "⚠️Choose the character for ASCII video render. 11 characters SEPARATED BY A WHITESPACE must be chosen. String structure MUST NOT BE ALTERED.",
            )
        )
        self.render_color_hex_label_3.setText(
            self._translate("MainWindow", "Render Color Hex:")
        )
        self.help_label.setText(
            self._translate(
                "MainWindow",
                'You can get support and help on ASCII nova\'s <a href="https://github.com/Spectrewolf8/Ascii-Nova-Ascii-video-renderer-and-player">github page</a>',
            )
        )

        self.main_continer_stack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

        # even handling for stack pages done above
        # Handling events

        # Ascii player
        self.browse_file_btn.clicked.connect(self.browseFileForAsciiPlayer)
        self.start_playing_ascii_video_btn.clicked.connect(self.playAsciiVideo)

        # Ascii renderer
        self.browse_file_btn_2.clicked.connect(self.browseFileForAsciiRenderer)
        self.render_ascii_btn.clicked.connect(self.renderAsciiVideo)

        # Realtime ASCII player
        self.browse_file_btn_3.clicked.connect(self.browseFileForRTAsciiPlayer)
        self.realtime_play_btn.clicked.connect(self.initializeRTAsciiPlayer)
        self.rt_play_btn.clicked.connect(self.startRTAsciiPlayer)

    # methods associated with events:

    # Ascii player

    def initializeAsciiPlayer(self):

        fonts = os.listdir("./fonts_dir/")
        fonts = natsort.natsorted(fonts, reverse=False)
        self.choose_fontComboBox.addItems(fonts)
        self.line_height_doubleSpinBox.setProperty("value", 1.0)
        self.font_size_spinBox.setProperty("value", 8)
        self.render_color_hex_lineEdit.setText(self._translate("MainWindow", "#FFFFFF"))
        self.show_fps_checkBox.setChecked(True)
        self.path_textBrowser.setHtml(
            self._translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Noto Sans Medium\'; font-size:12pt;">Path</span></p></body></html>',
            )
        )
        self.main_continer_stack.setCurrentIndex(1)

    def browseFileForAsciiPlayer(self):
        filepath = easygui.fileopenbox(
            "Choose a json.gz file to play",
            "ASCII Nova",
            filetypes=["*.json.gz"],
            default="*.json.gz",
            multiple=False,
        )

        self.system_message_label.setText("No system message yet...")
        if filepath is None:
            self.path_textBrowser.setHtml(
                self._translate(
                    "MainWindow",
                    '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                    '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                    "p, li { white-space: pre-wrap; }\n"
                    "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                    '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Noto Sans Medium\'; font-size:12pt;">Path</span></p></body></html>',
                )
            )
            filepath = self.path_textBrowser.toPlainText()
        else:
            if filepath.endswith(".json.gz"):
                self.path_textBrowser.setText(filepath)
            else:
                self.system_message_label.setText(
                    "Invalid file: The file path does not have the '.json.gz' extension."
                )

        print(filepath)

    def playAsciiVideo(self):

        if (
            self.path_textBrowser.toPlainText() == "Path"
            or self.path_textBrowser.toPlainText() == ""
        ):
            self.system_message_label.setText("No file selected. Please select a file.")
        else:

            from RendererAndPlayer import AsciiVideoPlayer

            AsciiVideoPlayerObject = AsciiVideoPlayer.AsciiVideoPlayer()
            AsciiVideoPlayerObject.lineHeight = self.line_height_doubleSpinBox.value()
            AsciiVideoPlayerObject.fontSize = self.font_size_spinBox.value()
            AsciiVideoPlayerObject.fontColorHex = self.render_color_hex_lineEdit.text()
            AsciiVideoPlayerObject.font = (
                "./fonts_dir/" + self.choose_fontComboBox.currentText()
            )
            AsciiVideoPlayerObject.showFpsSwitch = self.show_fps_checkBox.isChecked()
            AsciiVideoPlayerObject.playAsciiVideo(self.path_textBrowser.toPlainText())
            del AsciiVideoPlayerObject

    # Ascii renderer
    def initializeAsciiRenderer(self):
        self.path_textBrowser_2.setHtml(
            self._translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Noto Sans Medium\'; font-size:12pt;">Path</span></p></body></html>',
            )
        )
        self.ascii_image_width_spinBox.setProperty("value", 120)
        self.render_chars_lineEdit.setText(
            self._translate("MainWindow", "@ # ＄ % ? * + ; : , .")
        )
        self.threads_spinBox.setProperty("value", 64)
        self.message_label_2.setText(
            self._translate("MainWindow", "status: waiting for start")
        )
        self.render_progressBar.setProperty("value", 0)
        self.system_message_label.setText("No system message yet...")
        self.main_continer_stack.setCurrentIndex(2)

    def browseFileForAsciiRenderer(self):
        filepath = easygui.fileopenbox(
            "Choose a mp4 file to Render in ascii",
            "ASCII Nova",
            filetypes=["*.mp4"],
            default="*.mp4",
            multiple=False,
        )

        self.system_message_label.setText("No system message yet...")
        if filepath is None:
            self.path_textBrowser_2.setHtml(
                self._translate(
                    "MainWindow",
                    '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                    '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                    "p, li { white-space: pre-wrap; }\n"
                    "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                    '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Noto Sans Medium\'; font-size:12pt;">Path</span></p></body></html>',
                )
            )
            filepath = self.path_textBrowser_2.toPlainText()
        else:
            if filepath.endswith(".mp4"):
                self.path_textBrowser_2.setText(filepath)
            else:
                self.system_message_label.setText(
                    "Invalid file: The file path does not have the '.mp4' extension."
                )

        print(filepath)

    def renderAsciiVideo(self):
        if (
            self.path_textBrowser_2.toPlainText() == "Path"
            or self.path_textBrowser_2.toPlainText() == ""
        ):
            self.system_message_label.setText("No file selected. Please select a file.")
        else:
            renderChars = self.render_chars_lineEdit.text()
            if len(renderChars) != 21:
                self.system_message_label.setText(
                    "Invalid render characters format: The render characters string must be 21 characters long, with all the characters separated by a whitespace."
                )
            else:
                x = 1
                while x < len(renderChars):
                    if renderChars[x] == " ":
                        pass
                    else:
                        self.system_message_label.setText(
                            "Invalid render characters format: The render characters string must be 21 characters long, with all the characters separated by a whitespace."
                        )
                        return
                    x += 2
                print("Correct format")
                video_thread = self.VideoToAsciiJsonGzipThread(
                    self.render_chars_lineEdit,
                    self.path_textBrowser_2,
                    self.message_label_2,
                    self.render_progressBar,
                    self.threads_spinBox,
                    self.ascii_image_width_spinBox,
                    self.system_message_label,
                )

                # Create a new thread and start it
                thread = threading.Thread(target=video_thread.run)
                thread.start()

    # Realtime Ascii Player
    def browseFileForRTAsciiPlayer(self):
        filepath = easygui.fileopenbox(
            "Choose a mp4 file to Render in ascii",
            "ASCII Nova",
            filetypes=["*.mp4"],
            default="*.mp4",
            multiple=False,
        )

        self.system_message_label.setText("No system message yet...")
        if filepath is None:
            self.path_textBrowser_3.setHtml(
                self._translate(
                    "MainWindow",
                    '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                    '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                    "p, li { white-space: pre-wrap; }\n"
                    "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                    '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Noto Sans Medium\'; font-size:12pt;">Path</span></p></body></html>',
                )
            )
            filepath = self.path_textBrowser_3.toPlainText()
        else:
            if filepath.endswith(".mp4"):
                self.path_textBrowser_3.setText(filepath)
            else:
                self.system_message_label.setText(
                    "Invalid file: The file path does not have the '.mp4' extension."
                )

        print(filepath)

    def initializeRTAsciiPlayer(self):
        fonts = os.listdir("./fonts_dir/")
        fonts = natsort.natsorted(fonts, reverse=False)
        self.choose_fontComboBox_2.addItems(fonts)
        self.path_textBrowser_3.setHtml(
            self._translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Noto Sans Medium\'; font-size:12pt;">Path</span></p></body></html>',
            )
        )
        self.ascii_image_width_spinBox_2.setProperty("value", 120)
        self.render_chars_lineEdit_2.setText(
            self._translate("MainWindow", "@ # ＄ % ? * + ; : , .")
        )
        self.show_fps_checkBox_2.setChecked(True)
        self.render_color_hex_lineEdit_2.setText(
            self._translate("MainWindow", "#FFFFFF")
        )
        self.line_height_doubleSpinBox_2.setProperty("value", 1.0)
        self.font_size_spinBox_2.setProperty("value", 8)
        self.main_continer_stack.setCurrentIndex(3)

    def startRTAsciiPlayer(self):
        if (
            self.path_textBrowser_3.toPlainText() == "Path"
            or self.path_textBrowser_3.toPlainText() == ""
        ):
            self.system_message_label.setText("No file selected. Please select a file.")
        else:
            renderChars = self.render_chars_lineEdit_2.text()
            if len(renderChars) != 21:
                self.system_message_label.setText(
                    "Invalid render characters format: The render characters string must be 21 characters long, with all the characters separated by a whitespace."
                )
            else:
                x = 1
                while x < len(renderChars):
                    if renderChars[x] == " ":
                        pass
                    else:
                        self.system_message_label.setText(
                            "Invalid render characters format: The render characters string must be 21 characters long, with all the characters separated by a whitespace."
                        )
                        return
                    x += 2
                print("Correct format")
                from RendererAndPlayer.RTplayVideoAscii import RealTimeAsciiVideoPlayer

                RealTimeAsciiVideoPlayerObject = RealTimeAsciiVideoPlayer()
                RealTimeAsciiVideoPlayerObject.fontColorHex = (
                    self.render_color_hex_lineEdit_2.text()
                )
                RealTimeAsciiVideoPlayerObject.fontSize = (
                    self.font_size_spinBox_2.value()
                )
                RealTimeAsciiVideoPlayerObject.lineHeight = (
                    self.line_height_doubleSpinBox_2.value()
                )
                RealTimeAsciiVideoPlayerObject.showFpsSwitch = (
                    self.show_fps_checkBox_2.isChecked()
                )
                RealTimeAsciiVideoPlayerObject.ascii_render_font_name = (
                    "./fonts_dir/" + self.choose_fontComboBox_2.currentText()
                )
                RealTimeAsciiVideoPlayerObject.ascii_Chars = renderChars.split(" ")
                RealTimeAsciiVideoPlayerObject.renderTextWidth = (
                    self.ascii_image_width_spinBox_2.value()
                )
                RealTimeAsciiVideoPlayerObject.videoPath = (
                    self.path_textBrowser_3.toPlainText()
                )
                RealTimeAsciiVideoPlayerObject.RTplayVideoAscii()
                del RealTimeAsciiVideoPlayerObject

    # A class to render the video in a separate thread
    class VideoToAsciiJsonGzipThread:

        def __init__(
            self,
            render_chars_lineEdit,
            path_textBrowser_2,
            message_label_2,
            render_progressBar,
            threads_spinBox,
            ascii_image_width_spinBox,
            system_message_label,
        ):
            self.render_chars_lineEdit = render_chars_lineEdit
            self.path_textBrowser_2 = path_textBrowser_2
            self.message_label_2 = message_label_2
            self.render_progressBar = render_progressBar
            self.threads_spinBox = threads_spinBox
            self.ascii_image_width_spinBox = ascii_image_width_spinBox
            self.system_message_label = system_message_label

        def run(self):
            print("Starting render")

            from RendererAndPlayer import VideoToAsciiJsonGzip

            renderChars = self.render_chars_lineEdit.text()
            VideoToAsciiJsonGzip.videoPath = self.path_textBrowser_2.toPlainText()
            VideoToAsciiJsonGzip.ASCII_CHARS = renderChars.split(" ")
            VideoToAsciiJsonGzip.numberOfThreads = self.threads_spinBox.value()
            VideoToAsciiJsonGzip.asciiRenderWidth = (
                self.ascii_image_width_spinBox.value()
            )
            print("Starting render")

            VideoToAsciiJsonGzip.renderVideoToAsciiJsonGzip(
                self.message_label_2, self.render_progressBar
            )

            self.system_message_label.setText(
                "Rendering complete: Rendered file saved to "
                + os.path.abspath(self.path_textBrowser_2.toPlainText()).replace(
                    ".mp4", ".json.gz"
                )
            )


import GuiAndResources.AsciiNovaUIResources_rc


def run_app():
    import sys

    app = QtWidgets.QApplication(sys.argv)

    ui = Ui_MainWindow()
    ui.setupUi()
    ui.MainWindow.show()
    sys.exit(app.exec_())

    # browseFileForAsciiPlayer()
