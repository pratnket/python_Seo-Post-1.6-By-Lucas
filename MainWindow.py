# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1024, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/bg.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        MainWindow.setStatusTip("")
        MainWindow.setWhatsThis("")
        MainWindow.setAccessibleName("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("/*background-color: rgb(255, 255, 255);*/\n"
"/*background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #eef, stop: 1 #d8d9ff);*/\n"
"QWidget{\n"
"    background-image: url(:/icon/bg.png);\n"
"}\n"
"border-width: 2px;\n"
"border-color: rgb(205, 205, 205);\n"
"")
        MainWindow.setWindowFilePath("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setStyleSheet("background: rgba(255, 255, 255, 0);")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(100, 30))
        self.label.setSizeIncrement(QtCore.QSize(0, 0))
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setMinimumSize(QtCore.QSize(120, 404))
        self.groupBox.setMaximumSize(QtCore.QSize(120, 16777215))
        self.groupBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox.setStyleSheet("background-image: url();")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.Start_thread = QtWidgets.QPushButton(self.groupBox)
        self.Start_thread.setStyleSheet("QPushButton {\n"
"     background-color: qlineargradient(spread:pad, x1:0, y1:0.341, x2:0, y2:0, stop:0 rgba(74, 138, 255, 255), stop:0.5 rgba(106, 208, 225, 255), stop:1 rgba(74, 138, 255, 255));\n"
"     border: 1px solid #e1b190;\n"
"     padding:6px 0px 6px 0px;\n"
"     border-radius: 5px;\n"
"     color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(74, 138, 255, 255), stop:0.5 rgba(106, 208, 225, 255), stop:1 rgba(74, 138, 255, 255));\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(74, 138, 255, 255), stop:0.5 rgba(196, 232, 237, 255), stop:1 rgba(74, 138, 255, 255));\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: white;\n"
"    color: rgb(128, 128, 128);\n"
"}")
        self.Start_thread.setObjectName("Start_thread")
        self.verticalLayout.addWidget(self.Start_thread)
        self.Continue_thread = QtWidgets.QPushButton(self.groupBox)
        self.Continue_thread.setStyleSheet("QPushButton {\n"
"     background-color: qlineargradient(spread:pad, x1:0, y1:0.341, x2:0, y2:0, stop:0 rgba(74, 138, 255, 255), stop:0.5 rgba(106, 208, 225, 255), stop:1 rgba(74, 138, 255, 255));\n"
"     border: 1px solid #e1b190;\n"
"     padding:6px 0px 6px 0px;\n"
"     border-radius: 5px;\n"
"     color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(74, 138, 255, 255), stop:0.5 rgba(106, 208, 225, 255), stop:1 rgba(74, 138, 255, 255));\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(74, 138, 255, 255), stop:0.5 rgba(196, 232, 237, 255), stop:1 rgba(74, 138, 255, 255));\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: white;\n"
"    color: rgb(128, 128, 128);\n"
"}")
        self.Continue_thread.setObjectName("Continue_thread")
        self.verticalLayout.addWidget(self.Continue_thread)
        self.Pause_thread = QtWidgets.QPushButton(self.groupBox)
        self.Pause_thread.setStyleSheet("QPushButton {\n"
"     background-color: qlineargradient(spread:pad, x1:0, y1:0.341, x2:0, y2:0, stop:0 rgba(74, 138, 255, 255), stop:0.5 rgba(106, 208, 225, 255), stop:1 rgba(74, 138, 255, 255));\n"
"     border: 1px solid #e1b190;\n"
"     padding:6px 0px 6px 0px;\n"
"     border-radius: 5px;\n"
"     color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(74, 138, 255, 255), stop:0.5 rgba(106, 208, 225, 255), stop:1 rgba(74, 138, 255, 255));\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(74, 138, 255, 255), stop:0.5 rgba(196, 232, 237, 255), stop:1 rgba(74, 138, 255, 255));\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: white;\n"
"    color: rgb(128, 128, 128);\n"
"}")
        self.Pause_thread.setObjectName("Pause_thread")
        self.verticalLayout.addWidget(self.Pause_thread)
        self.Stop_thread = QtWidgets.QPushButton(self.groupBox)
        self.Stop_thread.setStyleSheet("QPushButton {\n"
"     background-color: qlineargradient(spread:pad, x1:0, y1:0.341, x2:0, y2:0, stop:0 rgba(74, 138, 255, 255), stop:0.5 rgba(106, 208, 225, 255), stop:1 rgba(74, 138, 255, 255));\n"
"     border: 1px solid #e1b190;\n"
"     padding:6px 0px 6px 0px;\n"
"     border-radius: 5px;\n"
"     color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(74, 138, 255, 255), stop:0.5 rgba(106, 208, 225, 255), stop:1 rgba(74, 138, 255, 255));\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(74, 138, 255, 255), stop:0.5 rgba(196, 232, 237, 255), stop:1 rgba(74, 138, 255, 255));\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: white;\n"
"    color: rgb(128, 128, 128);\n"
"}")
        self.Stop_thread.setObjectName("Stop_thread")
        self.verticalLayout.addWidget(self.Stop_thread)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
"    margin-top: -2px;\n"
"    \n"
"}\n"
"QTabWidget::tab-bar {\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: rgb(128,128,128);\n"
"    min-width: 40px;\n"
"    height: 28px;\n"
"    border-width: 0px 18px 0 18px;\n"
"    border-image: url(:/icon/tab-inactive.png) 0 18 0 18 stretch stretch;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    color: rgb(0, 0,0);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    color: rgb(0,0,0);\n"
"    height: 28px;\n"
"    border-width: 0px 18px 0 18px;\n"
"    border-image: url(:/icon/tab-active.png) 0 18 0 18 stretch stretch;\n"
"}\n"
"\n"
"QTabBar::tab:!first {\n"
"    margin-left: -20px;\n"
"}\n"
"\n"
"/*整数框*/\n"
"QSpinBox{\n"
"border:2px solid #c1fcff;\n"
"padding:0 4px;\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QSpinBox:hover{\n"
"border:2px solid #f58093;\n"
"}\n"
"QSpinBox:disabled{\n"
"color: rgb(230, 230, 230);\n"
"background-color:rgb(150, 150, 150);\n"
"}\n"
"QSpinBox[buttonSymbols=\"0\"]::up-button{/*显示按钮=0*/\n"
"width:14px;\n"
"height:14px;\n"
"subcontrol-origin:border;\n"
"subcontrol-position:top right;\n"
"right:4px;\n"
"top:2px;\n"
"border-image: url(:/icon/uparrows.png);\n"
"}\n"
"QSpinBox::up-button:hover{\n"
"border-image: url(:/icon/uparrows_hover.png);\n"
"}\n"
"QSpinBox::up-button:pressed{\n"
"}\n"
"QSpinBox[buttonSymbols=\"0\"]::down-button{\n"
"width:14px;\n"
"height:14px;\n"
"subcontrol-origin:border;\n"
"subcontrol-position:bottom right;\n"
"right:4px;\n"
"bottom:2px;\n"
"border-image: url(:/icon/downarrows.png);\n"
"}\n"
"QSpinBox::down-button:hover{\n"
"width:16px;\n"
"height:16px;\n"
"right:2px;\n"
"bottom:1px;\n"
"border-image: url(:/icon/downarrows_hover.png);\n"
"}\n"
"QSpinBox::down-button:pressed{\n"
"}\n"
"\n"
"QLineEdit {\n"
"padding: 4px 8px;\n"
"border:2px solid #c1fcff;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"border:2px solid #f58093;\n"
"}\n"
"\n"
"QTextEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border-radius: 4px;\n"
"border:2px solid #c1fcff;\n"
"}\n"
"\n"
"QTextEdit:hover {\n"
"border:2px solid #c1e8ff;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"subcontrol-origin: border;\n"
"subcontrol-position: left center;\n"
"background: white;\n"
"border-radius: 3px;\n"
"border:2px solid rgb(0, 0, 0);\n"
"}\n"
"QCheckBox::indicator:checked { \n"
"background: rgb(76, 76, 76);\n"
"} \n"
"\n"
"QComboBox {\n"
"    border:2px solid #c1fcff;\n"
"    border-radius: 3px;\n"
"    padding: 4px 8px;\n"
"    min-width: 9em; \n"
"}\n"
"\n"
"QComboBox:hover {\n"
"border:2px solid #f58093;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background-color: rgba(255, 251, 247,255);\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    right: 4px;\n"
"    width: 16px;\n"
"    border-image: url(:/icon/downarrows.png);\n"
"}\n"
"\n"
"QComboBox::drop-down:hover{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"    border-image: url(:/icon/downarrows_hover.png);\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QLabel {\n"
"border-radius: 4px;\n"
"background-color: rgba(0, 170, 255,128);\n"
"color: rgb(255, 255, 255);\n"
"font-weight：bold;\n"
"font: 12pt \"Arial\";\n"
"padding: 5px 8px;\n"
"}\n"
"\n"
"QTableWidget{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border-radius: 4px;\n"
"}\n"
" \n"
"QPushButton {\n"
"     font-size: 12px;\n"
"     background-color: rgb(74, 138, 255);\n"
"     border: 1px solid #e1b190;\n"
"     border-width: 1px;\n"
"     padding: 3px;\n"
"     border-radius: 7;\n"
"     color: white;\n"
"     padding-left: 5px;\n"
"     padding-right: 5px;\n"
"     min-width: 50px;\n"
"     max-width: 50px;\n"
"     min-height: 13px;\n"
"     max-height: 13px;\n"
"}\n"
"QPushButton:hover{        \n"
"    background-color: rgb(100, 196, 230);\n"
"}")
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("")
        self.tab.setObjectName("tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("QTextBrowser{\n"
"background-color: rgba(255, 255, 255,255);\n"
"}")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_5.addWidget(self.textBrowser)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setStyleSheet("    background-image: url();v")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.Task_tableWidget = QtWidgets.QTableWidget(self.groupBox_4)
        self.Task_tableWidget.setStyleSheet("/*表格*/\n"
"QTableView{/*对齐方式代码设置*/\n"
"border:2px solid #c1e8ff;\n"
"gridline-color: rgb(128, 128, 128);/*网格线颜色*/\n"
"background-image: url(:/icon/bg.png);\n"
"}\n"
"QTableView QTableCornerButton::section{/*表头左上*/\n"
"background-color: rgb(60,60,60);\n"
"border:0;\n"
"border-bottom:1px solid rgb(0, 170, 255);\n"
"}\n"
"QTableView::item{/*表内容*/\n"
"font: 15px \"宋体\";\n"
"color: rgb(250, 250, 250);\n"
"/*background-color: rgb(80, 80, 80);*/\n"
"}\n"
"QTableView::item:selected{\n"
"color:black;\n"
"background-color: rgb(255, 255, 188);\n"
"}\n"
"QTableView::indicator{\n"
"width: 20px;\n"
"height: 20px;\n"
"}\n"
"QTableView::indicator:enabled:checked{\n"
"image: ;\n"
"}\n"
"QTableView::indicator:enabled:unchecked{\n"
"image: ;\n"
"}")
        self.Task_tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.Task_tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.Task_tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.Task_tableWidget.setRowCount(0)
        self.Task_tableWidget.setColumnCount(3)
        self.Task_tableWidget.setObjectName("Task_tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.Task_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Task_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Task_tableWidget.setHorizontalHeaderItem(2, item)
        self.Task_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.Task_tableWidget.verticalHeader().setVisible(False)
        self.Task_tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_7.addWidget(self.Task_tableWidget)
        self.gridLayout_7.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_4, 1, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setStyleSheet("background: rgba(255, 255, 255, 0);")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.Task_progressBar = QtWidgets.QProgressBar(self.groupBox_5)
        self.Task_progressBar.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Task_progressBar.sizePolicy().hasHeightForWidth())
        self.Task_progressBar.setSizePolicy(sizePolicy)
        self.Task_progressBar.setMouseTracking(False)
        self.Task_progressBar.setTabletTracking(False)
        self.Task_progressBar.setAcceptDrops(False)
        self.Task_progressBar.setAccessibleName("")
        self.Task_progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Task_progressBar.setAutoFillBackground(False)
        self.Task_progressBar.setStyleSheet(" QProgressBar{\n"
"border-style: solid;\n"
"color: rgb(255,0, 0);\n"
"font: 12pt \"Arial\";\n"
"}\n"
"QProgressBar::chunk {\n"
"background-color: rgb(190, 219, 255);\n"
"}")
        self.Task_progressBar.setMinimum(0)
        self.Task_progressBar.setMaximum(100)
        self.Task_progressBar.setProperty("value", 0)
        self.Task_progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.Task_progressBar.setTextVisible(True)
        self.Task_progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.Task_progressBar.setInvertedAppearance(False)
        self.Task_progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.Task_progressBar.setObjectName("Task_progressBar")
        self.gridLayout_5.addWidget(self.Task_progressBar, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_5, 2, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setStyleSheet("background: rgba(255, 255, 255, 0);")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(0, 30))
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet("background-color: rgba(0, 170, 255,128);\n"
"color: rgb(255, 255, 255);")
        self.label_6.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_6.setLineWidth(1)
        self.label_6.setMidLineWidth(0)
        self.label_6.setText("掃描信息")
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setWordWrap(False)
        self.label_6.setIndent(-1)
        self.label_6.setOpenExternalLinks(False)
        self.label_6.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.Task_label_msg = QtWidgets.QLabel(self.groupBox_3)
        self.Task_label_msg.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Task_label_msg.sizePolicy().hasHeightForWidth())
        self.Task_label_msg.setSizePolicy(sizePolicy)
        self.Task_label_msg.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Task_label_msg.setFont(font)
        self.Task_label_msg.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Task_label_msg.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Task_label_msg.setAcceptDrops(False)
        self.Task_label_msg.setToolTip("")
        self.Task_label_msg.setStatusTip("")
        self.Task_label_msg.setWhatsThis("")
        self.Task_label_msg.setAccessibleName("")
        self.Task_label_msg.setAccessibleDescription("")
        self.Task_label_msg.setAutoFillBackground(False)
        self.Task_label_msg.setStyleSheet("border-bottom:1px dashed rgb(0, 170, 255);\n"
"color: rgb(128, 128, 128);\n"
"")
        self.Task_label_msg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Task_label_msg.setText("")
        self.Task_label_msg.setTextFormat(QtCore.Qt.AutoText)
        self.Task_label_msg.setWordWrap(False)
        self.Task_label_msg.setOpenExternalLinks(True)
        self.Task_label_msg.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.Task_label_msg.setObjectName("Task_label_msg")
        self.horizontalLayout_3.addWidget(self.Task_label_msg)
        self.Task_label_time = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Task_label_time.sizePolicy().hasHeightForWidth())
        self.Task_label_time.setSizePolicy(sizePolicy)
        self.Task_label_time.setMinimumSize(QtCore.QSize(120, 0))
        self.Task_label_time.setMaximumSize(QtCore.QSize(90, 16777215))
        self.Task_label_time.setStyleSheet("background: rgba(255, 255, 255, 0);\n"
"border:1px dashed rgb(0, 170, 255);\n"
"color: rgb(128, 128, 128);")
        self.Task_label_time.setText("")
        self.Task_label_time.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Task_label_time.setObjectName("Task_label_time")
        self.horizontalLayout_3.addWidget(self.Task_label_time)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 3)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout_9.setContentsMargins(0, -1, 0, 0)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet("background-color: rgba(0, 170, 255,128);\n"
"color: rgb(255, 255, 255);")
        self.label_2.setMidLineWidth(0)
        self.label_2.setObjectName("label_2")
        self.gridLayout_9.addWidget(self.label_2, 0, 0, 1, 1)
        self.Task_archiveButton = QtWidgets.QToolButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Task_archiveButton.sizePolicy().hasHeightForWidth())
        self.Task_archiveButton.setSizePolicy(sizePolicy)
        self.Task_archiveButton.setMinimumSize(QtCore.QSize(0, 30))
        self.Task_archiveButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Task_archiveButton.setStyleSheet("QToolButton {\n"
"     \n"
"    background-color: rgb(74, 138, 255);\n"
"     border: 1px solid #e1b190;\n"
"     padding:6px 0px 6px 0px;\n"
"     border-radius: 5px;\n"
"     color: rgb(255, 255, 255);\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(74, 138, 255, 255), stop:0.5 rgba(106, 208, 225, 255), stop:1 rgba(74, 138, 255, 255));\n"
"}\n"
"QToolButton:disabled {\n"
"    background-color: white;\n"
"    color: rgb(128, 128, 128);\n"
"}")
        self.Task_archiveButton.setObjectName("Task_archiveButton")
        self.gridLayout_9.addWidget(self.Task_archiveButton, 0, 2, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_9)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("background-color: rgba(0, 170, 255,128);\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.Task_spinBox_thread = QtWidgets.QSpinBox(self.groupBox_3)
        self.Task_spinBox_thread.setMinimumSize(QtCore.QSize(50, 30))
        self.Task_spinBox_thread.setAccessibleName("0")
        self.Task_spinBox_thread.setStyleSheet("background: rgba(255, 255, 255, 0);")
        self.Task_spinBox_thread.setAlignment(QtCore.Qt.AlignCenter)
        self.Task_spinBox_thread.setSuffix("")
        self.Task_spinBox_thread.setMaximum(100)
        self.Task_spinBox_thread.setProperty("value", 6)
        self.Task_spinBox_thread.setObjectName("Task_spinBox_thread")
        self.horizontalLayout_2.addWidget(self.Task_spinBox_thread)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet("background-color: rgba(0, 170, 255,128);\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.Task_spinBox_time_out = QtWidgets.QSpinBox(self.groupBox_3)
        self.Task_spinBox_time_out.setMinimumSize(QtCore.QSize(40, 30))
        self.Task_spinBox_time_out.setAccessibleName("")
        self.Task_spinBox_time_out.setStyleSheet("background: rgba(255, 255, 255, 0);")
        self.Task_spinBox_time_out.setAlignment(QtCore.Qt.AlignCenter)
        self.Task_spinBox_time_out.setSuffix("")
        self.Task_spinBox_time_out.setMaximum(15)
        self.Task_spinBox_time_out.setProperty("value", 3)
        self.Task_spinBox_time_out.setObjectName("Task_spinBox_time_out")
        self.horizontalLayout_2.addWidget(self.Task_spinBox_time_out)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_6.setStyleSheet("border:0px;border-bottom:1px dashed rgb(0, 170, 255);")
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_20.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_7 = QtWidgets.QLabel(self.groupBox_6)
        self.label_7.setStyleSheet("border:0px;\n"
"background-color: rgba(0, 170, 255,128);\n"
"color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_20.addWidget(self.label_7)
        self.Task_label_Success = QtWidgets.QLabel(self.groupBox_6)
        self.Task_label_Success.setStyleSheet("border-bottom:1px dashed rgb(0, 170, 255);\n"
"color: rgb(255, 0, 127);")
        self.Task_label_Success.setText("0")
        self.Task_label_Success.setObjectName("Task_label_Success")
        self.horizontalLayout_20.addWidget(self.Task_label_Success)
        self.label_5 = QtWidgets.QLabel(self.groupBox_6)
        self.label_5.setStyleSheet("border:0px;\n"
"background-color: rgba(0, 170, 255,128);\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_20.addWidget(self.label_5)
        self.Task_lineEdit_serial = QtWidgets.QLineEdit(self.groupBox_6)
        self.Task_lineEdit_serial.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Task_lineEdit_serial.sizePolicy().hasHeightForWidth())
        self.Task_lineEdit_serial.setSizePolicy(sizePolicy)
        self.Task_lineEdit_serial.setMinimumSize(QtCore.QSize(0, 0))
        self.Task_lineEdit_serial.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Task_lineEdit_serial.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Task_lineEdit_serial.setStyleSheet("QLineEdit{\n"
"border:0px;\n"
"border-bottom:1px dashed rgb(0, 170, 255);\n"
"background: rgba(255, 255, 255, 0);\n"
"font-weight：bold;\n"
"font: 12pt \"Arial\";\n"
"padding:0px;\n"
"color: rgb(236, 168, 172);\n"
"}\n"
"QLineEdit:hover{\n"
"border:1px dashed rgb(0, 170, 255)\n"
"}\n"
"\n"
"")
        self.Task_lineEdit_serial.setText("0")
        self.Task_lineEdit_serial.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Task_lineEdit_serial.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.Task_lineEdit_serial.setObjectName("Task_lineEdit_serial")
        self.horizontalLayout_20.addWidget(self.Task_lineEdit_serial)
        self.label_9 = QtWidgets.QLabel(self.groupBox_6)
        self.label_9.setMinimumSize(QtCore.QSize(0, 0))
        self.label_9.setStyleSheet("background: rgba(255, 255, 255, 0);\n"
"color: rgb(128, 128, 128);\n"
"padding:0px;")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_20.addWidget(self.label_9)
        self.Task_lineEdit_file_number = QtWidgets.QLabel(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Task_lineEdit_file_number.sizePolicy().hasHeightForWidth())
        self.Task_lineEdit_file_number.setSizePolicy(sizePolicy)
        self.Task_lineEdit_file_number.setMinimumSize(QtCore.QSize(30, 0))
        self.Task_lineEdit_file_number.setStyleSheet("border-bottom:1px dashed rgb(0, 170, 255);\n"
"color: rgb(255, 0, 127);\n"
"padding:0px;")
        self.Task_lineEdit_file_number.setText("0")
        self.Task_lineEdit_file_number.setAlignment(QtCore.Qt.AlignCenter)
        self.Task_lineEdit_file_number.setObjectName("Task_lineEdit_file_number")
        self.horizontalLayout_20.addWidget(self.Task_lineEdit_file_number)
        self.verticalLayout_9.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_2.addWidget(self.groupBox_6)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.gridLayout_3.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_7.setStyleSheet("    background-image: url();")
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Plus_tableWidget_item = QtWidgets.QTableWidget(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Plus_tableWidget_item.sizePolicy().hasHeightForWidth())
        self.Plus_tableWidget_item.setSizePolicy(sizePolicy)
        self.Plus_tableWidget_item.setMinimumSize(QtCore.QSize(150, 0))
        self.Plus_tableWidget_item.setStatusTip("")
        self.Plus_tableWidget_item.setWhatsThis("")
        self.Plus_tableWidget_item.setAccessibleName("")
        self.Plus_tableWidget_item.setStyleSheet("/*表格*/\n"
"QTableView{/*对齐方式代码设置*/\n"
"border:2px solid #c1e8ff;\n"
"gridline-color: rgb(128, 128, 128);/*网格线颜色*/\n"
"background-image: url(:/icon/bg.png);\n"
"}\n"
"QTableView QTableCornerButton::section{/*表头左上*/\n"
"background-color: rgb(60,60,60);\n"
"border:0;\n"
"border-bottom:1px solid rgb(0, 170, 255);\n"
"}\n"
"QTableView::item{/*表内容*/\n"
"font: 15px \"宋体\";\n"
"color: rgb(0, 0, 0);\n"
"/*background-color: rgb(255, 230, 238);*/\n"
"}\n"
"QTableView::item:selected{\n"
"color:black;\n"
"background-color: rgb(255, 255, 188);\n"
"}\n"
"QTableView::indicator{\n"
"width: 20px;\n"
"height: 20px;\n"
"}\n"
"QTableView::indicator:enabled:checked{\n"
"image: ;\n"
"}\n"
"QTableView::indicator:enabled:unchecked{\n"
"image: ;\n"
"}")
        self.Plus_tableWidget_item.setGridStyle(QtCore.Qt.NoPen)
        self.Plus_tableWidget_item.setRowCount(0)
        self.Plus_tableWidget_item.setColumnCount(1)
        self.Plus_tableWidget_item.setObjectName("Plus_tableWidget_item")
        item = QtWidgets.QTableWidgetItem()
        self.Plus_tableWidget_item.setHorizontalHeaderItem(0, item)
        self.Plus_tableWidget_item.horizontalHeader().setDefaultSectionSize(150)
        self.Plus_tableWidget_item.verticalHeader().setVisible(False)
        self.verticalLayout_8.addWidget(self.Plus_tableWidget_item)
        self.horizontalLayout_4.addWidget(self.groupBox_7)
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.groupBox_8.setFont(font)
        self.groupBox_8.setStyleSheet("    background-image: url();")
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_8 = QtWidgets.QLabel(self.groupBox_8)
        self.label_8.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("")
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_13.addWidget(self.label_8)
        self.Plus_lineEdit_name = QtWidgets.QLineEdit(self.groupBox_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Plus_lineEdit_name.setFont(font)
        self.Plus_lineEdit_name.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Plus_lineEdit_name.setStyleSheet("background: rgba(255, 255, 255, 0);")
        self.Plus_lineEdit_name.setObjectName("Plus_lineEdit_name")
        self.horizontalLayout_13.addWidget(self.Plus_lineEdit_name)
        self.verticalLayout_11.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_19 = QtWidgets.QLabel(self.groupBox_8)
        self.label_19.setMinimumSize(QtCore.QSize(120, 0))
        self.label_19.setStyleSheet("")
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_14.addWidget(self.label_19)
        self.Plus_spinBox_number = QtWidgets.QSpinBox(self.groupBox_8)
        self.Plus_spinBox_number.setMinimumSize(QtCore.QSize(40, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Plus_spinBox_number.setFont(font)
        self.Plus_spinBox_number.setStyleSheet("background-color: rgba(255, 251, 247,0);")
        self.Plus_spinBox_number.setAlignment(QtCore.Qt.AlignCenter)
        self.Plus_spinBox_number.setSuffix("")
        self.Plus_spinBox_number.setMinimum(1)
        self.Plus_spinBox_number.setMaximum(3)
        self.Plus_spinBox_number.setObjectName("Plus_spinBox_number")
        self.horizontalLayout_14.addWidget(self.Plus_spinBox_number)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem2)
        self.label_21 = QtWidgets.QLabel(self.groupBox_8)
        self.label_21.setStyleSheet("")
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_14.addWidget(self.label_21)
        self.Plus_comboBox_Type = QtWidgets.QComboBox(self.groupBox_8)
        self.Plus_comboBox_Type.setMinimumSize(QtCore.QSize(128, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Plus_comboBox_Type.setFont(font)
        self.Plus_comboBox_Type.setStyleSheet("QComboBox:disabled{\n"
"background-color: rgba(255, 251, 247,0);\n"
"}\n"
"QComboBox:editable{\n"
"background-color: rgba(255, 251, 247,0);\n"
"}\n"
"QComboBox:editable:disabled{\n"
"background-color: rgba(255, 251, 247,0);\n"
"}\n"
"QComboBox QAbstractItemView{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox::drop-down {\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.Plus_comboBox_Type.setObjectName("Plus_comboBox_Type")
        self.Plus_comboBox_Type.addItem("")
        self.Plus_comboBox_Type.addItem("")
        self.Plus_comboBox_Type.addItem("")
        self.horizontalLayout_14.addWidget(self.Plus_comboBox_Type)
        self.Plus_comboBox_request_Type = QtWidgets.QComboBox(self.groupBox_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Plus_comboBox_request_Type.setFont(font)
        self.Plus_comboBox_request_Type.setStyleSheet("QComboBox:disabled{\n"
"background-color: rgba(255, 251, 247,0);\n"
"}\n"
"QComboBox:editable{\n"
"background-color: rgba(255, 251, 247,0);\n"
"}\n"
"QComboBox:editable:disabled{\n"
"background-color: rgba(255, 251, 247,0);\n"
"}\n"
"QComboBox QAbstractItemView{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox::drop-down {\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.Plus_comboBox_request_Type.setObjectName("Plus_comboBox_request_Type")
        self.Plus_comboBox_request_Type.addItem("")
        self.Plus_comboBox_request_Type.addItem("")
        self.horizontalLayout_14.addWidget(self.Plus_comboBox_request_Type)
        self.verticalLayout_11.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_11 = QtWidgets.QLabel(self.groupBox_8)
        self.label_11.setMinimumSize(QtCore.QSize(120, 0))
        self.label_11.setStyleSheet("")
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_6.addWidget(self.label_11)
        self.Plus_lineEdit_insert = QtWidgets.QLineEdit(self.groupBox_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Plus_lineEdit_insert.setFont(font)
        self.Plus_lineEdit_insert.setStyleSheet("background: rgba(255, 255, 255, 0);")
        self.Plus_lineEdit_insert.setObjectName("Plus_lineEdit_insert")
        self.horizontalLayout_6.addWidget(self.Plus_lineEdit_insert)
        self.Plus_spinBox_insert_number = QtWidgets.QSpinBox(self.groupBox_8)
        self.Plus_spinBox_insert_number.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Plus_spinBox_insert_number.sizePolicy().hasHeightForWidth())
        self.Plus_spinBox_insert_number.setSizePolicy(sizePolicy)
        self.Plus_spinBox_insert_number.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Plus_spinBox_insert_number.setFont(font)
        self.Plus_spinBox_insert_number.setMouseTracking(False)
        self.Plus_spinBox_insert_number.setTabletTracking(False)
        self.Plus_spinBox_insert_number.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.Plus_spinBox_insert_number.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Plus_spinBox_insert_number.setStyleSheet("background-color: rgba(255, 251, 247,0);")
        self.Plus_spinBox_insert_number.setWrapping(False)
        self.Plus_spinBox_insert_number.setFrame(True)
        self.Plus_spinBox_insert_number.setAlignment(QtCore.Qt.AlignCenter)
        self.Plus_spinBox_insert_number.setReadOnly(False)
        self.Plus_spinBox_insert_number.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.Plus_spinBox_insert_number.setSpecialValueText("")
        self.Plus_spinBox_insert_number.setAccelerated(False)
        self.Plus_spinBox_insert_number.setProperty("showGroupSeparator", False)
        self.Plus_spinBox_insert_number.setSuffix("")
        self.Plus_spinBox_insert_number.setMinimum(1)
        self.Plus_spinBox_insert_number.setMaximum(3)
        self.Plus_spinBox_insert_number.setSingleStep(1)
        self.Plus_spinBox_insert_number.setProperty("value", 1)
        self.Plus_spinBox_insert_number.setObjectName("Plus_spinBox_insert_number")
        self.horizontalLayout_6.addWidget(self.Plus_spinBox_insert_number)
        self.Plus_checkBox_carry = QtWidgets.QCheckBox(self.groupBox_8)
        self.Plus_checkBox_carry.setStyleSheet("background: rgba(255, 255, 255, 0);")
        self.Plus_checkBox_carry.setObjectName("Plus_checkBox_carry")
        self.horizontalLayout_6.addWidget(self.Plus_checkBox_carry)
        self.Plus_pushButton_insert = QtWidgets.QPushButton(self.groupBox_8)
        self.Plus_pushButton_insert.setObjectName("Plus_pushButton_insert")
        self.horizontalLayout_6.addWidget(self.Plus_pushButton_insert)
        self.Plus_pushButton_delete = QtWidgets.QPushButton(self.groupBox_8)
        self.Plus_pushButton_delete.setObjectName("Plus_pushButton_delete")
        self.horizontalLayout_6.addWidget(self.Plus_pushButton_delete)
        self.verticalLayout_11.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_17 = QtWidgets.QLabel(self.groupBox_8)
        self.label_17.setMinimumSize(QtCore.QSize(120, 0))
        self.label_17.setStyleSheet("background: rgba(255, 255, 255, 0);")
        self.label_17.setText("")
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_18.addWidget(self.label_17)
        self.Plus_tableWidget_path_list = QtWidgets.QTableWidget(self.groupBox_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Plus_tableWidget_path_list.setFont(font)
        self.Plus_tableWidget_path_list.setStyleSheet("/*表格*/\n"
"QTableView{/*对齐方式代码设置*/\n"
"border:2px solid #c1e8ff;\n"
"gridline-color: rgb(128, 128, 128);/*网格线颜色*/\n"
"background-image: url(:/icon/bg.png);\n"
"}\n"
"QTableView QTableCornerButton::section{/*表头左上*/\n"
"background-color: rgb(60,60,60);\n"
"border:0;\n"
"border-bottom:1px solid rgb(0, 170, 255);\n"
"}\n"
"QTableView::item{/*表内容*/\n"
"font: 15px \"宋体\";\n"
"color: rgb(0, 0, 0);\n"
"/*background-color: rgb(80, 80, 80);*/\n"
"}\n"
"QTableView::item:selected{\n"
"color:black;\n"
"background-color: rgb(255, 255, 188);\n"
"}\n"
"QTableView::indicator{\n"
"width: 20px;\n"
"height: 20px;\n"
"}\n"
"QTableView::indicator:enabled:checked{\n"
"image: ;\n"
"}\n"
"QTableView::indicator:enabled:unchecked{\n"
"image: ;\n"
"}")
        self.Plus_tableWidget_path_list.setGridStyle(QtCore.Qt.NoPen)
        self.Plus_tableWidget_path_list.setObjectName("Plus_tableWidget_path_list")
        self.Plus_tableWidget_path_list.setColumnCount(3)
        self.Plus_tableWidget_path_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Plus_tableWidget_path_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Plus_tableWidget_path_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Plus_tableWidget_path_list.setHorizontalHeaderItem(2, item)
        self.Plus_tableWidget_path_list.horizontalHeader().setCascadingSectionResizes(False)
        self.Plus_tableWidget_path_list.horizontalHeader().setHighlightSections(True)
        self.Plus_tableWidget_path_list.horizontalHeader().setSortIndicatorShown(False)
        self.Plus_tableWidget_path_list.horizontalHeader().setStretchLastSection(True)
        self.Plus_tableWidget_path_list.verticalHeader().setVisible(False)
        self.horizontalLayout_18.addWidget(self.Plus_tableWidget_path_list)
        self.verticalLayout_11.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.Plus_label_url = QtWidgets.QLabel(self.groupBox_8)
        self.Plus_label_url.setMinimumSize(QtCore.QSize(120, 0))
        self.Plus_label_url.setStyleSheet("")
        self.Plus_label_url.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Plus_label_url.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Plus_label_url.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Plus_label_url.setObjectName("Plus_label_url")
        self.horizontalLayout_11.addWidget(self.Plus_label_url)
        self.Plus_lineEdit_url_Variable = QtWidgets.QLineEdit(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Plus_lineEdit_url_Variable.sizePolicy().hasHeightForWidth())
        self.Plus_lineEdit_url_Variable.setSizePolicy(sizePolicy)
        self.Plus_lineEdit_url_Variable.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Plus_lineEdit_url_Variable.setFont(font)
        self.Plus_lineEdit_url_Variable.setStyleSheet("background: rgba(255, 255, 255, 0);")
        self.Plus_lineEdit_url_Variable.setText("")
        self.Plus_lineEdit_url_Variable.setObjectName("Plus_lineEdit_url_Variable")
        self.horizontalLayout_11.addWidget(self.Plus_lineEdit_url_Variable)
        self.Plus_lineEdit_url = QtWidgets.QLineEdit(self.groupBox_8)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.Plus_lineEdit_url.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Plus_lineEdit_url.setFont(font)
        self.Plus_lineEdit_url.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Plus_lineEdit_url.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Plus_lineEdit_url.setAcceptDrops(True)
        self.Plus_lineEdit_url.setToolTip("")
        self.Plus_lineEdit_url.setStatusTip("")
        self.Plus_lineEdit_url.setWhatsThis("")
        self.Plus_lineEdit_url.setAccessibleName("")
        self.Plus_lineEdit_url.setAccessibleDescription("")
        self.Plus_lineEdit_url.setAutoFillBackground(False)
        self.Plus_lineEdit_url.setStyleSheet("background: rgba(255, 255, 255, 0);")
        self.Plus_lineEdit_url.setInputMask("")
        self.Plus_lineEdit_url.setCursorPosition(0)
        self.Plus_lineEdit_url.setDragEnabled(False)
        self.Plus_lineEdit_url.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.Plus_lineEdit_url.setClearButtonEnabled(False)
        self.Plus_lineEdit_url.setObjectName("Plus_lineEdit_url")
        self.horizontalLayout_11.addWidget(self.Plus_lineEdit_url)
        self.verticalLayout_11.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.Plus_label_path = QtWidgets.QLabel(self.groupBox_8)
        self.Plus_label_path.setMinimumSize(QtCore.QSize(120, 0))
        self.Plus_label_path.setStyleSheet("")
        self.Plus_label_path.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Plus_label_path.setObjectName("Plus_label_path")
        self.horizontalLayout_19.addWidget(self.Plus_label_path)
        self.Plus_lineEdit_path_Variable = QtWidgets.QLineEdit(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Plus_lineEdit_path_Variable.sizePolicy().hasHeightForWidth())
        self.Plus_lineEdit_path_Variable.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Plus_lineEdit_path_Variable.setFont(font)
        self.Plus_lineEdit_path_Variable.setStyleSheet("background: rgba(255, 255, 255, 0);")
        self.Plus_lineEdit_path_Variable.setObjectName("Plus_lineEdit_path_Variable")
        self.horizontalLayout_19.addWidget(self.Plus_lineEdit_path_Variable)
        self.Plus_lineEdit_path = QtWidgets.QLineEdit(self.groupBox_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Plus_lineEdit_path.setFont(font)
        self.Plus_lineEdit_path.setStyleSheet("background: rgba(255, 255, 255, 0);")
        self.Plus_lineEdit_path.setObjectName("Plus_lineEdit_path")
        self.horizontalLayout_19.addWidget(self.Plus_lineEdit_path)
        self.Plus_comboBox_path_type = QtWidgets.QComboBox(self.groupBox_8)
        self.Plus_comboBox_path_type.setMinimumSize(QtCore.QSize(128, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.Plus_comboBox_path_type.setFont(font)
        self.Plus_comboBox_path_type.setStyleSheet("background-color: rgb(255, 251, 247);")
        self.Plus_comboBox_path_type.setObjectName("Plus_comboBox_path_type")
        self.Plus_comboBox_path_type.addItem("")
        self.Plus_comboBox_path_type.addItem("")
        self.horizontalLayout_19.addWidget(self.Plus_comboBox_path_type)
        self.verticalLayout_11.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_12 = QtWidgets.QLabel(self.groupBox_8)
        self.label_12.setMinimumSize(QtCore.QSize(120, 0))
        self.label_12.setStyleSheet("")
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_9.addWidget(self.label_12)
        self.Plus_lineEdit_feature_Text = QtWidgets.QLineEdit(self.groupBox_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Plus_lineEdit_feature_Text.setFont(font)
        self.Plus_lineEdit_feature_Text.setStyleSheet("background: rgba(255, 255, 255, 0);")
        self.Plus_lineEdit_feature_Text.setObjectName("Plus_lineEdit_feature_Text")
        self.horizontalLayout_9.addWidget(self.Plus_lineEdit_feature_Text)
        self.verticalLayout_11.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_13 = QtWidgets.QLabel(self.groupBox_8)
        self.label_13.setMinimumSize(QtCore.QSize(120, 0))
        self.label_13.setStyleSheet("")
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_15.addWidget(self.label_13)
        self.Plus_lineEdit_exclude_Text = QtWidgets.QLineEdit(self.groupBox_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Plus_lineEdit_exclude_Text.setFont(font)
        self.Plus_lineEdit_exclude_Text.setStyleSheet("background: rgba(255, 255, 255, 0);")
        self.Plus_lineEdit_exclude_Text.setObjectName("Plus_lineEdit_exclude_Text")
        self.horizontalLayout_15.addWidget(self.Plus_lineEdit_exclude_Text)
        self.verticalLayout_11.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_14 = QtWidgets.QLabel(self.groupBox_8)
        self.label_14.setMinimumSize(QtCore.QSize(120, 0))
        self.label_14.setStyleSheet("")
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_8.addWidget(self.label_14)
        self.Plus_lineEdit_FileName = QtWidgets.QLineEdit(self.groupBox_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Plus_lineEdit_FileName.setFont(font)
        self.Plus_lineEdit_FileName.setStyleSheet("background: rgba(255, 255, 255, 0);")
        self.Plus_lineEdit_FileName.setObjectName("Plus_lineEdit_FileName")
        self.horizontalLayout_8.addWidget(self.Plus_lineEdit_FileName)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_8)
        self.comboBox.setStyleSheet("background-color: rgba(255, 251, 247,0);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox)
        self.verticalLayout_11.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_16 = QtWidgets.QLabel(self.groupBox_8)
        self.label_16.setMinimumSize(QtCore.QSize(120, 0))
        self.label_16.setStyleSheet("")
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_10.addWidget(self.label_16)
        self.Plus_checkBox_domain = QtWidgets.QCheckBox(self.groupBox_8)
        self.Plus_checkBox_domain.setStyleSheet("background: rgba(255, 255, 255, 0);")
        self.Plus_checkBox_domain.setObjectName("Plus_checkBox_domain")
        self.horizontalLayout_10.addWidget(self.Plus_checkBox_domain)
        self.Plus_checkBox_result = QtWidgets.QCheckBox(self.groupBox_8)
        self.Plus_checkBox_result.setStyleSheet("background: rgba(255, 255, 255, 0);")
        self.Plus_checkBox_result.setObjectName("Plus_checkBox_result")
        self.horizontalLayout_10.addWidget(self.Plus_checkBox_result)
        self.Plus_lineEdit_custom = QtWidgets.QLineEdit(self.groupBox_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.Plus_lineEdit_custom.setFont(font)
        self.Plus_lineEdit_custom.setStyleSheet("background: rgba(255, 255, 255, 0);")
        self.Plus_lineEdit_custom.setObjectName("Plus_lineEdit_custom")
        self.horizontalLayout_10.addWidget(self.Plus_lineEdit_custom)
        self.verticalLayout_11.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_10 = QtWidgets.QLabel(self.groupBox_8)
        self.label_10.setMinimumSize(QtCore.QSize(120, 0))
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setAutoFillBackground(False)
        self.label_10.setStyleSheet("")
        self.label_10.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_10.setText("POST參數")
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_16.addWidget(self.label_10)
        self.Plus_textEdit_POST = QtWidgets.QTextEdit(self.groupBox_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Plus_textEdit_POST.setFont(font)
        self.Plus_textEdit_POST.setStyleSheet("background: rgba(255, 255, 255, 0);")
        self.Plus_textEdit_POST.setObjectName("Plus_textEdit_POST")
        self.horizontalLayout_16.addWidget(self.Plus_textEdit_POST)
        self.verticalLayout_11.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_20 = QtWidgets.QLabel(self.groupBox_8)
        self.label_20.setMinimumSize(QtCore.QSize(120, 0))
        self.label_20.setStyleSheet("")
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_7.addWidget(self.label_20)
        self.Plus_textEdit_Headers = QtWidgets.QTextEdit(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Plus_textEdit_Headers.sizePolicy().hasHeightForWidth())
        self.Plus_textEdit_Headers.setSizePolicy(sizePolicy)
        self.Plus_textEdit_Headers.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Plus_textEdit_Headers.setFont(font)
        self.Plus_textEdit_Headers.setStyleSheet("background: rgba(255, 255, 255, 0);")
        self.Plus_textEdit_Headers.setObjectName("Plus_textEdit_Headers")
        self.horizontalLayout_7.addWidget(self.Plus_textEdit_Headers)
        self.verticalLayout_11.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_18 = QtWidgets.QLabel(self.groupBox_8)
        self.label_18.setMinimumSize(QtCore.QSize(120, 0))
        self.label_18.setStyleSheet("")
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_12.addWidget(self.label_18)
        self.Plus_textEdit_vote = QtWidgets.QTextEdit(self.groupBox_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Plus_textEdit_vote.setFont(font)
        self.Plus_textEdit_vote.setStyleSheet("background: rgba(255, 255, 255, 0);")
        self.Plus_textEdit_vote.setObjectName("Plus_textEdit_vote")
        self.horizontalLayout_12.addWidget(self.Plus_textEdit_vote)
        self.verticalLayout_11.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem3)
        self.Plus_pushButton_save = QtWidgets.QPushButton(self.groupBox_8)
        self.Plus_pushButton_save.setMinimumSize(QtCore.QSize(62, 21))
        self.Plus_pushButton_save.setToolTip("")
        self.Plus_pushButton_save.setStatusTip("")
        self.Plus_pushButton_save.setWhatsThis("")
        self.Plus_pushButton_save.setAccessibleName("")
        self.Plus_pushButton_save.setObjectName("Plus_pushButton_save")
        self.horizontalLayout_17.addWidget(self.Plus_pushButton_save)
        self.verticalLayout_11.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_4.addWidget(self.groupBox_8)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setStyleSheet("    background-image: url();")
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.management_tableWidget_item = QtWidgets.QTableWidget(self.tab_3)
        self.management_tableWidget_item.setStyleSheet("/*表格*/\n"
"QTableView{/*对齐方式代码设置*/\n"
"border:2px solid #c1e8ff;\n"
"gridline-color: rgb(128, 128, 128);/*网格线颜色*/\n"
"background-image: url(:/icon/bg.png);\n"
"}\n"
"QTableView QTableCornerButton::section{/*表头左上*/\n"
"background-color: rgb(60,60,60);\n"
"border:0;\n"
"border-bottom:1px solid rgb(0, 170, 255);\n"
"}\n"
"QTableView::item{/*表内容*/\n"
"font: 15px \"宋体\";\n"
"color: rgb(0, 0, 0);\n"
"/*background-color: rgb(80, 80, 80);*/\n"
"}\n"
"QTableView::item:selected{\n"
"color:black;\n"
"background-color: rgb(255, 255, 188);\n"
"}\n"
"QTableView::indicator{\n"
"width: 20px;\n"
"height: 20px;\n"
"}\n"
"QTableView::indicator:enabled:checked{\n"
"image: ;\n"
"}\n"
"QTableView::indicator:enabled:unchecked{\n"
"image: ;\n"
"}")
        self.management_tableWidget_item.setGridStyle(QtCore.Qt.NoPen)
        self.management_tableWidget_item.setObjectName("management_tableWidget_item")
        self.management_tableWidget_item.setColumnCount(3)
        self.management_tableWidget_item.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.management_tableWidget_item.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.management_tableWidget_item.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.management_tableWidget_item.setHorizontalHeaderItem(2, item)
        self.management_tableWidget_item.horizontalHeader().setStretchLastSection(True)
        self.management_tableWidget_item.verticalHeader().setVisible(False)
        self.management_tableWidget_item.verticalHeader().setCascadingSectionResizes(False)
        self.management_tableWidget_item.verticalHeader().setHighlightSections(True)
        self.management_tableWidget_item.verticalHeader().setSortIndicatorShown(False)
        self.management_tableWidget_item.verticalHeader().setStretchLastSection(False)
        self.gridLayout_4.addWidget(self.management_tableWidget_item, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.logs_tableWidget_item = QtWidgets.QTableWidget(self.tab_5)
        self.logs_tableWidget_item.setStyleSheet("/*表格*/\n"
"QTableView{/*对齐方式代码设置*/\n"
"border:2px solid #c1e8ff;\n"
"gridline-color: rgb(128, 128, 128);/*网格线颜色*/\n"
"background-image: url(:/icon/bg.png);\n"
"}\n"
"QTableView QTableCornerButton::section{/*表头左上*/\n"
"background-color: rgb(60,60,60);\n"
"border:0;\n"
"border-bottom:1px solid rgb(0, 170, 255);\n"
"}\n"
"QTableView::item{/*表内容*/\n"
"font: 15px \"宋体\";\n"
"color: rgb(0, 0, 0);\n"
"/*background-color: rgb(80, 80, 80);*/\n"
"}\n"
"QTableView::item:selected{\n"
"color:black;\n"
"background-color: rgb(255, 255, 188);\n"
"}\n"
"QTableView::indicator{\n"
"width: 20px;\n"
"height: 20px;\n"
"}\n"
"QTableView::indicator:enabled:checked{\n"
"image: ;\n"
"}\n"
"QTableView::indicator:enabled:unchecked{\n"
"image: ;\n"
"}")
        self.logs_tableWidget_item.setGridStyle(QtCore.Qt.NoPen)
        self.logs_tableWidget_item.setObjectName("logs_tableWidget_item")
        self.logs_tableWidget_item.setColumnCount(6)
        self.logs_tableWidget_item.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.logs_tableWidget_item.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.logs_tableWidget_item.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.logs_tableWidget_item.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.logs_tableWidget_item.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.logs_tableWidget_item.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.logs_tableWidget_item.setHorizontalHeaderItem(5, item)
        self.logs_tableWidget_item.horizontalHeader().setSortIndicatorShown(False)
        self.logs_tableWidget_item.horizontalHeader().setStretchLastSection(True)
        self.logs_tableWidget_item.verticalHeader().setVisible(False)
        self.gridLayout_8.addWidget(self.logs_tableWidget_item, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.gridLayout.addLayout(self.verticalLayout_4, 1, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_15.setAutoFillBackground(False)
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap(":/icon/bg.png"))
        self.label_15.setScaledContents(False)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Seo Post 1.6 《駭到你心裡》By Lucas"))
        self.label.setText(_translate("MainWindow", "SEO POST"))
        self.Start_thread.setText(_translate("MainWindow", "開始線程"))
        self.Continue_thread.setText(_translate("MainWindow", "繼續線程"))
        self.Pause_thread.setText(_translate("MainWindow", "暫停線程"))
        self.Stop_thread.setText(_translate("MainWindow", "停止線程"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'PMingLiU\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">版本更新資訊</span></p>\n"
"<hr />\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  版本1.0  -  2018/12/20  -   Seo Post 1.0 《駭到你心裡》By Lucas</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">              1.更新介面，新增CMS插件</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<hr />\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  版本1.1 -  2018/12/21  -   Seo Post 1.1 《駭到你心裡》By Lucas</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                          </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">              1.新增檔案上傳注入。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">              2.多線程與超時參數已可使用。              </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">              3.限制程式處理隊列(100)，隊列未滿 0.1秒 ，隊列已滿 0.5秒，以節省系統資源。</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<hr />\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  版本1.2 -  2018/1/9  -   Seo Post 1.2 《駭到你心裡》By Lucas</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                           </p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">              1.移除爆破機功能</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">              2.移除檔案注入</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">              3.多線程優化(新增協程)</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<hr />\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  版本1.3 -  2018/1/10  -   Seo Post 1.3 《駭到你心裡》By Lucas</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                           </p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">              1.新增檔案注入</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">              2.介面業務邏輯優化</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  </p>\n"
"<hr />\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">版本1.4 -  2018/1/11  -   Seo Post 1.4 《駭到你心裡》By Lucas</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                           </p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">              1.已修復檔案進度BUG</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">              2.新增資源監視器</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">              3.介面美化</p>\n"
"<hr />\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">版本1.5 -  2018/1/12  -   Seo Post 1.5 《駭到你心裡》By Lucas</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">              1.介面配色修改</p>\n"
"<hr />\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">版本1.6 -  2018/1/13  -   Seo Post 1.6 《駭到你心裡》By Lucas</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">              1.新增拖曳網址功能</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">              2.新增系統日誌功能</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "官方訊息"))
        self.Task_tableWidget.setSortingEnabled(False)
        item = self.Task_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.Task_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "HTTP Status"))
        item = self.Task_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "網址"))
        self.Task_progressBar.setFormat(_translate("MainWindow", "%p%"))
        self.label_2.setText(_translate("MainWindow", "文件"))
        self.Task_archiveButton.setText(_translate("MainWindow", "打開文件"))
        self.label_3.setText(_translate("MainWindow", "線程"))
        self.label_4.setText(_translate("MainWindow", "超時："))
        self.label_7.setText(_translate("MainWindow", "成功數量："))
        self.label_5.setText(_translate("MainWindow", "掃描進度："))
        self.label_9.setText(_translate("MainWindow", "/"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "任務"))
        item = self.Plus_tableWidget_item.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "插件名稱"))
        self.label_8.setText(_translate("MainWindow", "插件名稱"))
        self.label_19.setText(_translate("MainWindow", "請求次數"))
        self.label_21.setText(_translate("MainWindow", "漏洞類型"))
        self.Plus_comboBox_Type.setItemText(0, _translate("MainWindow", "一般"))
        self.Plus_comboBox_Type.setItemText(1, _translate("MainWindow", "遠程寫入"))
        self.Plus_comboBox_Type.setItemText(2, _translate("MainWindow", "檔案上傳"))
        self.Plus_comboBox_request_Type.setItemText(0, _translate("MainWindow", "GET"))
        self.Plus_comboBox_request_Type.setItemText(1, _translate("MainWindow", "POST"))
        self.label_11.setText(_translate("MainWindow", "請求路徑"))
        self.Plus_checkBox_carry.setText(_translate("MainWindow", "攜帶參數"))
        self.Plus_pushButton_insert.setText(_translate("MainWindow", "插入"))
        self.Plus_pushButton_delete.setText(_translate("MainWindow", "刪除"))
        item = self.Plus_tableWidget_path_list.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.Plus_tableWidget_path_list.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "參數"))
        item = self.Plus_tableWidget_path_list.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "網址"))
        self.Plus_label_url.setText(_translate("MainWindow", "小馬網址"))
        self.Plus_lineEdit_url_Variable.setPlaceholderText(_translate("MainWindow", "小馬變數名稱"))
        self.Plus_lineEdit_url.setPlaceholderText(_translate("MainWindow", "遠程寫入"))
        self.Plus_label_path.setText(_translate("MainWindow", "檔案路徑"))
        self.Plus_lineEdit_path_Variable.setPlaceholderText(_translate("MainWindow", "檔案變數名稱"))
        self.Plus_lineEdit_path.setPlaceholderText(_translate("MainWindow", "檔案上傳"))
        self.Plus_comboBox_path_type.setItemText(0, _translate("MainWindow", "r"))
        self.Plus_comboBox_path_type.setItemText(1, _translate("MainWindow", "rb"))
        self.label_12.setText(_translate("MainWindow", "特徵文本"))
        self.Plus_lineEdit_feature_Text.setPlaceholderText(_translate("MainWindow", "支援正則語法"))
        self.label_13.setText(_translate("MainWindow", "排除文本"))
        self.Plus_lineEdit_exclude_Text.setPlaceholderText(_translate("MainWindow", "暫時無作用"))
        self.label_14.setText(_translate("MainWindow", "導出文件名"))
        self.comboBox.setItemText(0, _translate("MainWindow", ".txt"))
        self.label_16.setText(_translate("MainWindow", "導出格式"))
        self.Plus_checkBox_domain.setText(_translate("MainWindow", "域名"))
        self.Plus_checkBox_result.setText(_translate("MainWindow", "結果 +"))
        self.label_20.setText(_translate("MainWindow", "Headers"))
        self.Plus_textEdit_Headers.setPlaceholderText(_translate("MainWindow", "特殊用途，例如Ecshop就是用這個注入的"))
        self.label_18.setText(_translate("MainWindow", "備註說明"))
        self.Plus_textEdit_vote.setPlaceholderText(_translate("MainWindow", "漏洞的使用說明請寫在這"))
        self.Plus_pushButton_save.setText(_translate("MainWindow", "保存"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "插件配置"))
        item = self.management_tableWidget_item.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "PID"))
        item = self.management_tableWidget_item.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "耗時"))
        item = self.management_tableWidget_item.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "狀態"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "資源監視器"))
        item = self.logs_tableWidget_item.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.logs_tableWidget_item.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "CMS"))
        item = self.logs_tableWidget_item.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "開始時間"))
        item = self.logs_tableWidget_item.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "結束時間"))
        item = self.logs_tableWidget_item.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "進度"))
        item = self.logs_tableWidget_item.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "數據"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "系統日誌"))
