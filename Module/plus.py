# 設定與編碼
import configparser,codecs

from os import listdir
from os.path import isfile, isdir, join

config = configparser.ConfigParser()

from PyQt5 import QtCore, QtGui, QtWidgets

# ANSI 編碼
#config.read('example.ini')

#MainWindows.py
#加入代碼
#from Module.plus import DropLineEdit
#self.Task_lineEdit_filepath = DropLineEdit()

class DropLineEdit(QtWidgets.QLineEdit):

    inp_text_signal = QtCore.pyqtSignal(str)

    def __init__(self,parent=None):
        super(QtWidgets.QLineEdit,self).__init__(parent)
        ###初始化打开接受拖拽使能
        self.setAcceptDrops(True)

    def dragEnterEvent(self,event):
        event.accept()

    def dropEvent(self, event):
        ###获取拖放过来的文件的路径
        st = str(event.mimeData().urls())
        ########st就是Qt文件的路径。我们将这个路径稍作处理便可以得到我们想要的路径了
        #[PyQt5.QtCore.QUrl('file:///E:/Project/Python_Script/公司/專案/UI/002/100.txt')]
        st = st.replace(u"[PyQt5.QtCore.QUrl('file:///","")
        st = st.replace(u"')], ",",")
        st = st.replace("PyQt5.QtCore.QUrl(u'file:///","")
        st = st.replace("')]","")
        self.setText(st)
        self.inp_text_signal.emit(st)

def read(name):
    ### 讀取 Start ###
    # UTF-8編碼
    config.readfp(codecs.open("配置文件/" + str(name),"r","utf-8-sig"))

    # 預覽所有的Section名稱
    #print(config.sections())

    '''
    # 讀取整個Section
    single_section = config.items("basic")

    
    for item in single_section:
        # 名稱 , 數值
        print(item[0],item[1])

        # 檔案讀取 附值變數
        if(item[0] == "檔案路徑變數名稱"):
            title = item[1]
        
        if(item[0] == "檔案路徑"):
            value = open(item[1],"rb")

        if(item[0]=="post參數2"):
            print(title,"=",value,item[1])

    ### 讀取 End ###
'''
    
    return config
def write(dict_obj,name):
    ### 寫入 Start ###

    sections = dict_obj
    print(sections)
    for section in sections:
        print(section)
        config[section] = {}
        for key in sections[section]:
            #print("       ",key,sections[section][key])
            config[section][key] = str(sections[section][key])
            print(config[section][key])

    with codecs.open("配置文件/" + str(name) + '.ini',"w","utf-8-sig") as configfile:
        config.write(configfile)

def FileList():

    # 陣列變數 tmps 回傳檔案列表用
    tmps = []

    # 指定要列出所有檔案的目錄
    mypath = "配置文件"

    # 取得所有檔案與子目錄名稱
    files = listdir(mypath)

    # 以迴圈處理
    for f in files:
      # 產生檔案的絕對路徑
      fullpath = join(mypath, f)
      # 判斷 fullpath 是檔案還是目錄
      if isfile(fullpath):
        print("檔案：", f)
        tmps.append(f)
        
      elif isdir(fullpath):
        print("目錄：", f)

    return tmps
