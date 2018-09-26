#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-26 10:24:57
# @Author  : Jade7Wei (jade7wei@126.com)
# @Link    : https://git.com/jade7wei
# @Version : $Id$

import sys
import serial
import threading
import binascii 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox,QMainWindow, QPushButton , QWidget , QApplication, QHBoxLayout
from UIDesign_new import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import serial.tools.list_ports
import time
import requests

class Pyqt5_Serial(QtWidgets.QWidget,Ui_MainWindow):
	ser = serial.Serial()
	def __init__(self):
		super(Pyqt5_Serial,self).__init__()
		self.setupUi(self)
		#游戏次数初始值
		self.i = 1
		self.init()

	def init(self):
		self.port_check()
		self.CheckButton.clicked.connect(self.port_check)
		self.OpenButton.clicked.connect(self.port_open)
		self.CloseButton.clicked.connect(self.port_close)
		self.machine_box.currentIndexChanged.connect(self.machine_data)
		self.StartButton.clicked.connect(self.wawaji_test)
		self.ReleaseButton.clicked.connect(lambda:self.uartsend_data(self.Release_text.text()))
		self.FrontButton.pressed.connect(lambda:self.uartsend_data(self.Front_text.text()))
		self.FrontButton.released.connect(lambda:self.uartsend_data(self.Stop_text.text()))
		self.BackButton.pressed.connect(lambda:self.uartsend_data(self.Back_text.text()))
		self.BackButton.released.connect(lambda:self.uartsend_data(self.Stop_text.text()))
		self.LeftButton.pressed.connect(lambda:self.uartsend_data(self.Left_text.text()))
		self.LeftButton.released.connect(lambda:self.uartsend_data(self.Stop_text.text()))
		self.RightButton.pressed.connect(lambda:self.uartsend_data(self.Right_text.text()))
		self.RightButton.released.connect(lambda:self.uartsend_data(self.Stop_text.text()))
		self.CALButton.clicked.connect(lambda:self.textxor_CAL(self.Input_text.text()))
		self.StopButton.clicked.connect(lambda:self.uartsend_data(self.Stop_text.text()))
		self.ClearButton.clicked.connect(self.clear_data)
		self.StartButton.clicked.connect(self.count_data)
		self.SaveButton.clicked.connect(self.save_text)
		self.method_test.currentIndexChanged.connect(self.way_test)
		self.TstartButton.clicked.connect(self.auto_test)
		self.SendButton.clicked.connect(self.sendtext_data)

	#检测串口
	def port_check(self):
		Com_List=[]
		port_list = list(serial.tools.list_ports.comports())
		self.PortNum.clear()
		for port in port_list:
			Com_List.append(port[0])
			self.PortNum.addItem(port[0])
			self.Datatext.append("检测到串口")
		if(len(Com_List) == 0):
			self.Datatext.append("未检测到串口")

	#打开串口
	def port_open(self):
		self.ser.port = self.PortNum.currentText()
		self.ser.baudrate = int(self.RateBox.currentText())
		self.ser.bytesize = int(self.DataBiteBox.currentText())
		self.ser.stopbits = int(self.StopBiteBox.currentText())
		ParityValue = self.ParityBox.currentText()
		self.ser.parity = ParityValue[0]
		try:
			self.ser.open()
			self.OpenButton.setEnabled(False)
			self.Datatext.append("打开成功")
			#创建一个线程
			self.t1 = threading.Thread(target=self.receive_data)
			#声明为守护线程
			self.t1.setDaemon(True)
			self.t1.start()
			self.CloseButton.setEnabled(True)
			self.Button_Open()
		except:
			self.Datatext.append("打开失败")

	#关闭串口
	def port_close(self):
		
		try:
			self.ser.close()
			self.CloseButton.setEnabled(False)
			self.Datatext.append("关闭成功")
		except:
			self.CloseButton.setEnabled(False)
			self.Datatext.append("关闭成功")
		self.OpenButton.setEnabled(True)
		self.Button_Close()

	#机器类型
	def machine_data(self):
		if(self.machine_box.currentText() == '娃娃机'):
			self.Start_text.setText('0570330101')
			self.Release_text.setText('0570330600')
			self.Front_text.setText('0570330101')
			self.Back_text.setText('0570330201')
			self.Left_text.setText('0570330301')
			self.Right_text.setText('0570330401')
			self.ReleaseButton.setText('下抓')

		elif(self.machine_box.currentText() == "篮球机"):
			self.Start_text.setText('037001')
			self.Release_text.setText('037002')
			self.Front_text.setText('')
			self.Back_text.setText('')
			self.Left_text.setText('')
			self.Right_text.setText('')

			self.ReleaseButton.setText("发球")
			self.FrontButton.setText('')
			self.BackButton.setText('')
			self.LeftButton.setText('')
			self.RightButton.setText('')

	#打开控制按钮
	def Button_Open(self):
		self.StartButton.setEnabled(True)
		self.ReleaseButton.setEnabled(True)
		self.FrontButton.setEnabled(True)
		self.BackButton.setEnabled(True)
		self.LeftButton.setEnabled(True)
		self.RightButton.setEnabled(True)

	#关闭控制按钮
	def Button_Close(self):
		self.StartButton.setEnabled(False)
		self.ReleaseButton.setEnabled(False)
		self.FrontButton.setEnabled(False)
		self.BackButton.setEnabled(False)
		self.LeftButton.setEnabled(False)
		self.RightButton.setEnabled(False)

	#异或校验
	def XOR_data(self,a):
		n = len(a)
		b = int(a[0:2],16)
		c = int(a[2:4],16)
		d = b^c
		i = 4
		while i < n:
			g = int(a[i:i+2],16)
			d = d^g
			i +=2
			e = hex(d)
			c = e[2:4]
		f = a + c
		return f

	#文本框异或校验
	def textxor_CAL(self,Befor_data):
		try:
			Afterxor_data = self.XOR_data(Befor_data)
			After_data = "aa" + Afterxor_data +"dd"
			self.Datatext.append(After_data)
		except:
			self.Datatext.append("ValuError")

	#串口发送数据
	def uartsend_data(self,name_text):
		try:
			get_data = self.XOR_data(name_text)
			send_data = "aa" + get_data + "dd"
			if(self.method_test.currentText() == "串口"):
				if(self.ser.isOpen()):
					self.ser.write(binascii.a2b_hex(send_data))
					self.Datatext.append(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + " 发送：" + send_data)
					self.ser.flushOutput()
				else:
					self.Datatext.append("PortError")
			elif(self.method_test.currentText() == "Web"):
				if(self.RoomidLine.text() != ""):
					roomid = self.RoomidLine.text()
					url = "http://iot.artqiyi.com:9510/api/device/control?mac=" + roomid + "&raw=" + send_data
					req = requests.get(url)
					self.Datatext.append(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + " 发送：" + send_data)
					self.Datatext.append(req.text)
				else:
					self.Datatext.append("请输入房间号")
		except:
			self.Datatext.append("ValueError")
	#发送输入数据
	def sendtext_data(self):
		try:
			if(self.input_data.text() != ""):
				if(self.method_test.currentText() == "串口"):
					if(self.ser.isOpen()):
						self.ser.write(binascii.a2b_hex(self.input_data.text()))
						self.Datatext.append(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + " 发送：" + self.input_data.text())
						self.ser.flushOutput()
					else:
						self.Datatext.append("PortError")
			else:
				self.Datatext.append("请输入指令")
		except:
			self.Datatext.append("ValuError")

			
	#娃娃机开始按钮
	def wawaji_test(self):
		if(self.machine_box.currentText() == "娃娃机"):
			self.uartsend_data(self.Start_text.text())
			self.uartsend_data(self.Stop_text.text())
		else:
			self.uartsend_data(self.Start_text.text())

	#测试方式选择
	def way_test(self):
		if(self.method_test.currentText() == "Web"):
			self.Button_Open()

	#接收数据
	def receive_data(self):
		res_data = ''
		num = 0
		while(self.ser.isOpen()):
			size = self.ser.inWaiting()
			if size:
				res_data = self.ser.read_all()
				self.ser.flushInput()
				num += 1
				self.Datatext.append(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + " 接收：" + binascii.b2a_hex(res_data).decode())

	#清除数据
	def clear_data(self):
		self.Datatext.clear()
		self.Count_text.setText('0')

	#游戏次数
	def count_data(self):
		self.Count_text.setText('%d' %self.i)
		self.i += 1

	#自动测试
	def auto_test(self):
		#self.TstartButton.setEnabled(False)
		if(self.TestBox.isChecked()):
			self.machine_data()
			#self.Button_Close()
			if self.TCount_text.text() != "":
				a = self.TCount_text.text()
				j = int(a)
				while j > 0:
					j = j - 1
					c = str(j)
					self.Datatext.append("第" + str(int(a)-j) + "次测试：")
					self.TCount_text.setText(c)

					if self.machine_box.currentText() == "篮球机":
						self.wawaji_test()
						for b in range(10):
							QApplication.processEvents() 
							self.uartsend_data(self.Release_text.text())
							time.sleep(0.5)

					elif self.machine_box.currentData() == "娃娃机":
						self.wawaji_test()
						time.sleep(1)
						self.uartsend_data(self.Right_text.text())
						QApplication.processEvents() 
						time.sleep(2)
						self.uartsend_data(self.Stop_text.text())
						self.uartsend_data(self.Front_text.text())
						QApplication.processEvents()
						time.sleep(2)
						self.uartsend_data(self.Stop_text.text())
						self.uartsend_data(self.Left_text.text())
						QApplication.processEvents()
						time.sleep(2)
						self.uartsend_data(self.Stop_text.text())
						self.uartsend_data(self.Release_text.text())
						QApplication.processEvents()
						time.sleep(7)
					#掉球机
					else:
						self.wawaji_test()
						time.sleep(1)
						self.uartsend_data(self.Right_text.text())
						QApplication.processEvents() 
						time.sleep(2)
						self.uartsend_data(self.Stop_text.text())
						self.uartsend_data(self.Back_text.text())
						QApplication.processEvents()
						time.sleep(2)
						self.uartsend_data(self.Stop_text.text())
						self.uartsend_data(self.Left_text.text())
						QApplication.processEvents()
						time.sleep(2)
						self.uartsend_data(self.Stop_text.text())
						self.uartsend_data(self.Release_text.text())
						QApplication.processEvents()
						time.sleep(7)
					
				self.Datatext.append("测试结束，测试次数：" + a)
			else:
				self.Datatext.append("请输入游戏次数")
		else:
			self.Datatext.append("请选择自动测试")

	#保存日志
	def save_text(self):
		if(self.SaveBox.isChecked()):
			if self.RoomidLine.text() != "":
				filename = self.RoomidLine.text() + '.txt'
				with open(filename,'w') as f:
					f.write(self.Datatext.toPlainText())
					self.Datatext.append("保存成功")	
			else:
				self.Datatext.append("请输入房间号")
		else:
			self.Datatext.append("请选择保存日志")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myshow = Pyqt5_Serial()
    myshow.show()
    sys.exit(app.exec_())