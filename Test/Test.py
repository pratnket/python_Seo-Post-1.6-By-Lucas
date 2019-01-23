import time
from PyQt5 import QtWidgets
from untitled import Ui_Form
 
import multiprocessing
import threading


class HandleSubProcess(multiprocessing.Process):
	def __init__(self, child_conn):
		super(HandleSubProcess, self).__init__()
		self.child_conn = child_conn
		
		pass
	
	def run(self):
		cnt = 0
		while True:
			self.child_conn.send("handleSubprocess\t"+str(cnt))
			cnt += 1
			self.delay()
			pass
		pass
	
	def delay(self, timeout=9999999):
		cnt = timeout
		while cnt>0:
			cnt -= 1
			pass
		pass
	pass

class mywindow(QtWidgets.QWidget,Ui_Form):
	def __init__(self):
		super(mywindow,self).__init__()
		self.setupUi(self)
		self.private_variable()
		self.register()
		self.connect()

		self.Queue = multiprocessing.Queue()

		parent_conn, child_conn = multiprocessing.Pipe()
		self.p = HandleSubProcess(child_conn)

		self.t1 = threading.Thread(target=self.run_thread, args=(parent_conn,self.p))
		self.p.start()
		self.t1.start()

		# 格式 
		# 1.print("說明","方法名稱")
		# 2.宣告變數 or 全局變數
		# 3.賦予私有變數
		# 4.私用變數 調用方法
		# 5.請遵守以上規範來維持代碼的統一性
	
	def private_variable(self):
		self.private = {}
		# 透過 字串的有無 控制 print 是否使用
		self.private["print_switch"] = " "

	def register(self):
		# 介面變數 宣告 self 類別專用的全局變數
		self.ui = {} # 2
		self.ui["pushButton"] = self.pushButton # 2

	def connect(self):
		# 1
		for _ in self.private["print_switch"]:
			print("綁定事件","connect")

		pushButton = self.ui["pushButton"] # 3
		pushButton.clicked.connect(self.click_1) # 4

	def click_1(self):
		# 1
		for _ in self.private["print_switch"]:
			print("滑鼠點擊事件1","click_1")

		#self.p.is_alive = 0
		self.Queue.put("111")

	def run_thread(self, parent_conn, pp,):
		while pp.is_alive:
			#self.textEdit.append(parent_conn.recv())

			val = self.Queue.get()
			print(val)

			print(parent_conn.recv())
			self.delay()
			pass
		print ("==== run_thread  end ==================\n")
		pass

	def delay(self, timeout=9999999):
		cnt = timeout
		while cnt>0:
			cnt -= 1
			pass
		pass
	pass

if __name__=="__main__":
	import sys
 
	app=QtWidgets.QApplication(sys.argv)
	myshow=mywindow()
	myshow.show()
	sys.exit(app.exec_())