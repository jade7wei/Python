# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIDesign_new.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ComPort = QtWidgets.QLabel(self.centralwidget)
        self.ComPort.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.ComPort.setObjectName("ComPort")
        self.PortNum = QtWidgets.QComboBox(self.centralwidget)
        self.PortNum.setGeometry(QtCore.QRect(50, 30, 69, 22))
        self.PortNum.setEditable(False)
        self.PortNum.setObjectName("PortNum")
        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton.setEnabled(False)
        self.StartButton.setGeometry(QtCore.QRect(30, 340, 75, 23))
        self.StartButton.setCheckable(False)
        self.StartButton.setAutoRepeat(False)
        self.StartButton.setObjectName("StartButton")
        self.ReleaseButton = QtWidgets.QPushButton(self.centralwidget)
        self.ReleaseButton.setEnabled(False)
        self.ReleaseButton.setGeometry(QtCore.QRect(120, 340, 75, 23))
        self.ReleaseButton.setObjectName("ReleaseButton")
        self.FrontButton = QtWidgets.QPushButton(self.centralwidget)
        self.FrontButton.setEnabled(False)
        self.FrontButton.setGeometry(QtCore.QRect(80, 370, 75, 23))
        self.FrontButton.setObjectName("FrontButton")
        self.LeftButton = QtWidgets.QPushButton(self.centralwidget)
        self.LeftButton.setEnabled(False)
        self.LeftButton.setGeometry(QtCore.QRect(30, 400, 75, 23))
        self.LeftButton.setObjectName("LeftButton")
        self.RightButton = QtWidgets.QPushButton(self.centralwidget)
        self.RightButton.setEnabled(False)
        self.RightButton.setGeometry(QtCore.QRect(120, 400, 75, 23))
        self.RightButton.setObjectName("RightButton")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setEnabled(False)
        self.BackButton.setGeometry(QtCore.QRect(80, 430, 75, 23))
        self.BackButton.setObjectName("BackButton")
        self.OpenButton = QtWidgets.QPushButton(self.centralwidget)
        self.OpenButton.setEnabled(True)
        self.OpenButton.setGeometry(QtCore.QRect(50, 60, 41, 23))
        self.OpenButton.setObjectName("OpenButton")
        self.CloseButton = QtWidgets.QPushButton(self.centralwidget)
        self.CloseButton.setEnabled(False)
        self.CloseButton.setGeometry(QtCore.QRect(100, 60, 41, 23))
        self.CloseButton.setObjectName("CloseButton")
        self.Datatext = QtWidgets.QTextEdit(self.centralwidget)
        self.Datatext.setGeometry(QtCore.QRect(390, 50, 401, 451))
        self.Datatext.setObjectName("Datatext")
        self.Datalabel = QtWidgets.QLabel(self.centralwidget)
        self.Datalabel.setGeometry(QtCore.QRect(390, 30, 54, 16))
        self.Datalabel.setObjectName("Datalabel")
        self.Ratelabel = QtWidgets.QLabel(self.centralwidget)
        self.Ratelabel.setGeometry(QtCore.QRect(10, 90, 41, 20))
        self.Ratelabel.setObjectName("Ratelabel")
        self.DataBitelabel = QtWidgets.QLabel(self.centralwidget)
        self.DataBitelabel.setGeometry(QtCore.QRect(10, 122, 54, 20))
        self.DataBitelabel.setObjectName("DataBitelabel")
        self.Paritylabel = QtWidgets.QLabel(self.centralwidget)
        self.Paritylabel.setGeometry(QtCore.QRect(10, 150, 41, 20))
        self.Paritylabel.setObjectName("Paritylabel")
        self.StopBitlabel = QtWidgets.QLabel(self.centralwidget)
        self.StopBitlabel.setGeometry(QtCore.QRect(10, 180, 41, 20))
        self.StopBitlabel.setObjectName("StopBitlabel")
        self.RateBox = QtWidgets.QComboBox(self.centralwidget)
        self.RateBox.setGeometry(QtCore.QRect(50, 90, 69, 21))
        self.RateBox.setObjectName("RateBox")
        self.RateBox.addItem("")
        self.RateBox.addItem("")
        self.RateBox.addItem("")
        self.DataBiteBox = QtWidgets.QComboBox(self.centralwidget)
        self.DataBiteBox.setGeometry(QtCore.QRect(50, 120, 69, 22))
        self.DataBiteBox.setObjectName("DataBiteBox")
        self.DataBiteBox.addItem("")
        self.DataBiteBox.addItem("")
        self.DataBiteBox.addItem("")
        self.DataBiteBox.addItem("")
        self.ParityBox = QtWidgets.QComboBox(self.centralwidget)
        self.ParityBox.setGeometry(QtCore.QRect(50, 150, 69, 22))
        self.ParityBox.setObjectName("ParityBox")
        self.ParityBox.addItem("")
        self.ParityBox.addItem("")
        self.ParityBox.addItem("")
        self.StopBiteBox = QtWidgets.QComboBox(self.centralwidget)
        self.StopBiteBox.setGeometry(QtCore.QRect(50, 180, 69, 22))
        self.StopBiteBox.setObjectName("StopBiteBox")
        self.StopBiteBox.addItem("")
        self.StopBiteBox.addItem("")
        self.StopBiteBox.addItem("")
        self.CheckButton = QtWidgets.QPushButton(self.centralwidget)
        self.CheckButton.setGeometry(QtCore.QRect(130, 30, 41, 23))
        self.CheckButton.setObjectName("CheckButton")
        self.ClearButton = QtWidgets.QPushButton(self.centralwidget)
        self.ClearButton.setGeometry(QtCore.QRect(720, 510, 71, 23))
        self.ClearButton.setObjectName("ClearButton")
        self.SaveBox = QtWidgets.QCheckBox(self.centralwidget)
        self.SaveBox.setGeometry(QtCore.QRect(420, 510, 71, 16))
        self.SaveBox.setObjectName("SaveBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 530, 41, 16))
        self.label.setObjectName("label")
        self.RoomidLine = QtWidgets.QLineEdit(self.centralwidget)
        self.RoomidLine.setGeometry(QtCore.QRect(460, 530, 91, 20))
        self.RoomidLine.setObjectName("RoomidLine")
        self.SaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveButton.setGeometry(QtCore.QRect(560, 530, 31, 23))
        self.SaveButton.setObjectName("SaveButton")
        self.Start_text = QtWidgets.QLineEdit(self.centralwidget)
        self.Start_text.setGeometry(QtCore.QRect(30, 220, 81, 20))
        self.Start_text.setObjectName("Start_text")
        self.Release_text = QtWidgets.QLineEdit(self.centralwidget)
        self.Release_text.setGeometry(QtCore.QRect(130, 220, 81, 20))
        self.Release_text.setObjectName("Release_text")
        self.Front_text = QtWidgets.QLineEdit(self.centralwidget)
        self.Front_text.setGeometry(QtCore.QRect(80, 250, 81, 20))
        self.Front_text.setObjectName("Front_text")
        self.Left_text = QtWidgets.QLineEdit(self.centralwidget)
        self.Left_text.setGeometry(QtCore.QRect(30, 280, 81, 20))
        self.Left_text.setObjectName("Left_text")
        self.Right_text = QtWidgets.QLineEdit(self.centralwidget)
        self.Right_text.setGeometry(QtCore.QRect(130, 280, 81, 20))
        self.Right_text.setObjectName("Right_text")
        self.Back_text = QtWidgets.QLineEdit(self.centralwidget)
        self.Back_text.setGeometry(QtCore.QRect(80, 310, 81, 20))
        self.Back_text.setObjectName("Back_text")
        self.Input_text = QtWidgets.QLineEdit(self.centralwidget)
        self.Input_text.setGeometry(QtCore.QRect(60, 470, 181, 20))
        self.Input_text.setText("")
        self.Input_text.setObjectName("Input_text")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 470, 51, 16))
        self.label_2.setObjectName("label_2")
        self.CALButton = QtWidgets.QPushButton(self.centralwidget)
        self.CALButton.setGeometry(QtCore.QRect(250, 470, 41, 23))
        self.CALButton.setObjectName("CALButton")
        self.machine_box = QtWidgets.QComboBox(self.centralwidget)
        self.machine_box.setGeometry(QtCore.QRect(270, 60, 61, 22))
        self.machine_box.setObjectName("machine_box")
        self.machine_box.addItem("")
        self.machine_box.addItem("")
        self.machine_box.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 60, 51, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 30, 54, 21))
        self.label_4.setObjectName("label_4")
        self.method_test = QtWidgets.QComboBox(self.centralwidget)
        self.method_test.setGeometry(QtCore.QRect(270, 30, 61, 22))
        self.method_test.setObjectName("method_test")
        self.method_test.addItem("")
        self.method_test.addItem("")
        self.Count_text = QtWidgets.QLineEdit(self.centralwidget)
        self.Count_text.setGeometry(QtCore.QRect(660, 510, 51, 21))
        self.Count_text.setObjectName("Count_text")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(610, 510, 54, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(680, 30, 31, 20))
        self.label_6.setObjectName("label_6")
        self.Score_text = QtWidgets.QLineEdit(self.centralwidget)
        self.Score_text.setGeometry(QtCore.QRect(710, 30, 81, 16))
        self.Score_text.setObjectName("Score_text")
        self.Stop_text = QtWidgets.QLineEdit(self.centralwidget)
        self.Stop_text.setGeometry(QtCore.QRect(60, 500, 113, 20))
        self.Stop_text.setObjectName("Stop_text")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 500, 31, 16))
        self.label_7.setObjectName("label_7")
        self.StopButton = QtWidgets.QPushButton(self.centralwidget)
        self.StopButton.setGeometry(QtCore.QRect(180, 500, 41, 23))
        self.StopButton.setObjectName("StopButton")
        self.TestBox = QtWidgets.QCheckBox(self.centralwidget)
        self.TestBox.setGeometry(QtCore.QRect(260, 90, 71, 21))
        self.TestBox.setObjectName("TestBox")
        self.TstartButton = QtWidgets.QPushButton(self.centralwidget)
        self.TstartButton.setGeometry(QtCore.QRect(340, 90, 41, 23))
        self.TstartButton.setObjectName("TstartButton")
        self.TCount_text = QtWidgets.QLineEdit(self.centralwidget)
        self.TCount_text.setGeometry(QtCore.QRect(270, 120, 71, 21))
        self.TCount_text.setObjectName("TCount_text")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(220, 120, 51, 21))
        self.label_8.setObjectName("label_8")
        self.input_data = QtWidgets.QLineEdit(self.centralwidget)
        self.input_data.setGeometry(QtCore.QRect(60, 530, 181, 20))
        self.input_data.setText("")
        self.input_data.setObjectName("input_data")
        self.SendButton = QtWidgets.QPushButton(self.centralwidget)
        self.SendButton.setGeometry(QtCore.QRect(250, 530, 51, 23))
        self.SendButton.setObjectName("SendButton")
        #MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        #MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UartTest"))
        self.ComPort.setText(_translate("MainWindow", "端口号"))
        self.StartButton.setText(_translate("MainWindow", "开始"))
        self.ReleaseButton.setText(_translate("MainWindow", "松抓"))
        self.FrontButton.setText(_translate("MainWindow", "前"))
        self.LeftButton.setText(_translate("MainWindow", "左"))
        self.RightButton.setText(_translate("MainWindow", "右"))
        self.BackButton.setText(_translate("MainWindow", "后"))
        self.OpenButton.setText(_translate("MainWindow", "OPEN"))
        self.CloseButton.setText(_translate("MainWindow", "CLOSE"))
        self.Datalabel.setText(_translate("MainWindow", "收发区"))
        self.Ratelabel.setText(_translate("MainWindow", "波特率"))
        self.DataBitelabel.setText(_translate("MainWindow", "数据位"))
        self.Paritylabel.setText(_translate("MainWindow", "校验位"))
        self.StopBitlabel.setText(_translate("MainWindow", "停止位"))
        self.RateBox.setItemText(0, _translate("MainWindow", "38400"))
        self.RateBox.setItemText(1, _translate("MainWindow", "9600"))
        self.RateBox.setItemText(2, _translate("MainWindow", "115200"))
        self.DataBiteBox.setItemText(0, _translate("MainWindow", "8"))
        self.DataBiteBox.setItemText(1, _translate("MainWindow", "7"))
        self.DataBiteBox.setItemText(2, _translate("MainWindow", "6"))
        self.DataBiteBox.setItemText(3, _translate("MainWindow", "5"))
        self.ParityBox.setItemText(0, _translate("MainWindow", "NONE"))
        self.ParityBox.setItemText(1, _translate("MainWindow", "ODD"))
        self.ParityBox.setItemText(2, _translate("MainWindow", "EVEN"))
        self.StopBiteBox.setItemText(0, _translate("MainWindow", "1"))
        self.StopBiteBox.setItemText(1, _translate("MainWindow", "2"))
        self.StopBiteBox.setItemText(2, _translate("MainWindow", "3"))
        self.CheckButton.setText(_translate("MainWindow", "检测"))
        self.ClearButton.setText(_translate("MainWindow", "Clear"))
        self.SaveBox.setText(_translate("MainWindow", "保存日志"))
        self.label.setText(_translate("MainWindow", "房间号"))
        self.SaveButton.setText(_translate("MainWindow", "保存"))
        self.Start_text.setText(_translate("MainWindow", "0370A2"))
        self.Release_text.setText(_translate("MainWindow", "0570330600"))
        self.Front_text.setText(_translate("MainWindow", "0570330101"))
        self.Left_text.setText(_translate("MainWindow", "0570330301"))
        self.Right_text.setText(_translate("MainWindow", "0570330401"))
        self.Back_text.setText(_translate("MainWindow", "0570330201"))
        self.label_2.setText(_translate("MainWindow", "异或校验"))
        self.CALButton.setText(_translate("MainWindow", "计算"))
        self.machine_box.setItemText(0, _translate("MainWindow", "掉球机"))
        self.machine_box.setItemText(1, _translate("MainWindow", "篮球机"))
        self.machine_box.setItemText(2, _translate("MainWindow", "娃娃机"))
        self.label_3.setText(_translate("MainWindow", "机器类型"))
        self.label_4.setText(_translate("MainWindow", "测试方式"))
        self.method_test.setItemText(0, _translate("MainWindow", "串口"))
        self.method_test.setItemText(1, _translate("MainWindow", "Web"))
        self.label_5.setText(_translate("MainWindow", "游戏次数"))
        self.label_6.setText(_translate("MainWindow", "得分"))
        self.Stop_text.setText(_translate("MainWindow", "0570330500"))
        self.label_7.setText(_translate("MainWindow", "停止"))
        self.StopButton.setText(_translate("MainWindow", "发送"))
        self.TestBox.setText(_translate("MainWindow", "自动测试"))
        self.TstartButton.setText(_translate("MainWindow", "开始"))
        self.label_8.setText(_translate("MainWindow", "测试次数"))
        self.SendButton.setText(_translate("MainWindow", "发送Hex"))

