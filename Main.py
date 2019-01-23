import os,re,sys

# 界面文件为 MainWindow.py
from MainWindow import *

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLineEdit ,QAction, QTableWidget, QFileDialog, QTableWidgetItem ,QVBoxLayout ,QMessageBox

# 計時器 QBasicTimer , 獲取時間 QTime
from PyQt5.QtCore import QBasicTimer, QTime,Qt

# 調用 ico 
from PyQt5.QtGui import QIcon , QPixmap

# 執行緒
from PyQt5 import QtCore

# 打包用
import PyQt5.sip

# 自定義
import Module.plus as plus

# 多線程，隊列
import queue as Queue
import threading
import time

# 協程
from gevent import monkey; monkey.patch_all()
from gevent.pool import Pool
import gevent

# 多進程
import multiprocessing

from Module.plus import DropLineEdit

# 圖標打包 Qrc 
# 指令如下
# pyrcc5 -o resources_rc.py resources_rc.qrc
import resources_rc

import requests

# 設定與編碼
import configparser,codecs

'''
修改原始UI文件
# Label 文件
		self.label_2.setObjectName("label_2")
		self.gridLayout_9.addWidget(self.label_2, 0, 0, 1, 1)
# Button 打開文件
		self.Task_archiveButton.setObjectName("Task_archiveButton")
		self.gridLayout_9.addWidget(self.Task_archiveButton, 0, 2, 1, 1)
'''

queueLock = threading.Lock()
workQueue = object
shell_Queue = Queue.Queue()
result_Queue = Queue.Queue()
threads = []
threadID = 1

class resultThread(threading.Thread):
	def __init__(self,config):
		threading.Thread.__init__(self)
		self.exitFlag = 0
		self.config = config
		self.thread_state = False
	def set(self,Tag):
		if Tag == "exitFlag" and self.thread_state == False:
			self.exitFlag = 1
	def run(self):
		while not self.exitFlag:
			
			r = result_Queue.get()

			self.thread_state = True

			pid = r.pid
			url = r.url
			domain = r.domain
			HTTP_Status = r.status_code
			html = r.text
			Qdata = {"id":pid,"HTTP_Status":HTTP_Status,"url":url,"shell":""}

			print("編號",pid,"處理中-資料長度",result_Queue.qsize())

			time.sleep(3)

			# test start
			
			group_shell = ""

			group_shell = group_shell + domain

			group_shell = group_shell + self.config["導出結果-自定義"]
			# 最終小馬地址
			Qdata["shell"] = group_shell

			shell_Queue.put(Qdata)

			# test end

			# 正則表達式
			res = re.compile(self.config["特徵文本"]).findall(html.lower())
			res_count = len(res)
			#print(self.config["特徵文本"])
			#print("是否符合資格",res_count)
			if res_count > 0:
				
				group_shell = ""
				
				if self.config["導出格式-域名"] == "True":
					group_shell = group_shell + domain

				if self.config["導出格式-結果"] == "True":
					group_shell = group_shell + res[0]

				group_shell = group_shell + self.config["導出結果-自定義"]
				# 最終小馬地址
				Qdata["shell"] = group_shell
				#print("有沒有小馬",Qdata)
				shell_Queue.put(Qdata)
				#print("檢查隊列有沒有小馬",result_Queue.get())

			self.thread_state = False

			time.sleep(2)

#線程
class dataThread(threading.Thread):
	def __init__(self , threadID , config , q , Referer , timeout , data , signal , signal_thread_state , data_max_count , files = ["",""]):
		threading.Thread.__init__(self)
		self.exitFlag = 0
		self.s = requests.Session()
		self.s.headers.update({'referer': str(Referer)})
		self.config = config
		self.threadID = threadID
		self.q = q
		self.timeout = timeout
		self.data = data
		# ["判斷是否有檔案變數",files物件]
		self.files = files

		# 跑的進度
		self.signal = signal
		self.data_max_count = data_max_count

		# 資源監控器關閉 節省CPU資源
		config = configparser.ConfigParser()
		config.readfp(codecs.open("config.ini","r","utf-8-sig"))
		switch = config['config']['Resource_Monitor_Switch']

		# 資源監視器 開關 預設關閉
		self.signal_thread_switch = switch

		# 資源監視器 狀態
		self.signal_thread_state = signal_thread_state

		# 資源監視器 線程是否使用中 預設 False
		self.thread_state = False

		# 資源監視器 耗時 預設為0
		self.time_consuming = float(0)

		if self.signal_thread_switch == "ON":
			# 資源監視器 信號
			self.signal_thread_state.emit(int(threadID),float(0),self.thread_state,)

	def set(self,Tag):
		if Tag == "exitFlag" and self.thread_state == False:
			self.exitFlag = 1

	def run(self):
		self.process_data(self.s,self.threadID, self.q)

	def session(self,pid, path_pid , path_max ,s,domain,path):

		if  not self.exitFlag:

			url = "error"
			t1 = time.time()

			#print("編號",pid,"處理前-資料長度",result_Queue.qsize())

			try:
				# 多線程 是否閒置狀態
				self.thread_state = True

				self.signal_thread_state.emit(int(self.threadID),self.time_consuming,self.thread_state)

				url = domain + path
				HTTP_Status = 0

				url = url.encode('utf-8').decode('utf-8-sig')
				
				if self.files[0] != "":
					#print("檔案注入")
					r = s.post( url , files = self.files[1] , data = self.data ,timeout = self.timeout)
				else:
					#print("非檔案注入")
					r = s.post( url , data = self.data ,timeout = self.timeout)

				r.pid = pid
				r.url = url
				r.domain = domain

				HTTP_Status = r.status_code

				if (HTTP_Status == 200) and (path_pid == path_max):
					result_Queue.put(r)
			except:
				pass

			self.signal.emit(str(url))
			self.thread_state = False
			if self.signal_thread_switch == "ON":
				t2 = time.time()
				self.time_consuming = float(t2-t1)
				self.signal_thread_state.emit(int(self.threadID),self.time_consuming,self.thread_state)
			gevent.sleep(1)
		else:
			self.thread_state = False
			if self.signal_thread_switch == "ON":
				self.time_consuming = float(t2-t1)
				self.signal_thread_state.emit(int(self.threadID),self.time_consuming,self.thread_state)

	# 數據
	def process_data(self,s,threadID, q):

		pool = Pool(20)

		while not self.exitFlag:
			queueLock.acquire()
			if not workQueue.empty():
				#print ("Starting " + self.threadID)
				datas = q.get()
				#print("設定檢查",self.config)
				#print("POPT檢查",self.data)
				#print("資料檢查",datas)
				queueLock.release()

				pid = datas[0]
				domains = datas[1]
				paths = datas[2]

				# 防止重覆輸出
				path_max = len(paths)
				path_pid = 1
				for path in paths:

					if self.files[0] != "":
						#print("檔案注入")
						jobs = [pool.spawn(self.session, pid , path_pid , path_max , s ,domains[i] , path[2]) for i in range(len(domains))]
						gevent.joinall(jobs)
					else:
						#print("非檔案注入")
						jobs = [pool.spawn(self.session, pid , path_pid , path_max , s ,domains[i] , path[2]) for i in range(len(domains))]
						gevent.joinall(jobs)
					path_pid = path_pid + 1

				# 接收到 停止 訊號 ，清空任務列表，回收資源

				if self.exitFlag:
					#print("準備退出-Queue-未清空",workQueue.qsize())
					with workQueue.mutex:
						workQueue.queue.clear()
					#print("Queue-已清空",workQueue.qsize())
					workQueue.task_done()
					break

				#print ("%s processing url: %s data: %s" % (threadID, url , data))
				workQueue.task_done()
				
			else:
				queueLock.release()

			time.sleep(1)

		#print ("Exiting " + self.threadID)

class RunThread(QtCore.QThread):

	signal = QtCore.pyqtSignal(str)
	signal_thread_state = QtCore.pyqtSignal(int,float,object)
	signal_Buttom = QtCore.pyqtSignal(object)
	signal_shell = QtCore.pyqtSignal(int,int,str)
	signal_restart = QtCore.pyqtSignal()
	signal_end = QtCore.pyqtSignal()

	def __init__(self, parent,Progress_count):
		super(QtCore.QThread, self).__init__()

		self.__flag = threading.Event()
		self.__flag.set()
		self.__running = threading.Event()
		self.__running.set()

		self.Progress_count = Progress_count

		self.data_max_count = 0

		self.values = {}

	def __del__(self):
		self.wait()

	def set(self,key,value):
		self.values[key] = value
		#print("數值檢查:",self.values[key])

	def get(self):

		#print(self.values)

		# self.domain => requests domain 的資料
		# self.data => requests data的資料 => 回傳 dict
		# self.urls => requests 網址路徑 => 回傳 list

		def _post():
			_dict = {}
			self.data = {}
			self.data.clear()

			# POST 資料
			self.data = self.values["post"]

			post_count = len(self.values["post"].split("&"))

			if post_count > 1:

				for v in self.values["post"].split("&"):
					_count = len(v.split("="))
					#print(_count)
					# 列表數量需偶數才轉字典
					if ( _count % 2 == 0):
						key,value = v.split("=")
						_dict[key] = value

				return _dict
			else:
				return self.data

		def _request(tableWidget):

			# 得到總行數
			rows = tableWidget.rowCount()
			#print(rows)

			self.urls = []

			for rows_index in range(rows):
				key = tableWidget.item(rows_index,0).text()
				_bool = tableWidget.item(rows_index,1).text()
				val = tableWidget.item(rows_index,2).text()
				
				#print ("索引",key)
				#print ("使用參數",_bool)
				#print ("數值",val)

				self.urls.append([key,_bool,val])

			return self.urls
				
		self.data = _post()
		#print("字典預覽",self.data)
		self.urls = _request(self.values["request"])
		#print("網址預覽",self.urls)
		
	def run(self):

		global workQueue

		# 讀取數據
		self.domains = [i.replace("\n","") for i in open(self.values["domain"],"r",encoding="UTF-8").readlines()]

		self.threads = []

		#print("核心數量",self.Multi_Core_Number,"超時時間",self.Time_Out)

		files = ["",""]
		if self.values["檔案路徑變數"] != "":
			files = [self.values["檔案路徑變數"],self.values["files"]]

		workQueue = Queue.Queue(self.Multi_Core_Number)

		thread_config = self.values
		thread_workQueue = workQueue
		thread_headers = self.values["標頭"]
		thread_time_out = self.Time_Out
		thread_data = self.data
		thread_files = files

		length = len(self.domains)

		if length < self.Multi_Core_Number:
			self.Multi_Core_Number = length

		#print("線程數量",self.Multi_Core_Number)

		self.datathreads = []
		self.resultthreads = []

		# 創造 100 個新線程
		for threadID in range(0,self.Multi_Core_Number):
			threadID += 1
			thread = dataThread(str(threadID), thread_config ,thread_workQueue , thread_headers , thread_time_out , thread_data , self.signal , self.signal_thread_state , self.data_max_count , files = thread_files )
			thread.setDaemon(True)
			thread.start()
			self.datathreads.append(thread)

		# 創造 100 個新線程
		for threadID in range(0,self.Multi_Core_Number):
			threadID += 1
			thread = resultThread(thread_config)
			thread.setDaemon(True)
			thread.start()
			self.resultthreads.append(thread)

		url_paths = self.urls

		while self.__running.isSet():

			self.__flag.wait() # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回

			try:
				# 每次迴圈底部，檢查是否有數值，把結果傳送至文本
				while not shell_Queue.empty():
					item = shell_Queue.get()
					#print("準備寫入小馬",shell_Queue.get())
					self.signal_shell.emit(item["id"],item["HTTP_Status"],item["shell"])
					with open (self.values["導出文件名"]+".txt","a") as f:
						f.write(item["shell"] + "\n")
			except:
				pass

			# 進度條數字 100% 離開
			if self.Progress_count >= self.data_max_count:

				try:
					print("1.等待隊列清空")
					workQueue.join()
					
					# 等待队列清空
					while not workQueue.empty():
						pass # 一定需要1秒以上

					while 1:

						print("2.再次檢查剩餘資料")

						print("data 小馬",shell_Queue.qsize())
						print("data HTTP",result_Queue.qsize())

						if self.data_max_count <= 20:
							inspections_number = 10
						else:
							inspections_number = 1

						for i in range(inspections_number):
							# 再次迴圈，檢查是否有數值，把結果傳送至文本
							while not shell_Queue.empty():
								item = shell_Queue.get()
								self.signal_shell.emit(item["id"],item["HTTP_Status"],item["shell"])
								with open (self.values["導出文件名"]+".txt","a") as f:
									f.write(item["shell"] + "\n")
								time.sleep(1) # 一定需要1秒以上
							time.sleep(1) # 一定需要1秒以上
							#print("2-2.資料檢查中 - " + str(i) , shell_Queue.qsize() )
						
						print("3.發送線程停止信號")

						# 透過隊列數值等於空,傳送信號終止線程
						for t in self.datathreads:
							t.set("exitFlag")
						for t in self.resultthreads:
							t.set("exitFlag")

						if shell_Queue.qsize() == 0 and result_Queue.qsize() == 0:
							break

						time.sleep(1)
					
					print("4.等待所有線程完成")

					# 等待所有線程完成
					for t in self.datathreads:
						t.join()
					for t in self.resultthreads:
						t.join()
				except:
					pass

				break
				# 通知線程是時候退出

			if not workQueue.full():

				# urls 檔案進度
				ID = self.Progress_count
				domains = self.domains[ID:ID+20]
				#print(domains)

				# 填充 item 隊列
				#queueLock.acquire()
				if len(domains) > 0:
					workQueue.put([ID,domains,url_paths])
				#queueLock.release()

				#print(workQueue.qsize())
				
				self.Progress_count += 20

				#print(self.Progress_count)

			time.sleep(0.1) # while
	
		# 發送結束信號
		self.signal_end.emit() 

	# 更新後台線程的數值
	def update_val(self,pid,val):
		if pid == 1:
			self.data_max_count = val
		if pid == 2:
			self.Progress_count = val
		if pid == 3:
			self.Multi_Core_Number = val[0]
			self.Time_Out = val[1]

	###################
	#
	# 專門控制內部線程
	#
	###################
	def _start(self):
		self.__running.set() # 设置为True

		if self.data_max_count > 0:
			Buttoms_status = [False,True,True,False]
			self.signal_Buttom.emit(Buttoms_status)
		
	def stop(self):
		#print("數據清空")

		# 傳送信號終止線程
		for t in self.threads:
			t.set("exitFlag")

		self.__flag.set()	   # 将线程从暂停状态恢复, 如何已经暂停的话
		self.__running.clear()		# 设置为False
		self.Progress_count = 0

		Buttoms_status = [False,False,False,False]
		self.signal_Buttom.emit(Buttoms_status)
		self.signal_restart.emit()

	def pause(self):
		#print("暫停")
		self.__flag.clear()	 # 设置为False, 让线程阻塞

		Buttoms_status = [False,True,False,True]
		self.signal_Buttom.emit(Buttoms_status)

	def resume(self):
		#print("繼續")
		self.__flag.set()	# 设置为True, 让线程停止阻塞

		Buttoms_status = [False,True,True,False]
		self.signal_Buttom.emit(Buttoms_status)

# 繼承至介面檔案的主視窗類
class MyMainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(MyMainWindow, self).__init__(parent)
		self.setupUi(self)

		# Qt 執行緒
		self.tutorial_thread = object

		# 保存檔案原始數量
		self.data_max_count_original = 0
		# 檔案最大數量
		self.data_max_count = 0
		# 檔案索引值 -> self.data[self.index]
		self.step_index = 0

		# Shell 成功數量
		self.Success_Total = 0
		# CPU 核心數量
		self.Multi_Core_Number = 0
		# 連線超時
		self.Time_Out = 0

		# 系統日誌 PID 尋找自己的位置 寫入參數
		self.logs_PID = 0

		# 檢查是否有此資料夾,不存在則建立
		self.examination()

		# 載入圖標
		self.icon()
		self.setWindowIcon(self.icon_window)

		self.Rewrite_object()

		# 界面繪製
		self.register()

		# CMS插件載入 
		self.PlusLoad()

		# 設置列表 欄目標題
		self.table_HeaderLabels_config()

		# 設置插件 欄目標題
		self.Plus_Headerpath_config()

		# 設定初始參數
		self.step_index = 0 # 進度條 初始數值
		self.UI["Task_progressBar"].setProperty("value", 0) # 進度條初始化
		self.timer = QBasicTimer() # 計時器
		self.step = 0 # 進度條 計算完畢的數值
		self.row_count = 0 # 列表 Row 數值
		self.Time_Out = 3 # 超時的初始時間

		# 信號連結
		self.start_login()

		# 按鈕綁定事件
		self.connect()

		# 1.系統日誌 只有Start的時候寫入(True)
		# 2.使用定時器實時返回
		# 3.返回1次後關閉(False)
		self.logsSwitch = True
		# 載入系統日誌
		self.logsLove()

		# 暫放UI參數
		self.value = {}

		# 獲取窗體初始寬度
		self.window_width = int(self.width())

		# 狀態的變化參數
		self.state = "start"

		self.Task_lineEdit_filepath.inp_text_signal.connect(self.callback_DropLineEdit)   #绑定槽函数

		# 多進程池
		self.multiprocessing_Queue = multiprocessing.Queue()
		self.multiprocessing_Queue.put("111")

	# 繼承重寫UI元件
	def Rewrite_object(self):
		self.Task_lineEdit_filepath = DropLineEdit()
		self.Task_lineEdit_filepath = DropLineEdit(self.groupBox_3)
		self.Task_lineEdit_filepath.setEnabled(True)
		self.Task_lineEdit_filepath.setMinimumSize(QtCore.QSize(0, 30))
		font = QtGui.QFont()
		font.setFamily("Arial")
		self.Task_lineEdit_filepath.setFont(font)
		self.Task_lineEdit_filepath.setStyleSheet("")
		self.Task_lineEdit_filepath.setText("")
		self.Task_lineEdit_filepath.setDragEnabled(True)
		self.Task_lineEdit_filepath.setObjectName("Task_lineEdit_filepath")
		self.gridLayout_9.addWidget(self.Task_lineEdit_filepath, 0, 1)
		self.Task_lineEdit_filepath.setPlaceholderText("將文件拖曳到這裡")

	def ellipsis(self,_str):
		
		# 初始數值 1024
		# 文字長度 75 (省略號6個)
		# 初始數值 1920
		# 文字長度 190 (省略號6個)
		
		# 窗體寬度
		if (self.window_width == 1024) and len(_str) >= 75:
			return _str[0:75] + "......"
		elif (self.window_width > 1024) and len(_str) >= 190:
			return _str[0:190] + "......"
		else:
			return _str

	def examination(self):

		paths = ["logs","cache"]

		for path in paths:
			if not os.path.isdir(path):
				os.mkdir(path)

	def logsmodify(self):

		lines = [i.replace("\n","") for i in open("cache/logs.txt","r+",encoding="UTF-8").readlines()]

		Copywriting = ""

		End_Time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

		FileProgress = self.UI["Task_lineEdit_serial"].text() + "/" + self.UI["Task_lineEdit_file_number"].text()

		i = 0
		for line in lines:
			if self.logs_PID == i:
				LogsTxt = lines[self.logs_PID]
				ArrayLogsTxt = LogsTxt.split("|")

				ID = ""
				PlusName = ""
				StartTime = ""
				EndTime = ""
				FilePath = ""

				# 執行中，初始只有4個數據
				if len(ArrayLogsTxt) == 4:
					(ID,PlusName,StartTime,FilePath) = ArrayLogsTxt

				# 完整數據，執行完畢的數據
				if len(ArrayLogsTxt) == 6:
					(ID,PlusName,StartTime,EndTime,FileProgress,FilePath) = ArrayLogsTxt

				if ID != "":
					LogsTxt = '%s|%s|%s|%s|%s|%s\n' % (ID,PlusName,StartTime,End_Time,FileProgress,FilePath)
				Copywriting += LogsTxt
			else:
				Copywriting += line + "\n"
			i += 1 

		with open('cache/logs.txt', 'r+',encoding="UTF-8") as f:
		    f.writelines(Copywriting)

		self.logsLove(Tag="Update")

	def logsSave(self):

		if not os.path.isfile("cache/logs.txt"):
			open("cache/logs.txt","w",encoding="UTF-8")

		self.logs_PID = len([i.replace("\n","") for i in open("cache/logs.txt","r",encoding="UTF-8").readlines()])
		print("本次編號",self.logs_PID)
		PlusName = self.UI["Plus_lineEdit_name"].text()
		StartTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		FilePath = self.UI["Task_lineEdit_filepath"].text()
		
		txt = (str(self.logs_PID) , PlusName , StartTime , FilePath)
		LogsTxt = "|".join(txt) + "\n"

		with open ("cache/logs.txt","a",encoding="UTF-8") as f:
			f.write(LogsTxt)

	def logsLove(self,Tag = "Null"):

		if not os.path.isfile("cache/logs.txt"):
			open("cache/logs.txt","w",encoding="UTF-8")

		if self.logsSwitch == True or Tag == "Update":

			LogsTxts = [i.replace("\n","") for i in open("cache/logs.txt","r",encoding="UTF-8").readlines()]

			tableWidget = self.UI["logs_tableWidget_item"]
			tableWidget.setRowCount(len(LogsTxts))

			for LogsTxt in LogsTxts:
				ArrayLogsTxt = LogsTxt.split("|")
				
				ID = 0
				PlusName = ""
				StartTime = ""
				EndTime = ""
				FileProgress = ""
				FilePath = ""

				# 執行中，初始只有4個數據
				if len(ArrayLogsTxt) == 4:
					(ID,PlusName,StartTime,FilePath) = ArrayLogsTxt

				# 完整數據，執行完畢的數據
				if len(ArrayLogsTxt) == 6:
					(ID,PlusName,StartTime,EndTime,FileProgress,FilePath) = ArrayLogsTxt

				ID = int(ID)

				tableWidget.horizontalHeader().resizeSection(2,150)
				tableWidget.horizontalHeader().resizeSection(3,150)
				tableWidget.horizontalHeader().resizeSection(4,150)

				# 插入數值
				tableWidget.setItem(ID,0, QTableWidgetItem(str(ID)))
				tableWidget.setItem(ID,1, QTableWidgetItem(str(PlusName)))
				tableWidget.setItem(ID,2, QTableWidgetItem(str(StartTime)))
				tableWidget.setItem(ID,3, QTableWidgetItem(str(EndTime)))
				tableWidget.setItem(ID,4, QTableWidgetItem(str(FileProgress)))
				tableWidget.setItem(ID,5, QTableWidgetItem(str(FilePath)))
				
				# 設置字體居中
				tableWidget.item(ID,0).setTextAlignment(Qt.AlignCenter)
				tableWidget.item(ID,1).setTextAlignment(Qt.AlignCenter)
				tableWidget.item(ID,2).setTextAlignment(Qt.AlignCenter)
				tableWidget.item(ID,3).setTextAlignment(Qt.AlignCenter)
				tableWidget.item(ID,4).setTextAlignment(Qt.AlignCenter)
				tableWidget.item(ID,5).setTextAlignment(Qt.AlignCenter)

				if ID % 2 == 0:
					# 修改背景顏色
					brush = QtGui.QBrush(QtGui.QColor(194, 234, 254,45))
					brush.setStyle(Qt.SolidPattern)
					tableWidget.item(ID,0).setBackground(brush)
					tableWidget.item(ID,1).setBackground(brush)
					tableWidget.item(ID,2).setBackground(brush)
					tableWidget.item(ID,3).setBackground(brush)
					tableWidget.item(ID,4).setBackground(brush)
					tableWidget.item(ID,5).setBackground(brush)
				else:
					brush = QtGui.QBrush(QtGui.QColor(255, 241, 252))
					brush.setStyle(Qt.SolidPattern)
					tableWidget.item(ID,0).setBackground(brush)
					tableWidget.item(ID,1).setBackground(brush)
					tableWidget.item(ID,2).setBackground(brush)
					tableWidget.item(ID,3).setBackground(brush)
					tableWidget.item(ID,4).setBackground(brush)
					tableWidget.item(ID,5).setBackground(brush)

		# 關閉日誌通道
		self.logsSwitch = False
		
	#程式圖標載入區
	def icon(self):

		# 程式圖標
		self.icon_window = QIcon(':/icon/bg.ico')

	def data_Entrance(self,path):

		self.data = [i.replace("\n","") for i in open(path,"r",encoding="UTF-8").readlines()]
		self.data_max_count = len(self.data)
		self.data_max_count_original = self.data_max_count

		File_Path_View = self.UI["Task_lineEdit_filepath"] 
		urls_number = self.UI["Task_lineEdit_file_number"]
		Number_of_URL = self.UI["Plus_tableWidget_path_list"]
		Number_of_URL_lines = int(Number_of_URL.rowCount())

		if Number_of_URL_lines == 0:
			rowCount = 1
		else:
			rowCount = int(self.UI["Plus_tableWidget_path_list"].rowCount())

		self.data_max_count = int(rowCount) * int(self.data_max_count_original)

		# 更新 網址數量最大值
		self.tutorial_thread.update_val(1,self.data_max_count)
		self.tutorial_thread.set("domain",path)

		urls_number.setText(str(self.data_max_count))
		File_Path_View.setText(path)

	def connect(self):

		# 開始 繼續 暫停 停止
		self.Start_thread.clicked.connect(self.start)
		self.Stop_thread.clicked.connect(self.stop)
		self.Pause_thread.clicked.connect(self.pause)
		self.Continue_thread.clicked.connect(self.resume)

		# 任務 打開文件
		self.Task_archiveButton.clicked.connect(self.openFileNameDialog)

		# 插件 保存
		self.Plus_pushButton_save.clicked.connect(self.PlusSave)

		# 請求路徑 插入
		self.UI["Plus_pushButton_insert"].clicked.connect(self.Plus_path_insert)
		# 請求路徑 刪除
		self.UI["Plus_pushButton_delete"].clicked.connect(self.Plus_path_delete)

	def register(self):

		####################
		#
		# 不再本文件註冊將無法調用變更介面
		#
		####################

		########### Start ###########

		###任務欄###

		self.UI = {}

		# 開始
		self.UI["Start_thread"] = self.Start_thread

		# 停止
		self.UI["Stop_thread"] = self.Stop_thread
		self.UI["Stop_thread"].setEnabled(False)
		# 暫停
		self.UI["Pause_thread"] = self.Pause_thread
		self.UI["Pause_thread"].setEnabled(False)
		# 繼續
		self.UI["Continue_thread"] = self.Continue_thread
		self.UI["Continue_thread"].setEnabled(False)
		# 列表
		self.UI["Task_tableWidget"] = self.Task_tableWidget
		# 進度條
		self.UI["Task_progressBar"] = self.Task_progressBar

		# 檔案數量
		self.UI["Task_lineEdit_file_number"] = self.Task_lineEdit_file_number

		# 現在的檔案數量(可編輯)
		self.UI["Task_lineEdit_serial"] = self.Task_lineEdit_serial

		# 載入後的檔案路徑
		self.UI["Task_lineEdit_filepath"] = self.Task_lineEdit_filepath

		# 線程數量
		self.UI["Task_spinBox_thread"] = self.Task_spinBox_thread

		# 超時
		self.UI["Task_spinBox_time_out"] = self.Task_spinBox_time_out

		# 成功數量
		self.UI["Task_label_Success"] = self.Task_label_Success
		
		# 訊息
		self.UI["Task_label_msg"] = self.Task_label_msg

		# 時間
		self.UI["Task_label_time"] = self.Task_label_time

		###任務欄###

		###插件欄###

		# 插件項目
		self.UI["Plus_tableWidget_item"] = self.Plus_tableWidget_item

		# 插件名稱
		self.UI["Plus_lineEdit_name"] = self.Plus_lineEdit_name

		# 請求次數
		self.UI["Plus_spinBox_number"] = self.Plus_spinBox_number
		# 漏洞類型
		self.UI["Plus_comboBox_Type"] = self.Plus_comboBox_Type
		# 請求類型
		self.UI["Plus_comboBox_request_Type"] = self.Plus_comboBox_request_Type
		# 攜帶參數
		self.UI["Plus_checkBox_carry"] = self.Plus_checkBox_carry

		# 請求路徑 插入欄
		self.UI["Plus_lineEdit_insert"] = self.Plus_lineEdit_insert
		# 請求路徑 第幾行插入
		self.UI["Plus_spinBox_insert_number"] = self.Plus_spinBox_insert_number
		# 請求路徑 插入
		self.UI["Plus_pushButton_insert"] = self.Plus_pushButton_insert
		# 請求路徑 刪除
		self.UI["Plus_pushButton_delete"] = self.Plus_pushButton_delete

		# 請求路徑列表
		self.UI["Plus_tableWidget_path_list"] = self.Plus_tableWidget_path_list

		# 小馬網址文本
		self.UI["Plus_label_url"] = self.Plus_label_url
		# 小馬網址變數
		self.UI["Plus_lineEdit_url_Variable"] = self.Plus_lineEdit_url_Variable
		# 小馬網址
		self.UI["Plus_lineEdit_url"] = self.Plus_lineEdit_url

		# 檔案路徑文本
		self.UI["Plus_label_path"] = self.Plus_label_path
		# 檔案路徑變數
		self.UI["Plus_lineEdit_path_Variable"] = self.Plus_lineEdit_path_Variable
		# 檔案路徑
		self.UI["Plus_lineEdit_path"] = self.Plus_lineEdit_path
		# 檔案讀取類型
		self.UI["Plus_comboBox_path_type"] = self.Plus_comboBox_path_type

		# POST參數
		self.UI["Plus_textEdit_POST"] = self.Plus_textEdit_POST

		# Headers
		self.UI["Plus_textEdit_Headers"] = self.Plus_textEdit_Headers

		# 特徵文本
		self.UI["Plus_lineEdit_feature_Text"] = self.Plus_lineEdit_feature_Text
		# 排除文本
		self.UI["Plus_lineEdit_exclude_Text"] = self.Plus_lineEdit_exclude_Text

		# 導出文件名
		self.UI["Plus_lineEdit_FileName"] = self.Plus_lineEdit_FileName

		# 導出格式-域名
		self.UI["Plus_checkBox_domain"]  = self.Plus_checkBox_domain
		# 導出格式-結果
		self.UI["Plus_checkBox_result"] = self.Plus_checkBox_result
		# 導出結果-自定義
		self.UI["Plus_lineEdit_custom"] = self.Plus_lineEdit_custom

		# 備註說明
		self.UI["Plus_textEdit_vote"] = self.Plus_textEdit_vote

		###插件欄###

		# 資源監視器
		self.UI["management_tableWidget_item"] = self.management_tableWidget_item

		# 系統日誌
		self.UI["logs_tableWidget_item"] = self.logs_tableWidget_item

		########### End ###########

	def start_login(self):

		# 執行緒(參數值)
		self.tutorial_thread = RunThread(self,self.step)

		# 線程發過來的信號掛接到槽：callback
		self.tutorial_thread.signal.connect(self.callback)
		# 線程發過來的信號掛接到槽：callback_thread_state
		self.tutorial_thread.signal_thread_state.connect(self.callback_thread_state)
		# 線程發過來的信號掛接到槽：callback_Buttom
		self.tutorial_thread.signal_Buttom.connect(self.callback_Buttom)
		# 線程發過來的信號掛接到槽：callback_table_row_insert
		self.tutorial_thread.signal_shell.connect(self.callback_table_row_insert)

		# 線程發過來的信號掛接到槽：callback_restart
		self.tutorial_thread.signal_restart.connect(self.callback_restart)

		# 線程發過來的信號掛接到槽：callback_end
		self.tutorial_thread.signal_end.connect(self.callback_end)

	def table_HeaderLabels_config(self):

		# 垂直數量 4
		# 如果要顯示固定的數量，可直接輸入
		# self.tableWidget.setRowCount(4)

		# 水平數量 2
		# 基本上都是固定的，所以你要什麼功能就寫多少吧
		self.UI["Task_tableWidget"].setColumnCount(3)

		# 設定水平表頭 標題
		#self.UI["Task_tableWidget"].setHorizontalHeaderLabels(('ID','HTTP Status','網址'))

		# 自適應布局
		self.UI["Task_tableWidget"].horizontalHeader().resizeSection(0,40) #設置第一列的宽度为40
		self.UI["Task_tableWidget"].horizontalHeader().resizeSection(1,100) #設置第二列的宽度为100
		self.UI["Task_tableWidget"].horizontalHeader().setStretchLastSection(True) ##设置最后一列拉伸至最大

		# 隱藏垂直表頭
		self.UI["Task_tableWidget"].verticalHeader().setVisible(False)

		self.UI["Plus_tableWidget_item"].itemClicked.connect(self.Plus_tableItem_OnClicked) #列表點擊信號

		# 隱藏垂直表頭
		self.UI["Plus_tableWidget_item"].verticalHeader().setVisible(False)

	# 程序已結束
	def EndEvent(self):

		msgBox = QMessageBox()
		msgBox.setStyleSheet("background-color: rgb(232, 233, 255);")
		msgBox.setWindowIcon(QIcon(':/icon/bg.ico'))
		msgBox.setWindowTitle('結束訊息')
		msgBox.setText("對於阻擋在吾等面前！所有愚蠢的事物！")
		msgBox.setIconPixmap(QPixmap(":/icon/end.png"))
		msgBox.setStandardButtons(QMessageBox.Ok)

		reply = msgBox.exec()

	# 視窗關閉訊息
	def closeEvent(self, event):

		# 縮寫
		# msgBox = QMessageBox(QMessageBox.NoIcon, '提示訊息',"醒來吧！邪王真眼！覺醒的時刻到來啦！")

		msgBox = QMessageBox()
		msgBox.setStyleSheet("background-color: rgb(232, 233, 255);")
		msgBox.setWindowIcon(QIcon(':/icon/bg.ico'))
		msgBox.setWindowTitle('關閉確認訊息')
		msgBox.setText("醒來吧！邪王真眼！覺醒的時刻到來啦！")
		msgBox.setIconPixmap(QPixmap(":/icon/exit.png"))
		msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

		reply = msgBox.exec()

		if reply == QMessageBox.Yes:
			self.logsmodify()
			event.accept()
		else:
			event.ignore()

	def callback(self,url):	 

		self.step_index = self.step_index + 1
		
		self.step = int( self.step_index / self.data_max_count * 100)

		if self.state == "start":
			# 檔案Key編號
			try:
				self.gmsg = str(self.step_index)+ " " + "-" + " "+ str(url)
			except:
				pass
		else:
			self.UI["Task_label_msg"].setText("子線程停止中")

	def callback_DropLineEdit(self,path):

		self.data = [i.replace("\n","") for i in open(path,"r",encoding="UTF-8").readlines()]
		self.data_max_count = len(self.data)
		self.data_max_count_original = self.data_max_count

		urls_number = self.UI["Task_lineEdit_file_number"]
		Number_of_URL = self.UI["Plus_tableWidget_path_list"]
		Number_of_URL_lines = int(Number_of_URL.rowCount())

		if Number_of_URL_lines == 0:
			rowCount = 1
		else:
			rowCount = int(self.UI["Plus_tableWidget_path_list"].rowCount())

		self.data_max_count = int(rowCount) * int(self.data_max_count_original)

		urls_number.setText(str(self.data_max_count))

		# 更新 網址數量最大值
		self.tutorial_thread.update_val(1,self.data_max_count)

	def callback_thread_state(self,pid,time_consuming,status):

		try:
			offset = 1
			pid = pid - offset
			view_pid = pid + offset

			if status == True:
				state = "執行中"
			if status == False:
				state = "暫停"
			
			# 插入數值
			self.UI["management_tableWidget_item"].setItem(pid,0, QTableWidgetItem(str(view_pid)))
			self.UI["management_tableWidget_item"].setItem(pid,1, QTableWidgetItem(str(time_consuming)))
			self.UI["management_tableWidget_item"].setItem(pid,2, QTableWidgetItem(str(state)))
			
			# 設置字體居中
			self.UI["management_tableWidget_item"].item(pid,0).setTextAlignment(Qt.AlignCenter)
			self.UI["management_tableWidget_item"].item(pid,1).setTextAlignment(Qt.AlignCenter)
			self.UI["management_tableWidget_item"].item(pid,2).setTextAlignment(Qt.AlignCenter)

			if pid % 2 == 0:
				# 修改背景顏色
				brush = QtGui.QBrush(QtGui.QColor(194, 234, 254,45))
				brush.setStyle(Qt.SolidPattern)
				self.UI["management_tableWidget_item"].item(pid,0).setBackground(brush)
				self.UI["management_tableWidget_item"].item(pid,1).setBackground(brush)
				self.UI["management_tableWidget_item"].item(pid,2).setBackground(brush)
			else:
				brush = QtGui.QBrush(QtGui.QColor(255, 241, 252))
				brush.setStyle(Qt.SolidPattern)
				self.UI["management_tableWidget_item"].item(pid,0).setBackground(brush)
				self.UI["management_tableWidget_item"].item(pid,1).setBackground(brush)
				self.UI["management_tableWidget_item"].item(pid,2).setBackground(brush)
		except:
			pass

	def callback_Buttom(self,msgs):

		self.UI["Start_thread"].setEnabled(msgs[0])
		self.UI["Stop_thread"].setEnabled(msgs[1])
		self.UI["Pause_thread"].setEnabled(msgs[2])
		self.UI["Continue_thread"].setEnabled(msgs[3])

	def callback_table_row_insert(self,key,status,msg):
		try:
			row_count = self.UI["Task_tableWidget"].rowCount()

			# 動態插入行數
			self.UI["Task_tableWidget"].insertRow(self.row_count)
			self.row_count += 1

			# 插入數值
			self.UI["Task_tableWidget"].setItem(row_count,0, QTableWidgetItem(str(key)))
			self.UI["Task_tableWidget"].setItem(row_count,1, QTableWidgetItem(str(status)))
			self.UI["Task_tableWidget"].setItem(row_count,2, QTableWidgetItem(str(msg)))

			# 設置字體居中
			self.UI["Task_tableWidget"].item(row_count,0).setTextAlignment(Qt.AlignCenter)
			self.UI["Task_tableWidget"].item(row_count,1).setTextAlignment(Qt.AlignCenter)

			# 成功數量總計
			self.Success_Total = int(self.row_count)
			self.UI["Task_label_Success"].setText(str(self.Success_Total))

			if self.row_count % 2 == 0:
				# 修改背景顏色
				brush = QtGui.QBrush(QtGui.QColor(255, 230, 238))
				brush.setStyle(Qt.SolidPattern)
				self.UI["Task_tableWidget"].item(key,0).setBackground(brush)
				self.UI["Task_tableWidget"].item(key,1).setBackground(brush)
				self.UI["Task_tableWidget"].item(key,2).setBackground(brush)
			else:
				brush = QtGui.QBrush(QtGui.QColor(255, 242, 252))
				brush.setStyle(Qt.SolidPattern)
				self.UI["Task_tableWidget"].item(key,0).setBackground(brush)
				self.UI["Task_tableWidget"].item(key,1).setBackground(brush)
				self.UI["Task_tableWidget"].item(key,2).setBackground(brush)
		except:
			pass

	def callback_restart(self):
		
		self.UI["Task_label_msg"].setText(str("線程停止中，請稍等")) # 現在掃描數量初始化
		self.UI["Task_lineEdit_serial"].setText(str(0)) # 現在掃描數量初始化
		self.UI["Task_progressBar"].setProperty("value", 0) # 進度條初始化

	def callback_end(self):

		self.UI["Task_label_msg"].setText(str("線程已停止")) # 現在掃描數量初始化

		# 開始
		self.UI["Start_thread"].setEnabled(True)
		# 停止
		self.UI["Stop_thread"].setEnabled(False)
		# 暫停
		self.UI["Pause_thread"].setEnabled(False)
		# 繼續
		self.UI["Continue_thread"].setEnabled(False)

		time = QTime.currentTime()
		time_Formatting = time.toString(Qt.DefaultLocaleLongDate)

		try:
			self.UI["Task_label_time"].setText(str(time_Formatting))
			self.UI["Task_lineEdit_serial"].setText(str(self.step_index))
			self.gmsg = "線程已停止"
			self.UI["Task_label_msg"].setText(self.gmsg)
			self.UI["Task_progressBar"].setValue(self.step)
		except:
			pass

		# 修改系統日誌
		self.logsmodify()

		self.EndEvent()

	def timerEvent(self, e):

		time = QTime.currentTime()
		time_Formatting = time.toString(Qt.DefaultLocaleLongDate)

		if self.logsSwitch == True:
			self.logsLove()

		if self.step >= 100:
			self.timer.stop()
			self.UI["Task_label_msg"].setText("數據已跑完，請等待結束")
			return

		# 5秒更新1次 全介面 節省CPU使用率

		try:
			self.UI["Task_label_time"].setText(str(time_Formatting))
			self.UI["Task_lineEdit_serial"].setText(str(self.step_index))
			self.gmsg = self.ellipsis(self.gmsg)
			self.UI["Task_label_msg"].setText(self.gmsg)
			self.UI["Task_progressBar"].setValue(self.step)
		except:
			pass

	###################
	#
	# 專門控制3種線程(自定義Qt類別方法、計時器、Qt信號槽)
	# self.tutorial_thread._start() QT線程內的方法 (開始)
	# self.timer.start(100, self) 自身 計時器 啟動 方法，最高100
	# self.tutorial_thread.start() Qt 信號槽 開始
	#
	###################

	def start(self):

		#CPU 核心數量
		self.Multi_Core_Number = int(self.UI["Task_spinBox_thread"].value())

		# 資源監視器 插入指定行數
		self.UI["management_tableWidget_item"].setRowCount(self.Multi_Core_Number)

		#連線超時
		self.Time_Out = int(self.UI["Task_spinBox_time_out"].value())

		array = [self.Multi_Core_Number,self.Time_Out]
		# 更新 介面 CPU核心數量 , 超時
		self.tutorial_thread.update_val(3,array)

		# 現在檔案的進度
		serial = int(self.UI["Task_lineEdit_serial"].text())

		# 更新進度條初始數值
		self.step_index = serial

		# 更新狀態變化參數
		self.state = "start"

		# 更新預設視窗寬度
		self.window_width = self.width()

		if self.UI["Task_lineEdit_filepath"].text() != "":
			self.data_Entrance(self.UI["Task_lineEdit_filepath"].text())

		if self.data_max_count > 0 and self.UI["Plus_lineEdit_name"].text() != "":

			# 開啟系統日誌通道
			self.logsSwitch = True

			# 寫入系統日誌
			self.logsSave()

			# 更新進度條數值
			self.step = int( self.step_index / self.data_max_count * 100)
			self.UI["Task_lineEdit_serial"].setText(str(self.step_index))
			self.UI["Task_progressBar"].setValue(self.step)

			# 線程開始
			self.tutorial_thread._start()

			# 更新 後台線程 現在網址的最小數值
			self.tutorial_thread.update_val(2,serial)
		
			# 計時器開始
			self.timer.start(5000, self)

			# Qt線程開始
			self.tutorial_thread.start()

			###################
			#
			# 單按鈕開始與停止
			#
			###################

			#if self.timer.isActive():
				#self.timer.stop()
				#print('开始')
			#else:
				#self.timer.start(100, self)
				#print('停止')

	###################
	#
	# self.tutorial_thread.terminate() # Qt 信號槽 停止 (不推薦使用)
	# --------------------------------------------------------------
	# 專門控制2種線程(計時器，Qt線程)
	#
	# self.timer.stop() 自身 計時器 停止 方法，最高100
	# self.tutorial_thread.stop() QT線程內的方法 (停止)
	#
	###################

	def stop(self):
		# 停止按鈕 - 禁止選取
		#self.tutorial_thread.terminate()

		msgBox = QMessageBox()
		msgBox.setStyleSheet("background-color: rgb(232, 233, 255);")
		msgBox.setWindowIcon(QIcon(':/icon/bg.ico'))
		msgBox.setWindowTitle('停止確認')
		msgBox.setText("在無盡的歲月中迴盪著 停止那短暫的悲傷")
		msgBox.setIconPixmap(QPixmap(":/icon/stop.png"))
		msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

		reply = msgBox.exec()

		if reply == QMessageBox.Yes:
			print("應用程式停止中")
			self.state = "stop"
			pass
		else:
			print("繼續執行")
			self.state = "start"
			return

		# 計時器停止
		self.timer.stop()
		self.tutorial_thread.stop()


	def pause(self):
		# 暫停按鈕 - 禁止選取

		# 計時器停止
		self.timer.stop()

		# Qt線程->暫停方法
		self.tutorial_thread.pause()

	def resume(self):
		# 繼續按鈕 - 禁止選取
		# 計時器開始
		self.timer.start(100, self)
		self.tutorial_thread.resume()

	def Plus_tableItem_OnClicked(self, item):
		
		tmp = item #type: QTableWidgetItem
		cmsText = tmp.text()
		#print(cmsText)
		config = plus.read(cmsText)

		#print(config["basic"])
		#config["basic"]
		#config["request"]
		#config["headers"]
	   
		###插件欄###

		# 插件名稱
		self.UI["Plus_lineEdit_name"].setText(config["basic"]["插件名稱"])
		self.tutorial_thread.set("插件名稱",config["basic"]["插件名稱"])

		# 請求次數
		self.UI["Plus_spinBox_number"].setValue(int(config["basic"]["請求次數"]))
		self.tutorial_thread.set("請求次數",int(config["basic"]["請求次數"]))
		# 漏洞類型
		self.UI["Plus_comboBox_Type"].setCurrentText(config["basic"]["漏洞類型"])
		self.tutorial_thread.set("漏洞類型",config["basic"]["漏洞類型"])
		# 請求類型
		self.UI["Plus_comboBox_request_Type"].setCurrentText(config["basic"]["請求類型"])
		self.tutorial_thread.set("插件名稱",config["basic"]["插件名稱"])

		# 請求路徑列表(數值，UI列表)
		
		self.plus_view_List_Widget_OnClicked_insert(config["request"],self.UI["Plus_tableWidget_path_list"])
		self.tutorial_thread.set("request",self.UI["Plus_tableWidget_path_list"])
		# 清空列表數值，防止數值疊加，要拿數值，請至UI介面拿取
		config["request"].clear()
		
		# 小馬網址文本
		#self.UI["Plus_label_url"] = self.Plus_label_url
		# 小馬網址變數
		self.UI["Plus_lineEdit_url_Variable"].setText(config["basic"]["小馬網址變數"])
		self.tutorial_thread.set("小馬網址變數",config["basic"]["小馬網址變數"])
		# 小馬網址
		self.UI["Plus_lineEdit_url"].setText(config["basic"]["小馬網址"])
		self.tutorial_thread.set("小馬網址",config["basic"]["小馬網址"])
		
		# 檔案路徑文本
		#self.UI["Plus_label_path"] = self.Plus_label_path
		# 檔案路徑變數
		self.UI["Plus_lineEdit_path_Variable"].setText(config["basic"]["檔案路徑變數"])
		self.tutorial_thread.set("檔案路徑變數",config["basic"]["檔案路徑變數"])
		# 檔案路徑
		self.UI["Plus_lineEdit_path"].setText(config["basic"]["檔案路徑"])
		self.tutorial_thread.set("檔案路徑",config["basic"]["檔案路徑"])
		# 檔案讀取類型
		self.UI["Plus_comboBox_path_type"].setCurrentText(config["basic"]["檔案讀取類型"])
		self.tutorial_thread.set("檔案讀取類型",config["basic"]["檔案讀取類型"])
		
		#v = dir(self.UI["Plus_textEdit_POST"])
		#print(v)
		# POST參數
		#print(open(config["basic"]["檔案路徑"],"rb").read())

		# 載入圖片木馬
		def _Files():
			fileName = config["basic"]["檔案路徑"].replace("image/", "");
			files = {config["basic"]["檔案路徑變數"]: ( fileName , open(config["basic"]["檔案路徑"],config["basic"]["檔案讀取類型"]), "multipart/form-data") }
			return files

		if config["basic"]["小馬網址變數"] != "":
			GroupPost = config["basic"]["小馬網址變數"] + "=" + config["basic"]["小馬網址"] + "&" + config["basic"]["post"]
			self.tutorial_thread.set("post",GroupPost)
		elif config["basic"]["檔案路徑變數"] != "":
			self.value["files"] = _Files()
			GroupPost = config["basic"]["post"]
			self.tutorial_thread.set("files",self.value["files"])
			self.tutorial_thread.set("post",GroupPost)
		else:
			GroupPost = config["basic"]["post"]
			self.tutorial_thread.set("post",GroupPost)
		
		self.UI["Plus_textEdit_POST"].setText(str(GroupPost))
		# Headers
		self.UI["Plus_textEdit_Headers"].setText(config["headers"]["標頭"])
		self.tutorial_thread.set("標頭",config["headers"]["標頭"])
		
		# 特徵文本
		self.UI["Plus_lineEdit_feature_Text"].setText(config["basic"]["特徵文本"])
		self.tutorial_thread.set("特徵文本",config["basic"]["特徵文本"])
		# 排除文本
		self.UI["Plus_lineEdit_exclude_Text"].setText(config["basic"]["排除文本"])
		self.tutorial_thread.set("排除文本",config["basic"]["排除文本"])

		# 導出文件名
		self.UI["Plus_lineEdit_FileName"].setText(config["basic"]["導出文件名"])
		self.tutorial_thread.set("導出文件名",config["basic"]["導出文件名"])

		check_domain = 0
		check_restult = 0
		if config["basic"]["導出格式-域名"] == "True":
			check_domain = 1
			
		if config["basic"]["導出格式-結果"] == "True":
			check_restult = 1
			
		# 導出格式-域名
		self.UI["Plus_checkBox_domain"] .setChecked(int(check_domain))
		self.tutorial_thread.set("導出格式-域名",config["basic"]["導出格式-域名"])
		# 導出格式-結果
		self.UI["Plus_checkBox_result"].setChecked(int(check_restult))
		self.tutorial_thread.set("導出格式-結果",config["basic"]["導出格式-結果"])
		# 導出結果-自定義
		self.UI["Plus_lineEdit_custom"].setText(config["basic"]["導出結果-自定義"])
		self.tutorial_thread.set("導出結果-自定義",config["basic"]["導出結果-自定義"])

		# 備註說明
		self.UI["Plus_textEdit_vote"].setText(config["basic"]["備註說明"])
		self.tutorial_thread.set("備註說明",config["basic"]["備註說明"])
		self.tutorial_thread.get()

		if int(self.UI["Plus_tableWidget_path_list"].rowCount()) == 0:
			rowCount = 1
		else:
			rowCount = int(self.UI["Plus_tableWidget_path_list"].rowCount())

		self.data_max_count = int(rowCount) * int(self.data_max_count_original)

		self.UI["Task_lineEdit_file_number"].setText(str(self.data_max_count))

	def plus_view_List_Widget_OnClicked_insert(self,sections,tableWidget):

		# 舊數值，逆向循環刪除
		row_count = tableWidget.rowCount()
		for rP in range(0, row_count)[::-1]:
			tableWidget.removeRow(1)

		# 插入新數值
		for index ,section in enumerate(sections):
			check , url = sections[section].split("|",1)
			
			# 獲取row數量
			row_count = index

			# 垂直數量 N
			# 基本上都是固定的，所以你要什麼功能就寫多少吧
			tableWidget.setRowCount(len(sections))
			
			# 插入數值
			tableWidget.setItem(row_count,0, QTableWidgetItem(str(index)))
			tableWidget.setItem(row_count,1, QTableWidgetItem(str(check)))
			tableWidget.setItem(row_count,2, QTableWidgetItem(str(url)))

			# 設置字體居中
			tableWidget.item(row_count,0).setTextAlignment(Qt.AlignCenter)
			tableWidget.item(row_count,1).setTextAlignment(Qt.AlignCenter)
			tableWidget.item(row_count,2).setTextAlignment(Qt.AlignCenter)

			if row_count % 2 == 0:
				# 修改背景顏色
				brush = QtGui.QBrush(QtGui.QColor(194, 234, 254,45))
				brush.setStyle(Qt.SolidPattern)
				tableWidget.item(row_count,0).setBackground(brush)
				tableWidget.item(row_count,1).setBackground(brush)
				tableWidget.item(row_count,2).setBackground(brush)
			else:
				brush = QtGui.QBrush(QtGui.QColor(255, 241, 252))
				brush.setStyle(Qt.SolidPattern)
				tableWidget.item(row_count,0).setBackground(brush)
				tableWidget.item(row_count,1).setBackground(brush)
				tableWidget.item(row_count,2).setBackground(brush)

	def Plus_Headerpath_config(self):

		# 垂直數量 4
		# 如果要顯示固定的數量，可直接輸入
		# self.tableWidget.setRowCount(4)

		# 水平數量 3
		# 基本上都是固定的，所以你要什麼功能就寫多少吧
		self.UI["Plus_tableWidget_path_list"].setColumnCount(3)

		# 設定水平表頭 標題
		#self.UI["Plus_tableWidget_path_list"].setHorizontalHeaderLabels(('ID','參數','網址'))

		# 自適應布局
		self.UI["Plus_tableWidget_path_list"].horizontalHeader().resizeSection(0,40) #設置第一列的宽度为80
		self.UI["Plus_tableWidget_path_list"].horizontalHeader().resizeSection(1,60) #設置第二列的宽度为80
		self.UI["Plus_tableWidget_path_list"].horizontalHeader().setStretchLastSection(True) ##设置最后一列拉伸至最大

		# 隱藏垂直表頭
		self.UI["Plus_tableWidget_path_list"].verticalHeader().setVisible(False)

	def Plus_path_insert(self):
		# 第幾行
		index = self.UI["Plus_spinBox_insert_number"].text()

		Offset = 1
		key = int(index)-Offset

		# 插入的內容
		val = self.UI["Plus_lineEdit_insert"].text()

		# 獲取row數量
		row_count = self.UI["Plus_tableWidget_path_list"].rowCount()

		# 預覽數值
		#print("row",row_count,"/",key,"內容",val)

		# 動態插入行數 現在行數 小於 插入行數才繼續執行
		if key <= row_count and not(val in [None,""]):
			if row_count < 3:
				self.UI["Plus_tableWidget_path_list"].insertRow(row_count)

			# 插入數值
			self.UI["Plus_tableWidget_path_list"].setItem(key,0, QTableWidgetItem(str(index)))
			self.UI["Plus_tableWidget_path_list"].setItem(key,1, QTableWidgetItem(str(self.UI["Plus_checkBox_carry"].isChecked())))
			self.UI["Plus_tableWidget_path_list"].setItem(key,2, QTableWidgetItem(str(val)))

			# 設置字體居中
			self.UI["Plus_tableWidget_path_list"].item(key,0).setTextAlignment(Qt.AlignCenter)
			self.UI["Plus_tableWidget_path_list"].item(key,1).setTextAlignment(Qt.AlignCenter)
			self.UI["Plus_tableWidget_path_list"].item(key,2).setTextAlignment(Qt.AlignCenter)

			if row_count % 2 == 0:
				# 修改背景顏色
				brush = QtGui.QBrush(QtGui.QColor(194, 234, 254,45))
				brush.setStyle(Qt.SolidPattern)
				self.UI["Plus_tableWidget_path_list"].item(key,0).setBackground(brush)
				self.UI["Plus_tableWidget_path_list"].item(key,1).setBackground(brush)
				self.UI["Plus_tableWidget_path_list"].item(key,2).setBackground(brush)
			else:
				brush = QtGui.QBrush(QtGui.QColor(255, 241, 252))
				brush.setStyle(Qt.SolidPattern)
				self.UI["Plus_tableWidget_path_list"].item(key,0).setBackground(brush)
				self.UI["Plus_tableWidget_path_list"].item(key,1).setBackground(brush)
				self.UI["Plus_tableWidget_path_list"].item(key,2).setBackground(brush)

	def Plus_path_delete(self):
		##############
		# 刪除 Start #
		##############

		def _del():
			# input 第幾行
			index = self.UI["Plus_spinBox_insert_number"].text()
			
			Offset = 1
			row = int(index) - Offset

			# 刪除指定列
			self.UI["Plus_tableWidget_path_list"].removeRow(row)

		##############
		# 刪除 End   #
		##############

		##############
		# 迴圈 Start #
		##############
		def _sort():
			# 獲取剩餘row數量
			row_count = self.UI["Plus_tableWidget_path_list"].rowCount()
			# ID 重排序
			if row_count > 0:
				for row in range(int(row_count)):

					# 插入數值
					self.UI["Plus_tableWidget_path_list"].setItem(row,0, QTableWidgetItem(str(row+1)))
					# 設置字體居中
					self.UI["Plus_tableWidget_path_list"].item(row,0).setTextAlignment(Qt.AlignCenter)

		def _values():

			# 得到總行數
			rows = self.UI["Plus_tableWidget_path_list"].rowCount()

			for rows_index in range(rows):
				print ("索引",self.UI["Plus_tableWidget_path_list"].item(rows_index,0).text())
				print ("數值",self.UI["Plus_tableWidget_path_list"].item(rows_index,1).text())
		
		##############
		# 迴圈 End   #
		##############

		_del()
		_sort()
		#_values()

	# CMS插件載入
	def PlusLoad(self):

		lists = plus.FileList()

		# 獲取row數量
		
		for val in lists:
			row_count = self.UI["Plus_tableWidget_item"].rowCount()
			self.UI["Plus_tableWidget_item"].insertRow(row_count)

			# 插入數值
			self.UI["Plus_tableWidget_item"].setItem(row_count,0, QTableWidgetItem(str(val)))

			# 設置字體居中
			self.UI["Plus_tableWidget_item"].item(row_count,0).setTextAlignment(Qt.AlignCenter)

			if row_count % 2 == 0:
				# 修改背景顏色
				brush = QtGui.QBrush(QtGui.QColor(194, 234, 254,45))
				brush.setStyle(Qt.SolidPattern)
				self.UI["Plus_tableWidget_item"].item(row_count,0).setBackground(brush)
			else:
				brush = QtGui.QBrush(QtGui.QColor(255, 241, 252))
				brush.setStyle(Qt.SolidPattern)
				self.UI["Plus_tableWidget_item"].item(row_count,0).setBackground(brush)

	# CMS插件保存
	def PlusSave(self):

		def _request(sections):

			sections["request"] = {}

			# 得到總行數
			rows = self.UI["Plus_tableWidget_path_list"].rowCount()

			for rows_index in range(rows):
				key = self.UI["Plus_tableWidget_path_list"].item(rows_index,0).text()
				_bool = self.UI["Plus_tableWidget_path_list"].item(rows_index,1).text()
				val = self.UI["Plus_tableWidget_path_list"].item(rows_index,2).text()
				
				#print ("索引",key)
				#print ("使用參數",_bool)
				#print ("數值",val)

				sections["request"]["請求路徑_"+str(rows_index)] = _bool + "|" + val

			return sections
		
		#########
		#　說明　#
		#########
		
		# spinBox 下拉式數字
		# spinBox.text() 讀取 下拉式 選取中 數字

		# lineEdit 單行文本
		# lineEdit.text() # 讀取 文本

		# textEdit 多行文本
		# textEdit.toPlainText() # 讀取 文本
		# textEdit.setPlainText() # 設置 文本

		# comboBox 下拉式選單
		# comboBox.currentText() 獲取 字串

		# checkBox 勾選
		# checkBox.isChecked() 獲取 True、False

		###插件欄###
		sections = {}
		sections["basic"] = {}
		# 插件項目
		#tmp["test"]["1"] = self.UI["Plus_tableWidget_item"].text()

		# 插件名稱
		sections["basic"]["插件名稱"] = self.UI["Plus_lineEdit_name"].text()

		# 請求次數
		sections["basic"]["請求次數"] = self.UI["Plus_spinBox_number"].text()
		sections["basic"]["漏洞類型"] = self.UI["Plus_comboBox_Type"].currentText()
		sections["basic"]["請求類型"] = self.UI["Plus_comboBox_request_Type"].currentText()

		sections["request"] = {}

		sections["basic"]["小馬網址變數"] = self.UI["Plus_lineEdit_url_Variable"].text()
		sections["basic"]["小馬網址"] = self.UI["Plus_lineEdit_url"].text()
		
		sections["basic"]["檔案路徑變數"] = self.UI["Plus_lineEdit_path_Variable"].text()
		sections["basic"]["檔案路徑"] = self.UI["Plus_lineEdit_path"].text()
		
		sections["basic"]["檔案讀取類型"] = self.UI["Plus_comboBox_path_type"].currentText()

		sections["basic"]["POST"] = self.UI["Plus_textEdit_POST"].toPlainText()

		sections["headers"] = {}

		# Headers
		sections["headers"]["標頭"] = self.UI["Plus_textEdit_Headers"].toPlainText()

		sections["basic"]["特徵文本"] = self.UI["Plus_lineEdit_feature_Text"].text()
		sections["basic"]["排除文本"] = self.UI["Plus_lineEdit_exclude_Text"].text()
		sections["basic"]["導出文件名"] = self.UI["Plus_lineEdit_FileName"].text()
		sections["basic"]["導出格式-域名"] = self.UI["Plus_checkBox_domain"] .isChecked()
		sections["basic"]["導出格式-結果"] = self.UI["Plus_checkBox_result"].isChecked()
		sections["basic"]["導出結果-自定義"] = self.UI["Plus_lineEdit_custom"].text()

		# 備註說明
		sections["basic"]["備註說明"] = self.UI["Plus_textEdit_vote"].toPlainText()

		sections = _request(sections)
		plus.write(sections,sections["basic"]["插件名稱"])

	###################
	#
	# 檔案處理
	# --------------------------------------------------------------
	#
	###################

	# 信號事件-資料夾選擇
	def openDirNameDialog(self):
		fileName = QFileDialog.getExistingDirectory(self,"QFileDialog.getExistingDirectory()",os.getcwd())
		if fileName:
			print(fileName)
		else:
			print("取消選擇")

	# 信號事件-單文件選擇
	def openFileNameDialog(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
		if fileName:
			#print(fileName)
			
			self.data_Entrance(fileName)

	# 信號事件-多文件選擇
	def openFileNamesDialog(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
		if files:
			print(files)

		tmps = []
		for fpath in files:
			f = open(fpath,"r")
			obj = f.read()
			tmps.append(obj)

		f.close()

		txt = "\n".join(tmps)
		
		f = open("3.txt","a")
		f.write(txt)
		f.close()
			
	# 信號事件-保存文件
	def saveFileDialog(self):	
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
		if fileName:
			print(fileName)
		
def main():
	"""
	主函数，用于运行程序
	:return: None
	"""

	# 宣告
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()

	# 繼承原生UI介面
	ui = MyMainWindow()
	# 繪製UI介面
	ui.setupUi(MainWindow)
	# 顯示UI介面
	ui.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
