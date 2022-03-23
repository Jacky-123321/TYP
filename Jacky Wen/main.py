import time
from PyQt5 import QtGui
from PyQt5.Qt import *
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url = 'https://httparchive.org/reports/state-of-the-web'
lens_list = ['drupal', 'magento', 'wordpress', 'top1k', 'top10k', 'top100k', 'top1m']
startDate_list = []
endDate_list = []
click_grid_button = True
click_list_button = False
#check_time = True

numUrls_text = ""
bytesTotal_text = ""
reqTotal_text = ""
pctHttps_text = ""
pctVuln_text = ""
tcp_text = ""
h2_text = ""
h3_text = ""
fontDisplay_text = ""

# def create_window():
# closed window
wd = webdriver.ChromeOptions()
wd.add_argument("headless")
wd = webdriver.Chrome(options=wd)


# return wd


# 浏览器驱动的打开 r 打开相对路径
# opened window
# wd = webdriver.Chrome(url)


def crawl_data(lens_p, startDate_p, endDate_p, check_time):
    try:
        wd.get(url)
        lens = wd.find_element(By.ID, 'lens')
        Select(lens).select_by_index(lens_p)
        # time.sleep(0.1)

        startDate = wd.find_element(By.ID, 'startDate')
        s1 = Select(startDate)
        if len(startDate_list) == 0:
            for select1 in s1.options:
                startDate_list.append(select1.text)
            print(startDate_list)
        else:
            s1.select_by_index(startDate_p)
        # time.sleep(0.1)

        endDate = wd.find_element(By.ID, 'endDate')
        s2 = Select(endDate)
        if len(endDate_list) == 0:
            for select2 in s2.options:
                endDate_list.append(select2.text)
            print(endDate_list)
        else:
            s2.select_by_index(endDate_p)
        # time.sleep(0.1)

        update_button = wd.find_element(By.ID, 'update')
        update_button.click()
        time.sleep(0.01)

        grid_view_button = wd.find_element(By.ID, 'grid-view')
        if click_grid_button:
            grid_view_button.click()
        time.sleep(0.01)

        list_view_button = wd.find_element(By.ID, 'list-view')
        if click_list_button:
            list_view_button.click()
        time.sleep(0.01)

        numUrls = wd.find_element(By.ID, 'numUrls')
        if check_time:
            global numUrls_text
            numUrls_text = numUrls.text
        else:
            numUrls_text = numUrls.text
        print(numUrls.text)

        bytesTotal = wd.find_element(By.ID, 'bytesTotal')
        if check_time:
            global bytesTotal_text
            bytesTotal_text = bytesTotal.text
        else:
            bytesTotal_text = bytesTotal.text
        print(bytesTotal.text)

        reqTotal = wd.find_element(By.ID, 'reqTotal')
        if check_time:
            global reqTotal_text
            reqTotal_text = reqTotal.text
        else:
            reqTotal_text = reqTotal.text
        print(reqTotal.text)

        pctHttps = wd.find_element(By.ID, 'pctHttps')
        if check_time:
            global pctHttps_text
            pctHttps_text = pctHttps.text
        else:
            pctHttps_text = pctHttps.text
        print(pctHttps.text)

        pctVuln = wd.find_element(By.ID, 'pctVuln')
        if check_time:
            global pctVuln_text
            pctVuln_text = pctVuln.text
        else:
            pctVuln_text = pctVuln.text
        print(pctVuln.text)

        tcp = wd.find_element(By.ID, 'tcp')
        if check_time:
            global tcp_text
            tcp_text = tcp.text
        else:
            tcp_text = tcp.text
        print(tcp.text)

        h2 = wd.find_element(By.ID, 'h2')
        if check_time:
            global h2_text
            h2_text = h2.text
        else:
            h2_text = h2.text
        print(h2.text)

        h3 = wd.find_element(By.ID, 'h3')
        if check_time:
            global h3_text
            h3_text = h3.text
        else:
            h3_text = h3.text
        print(h3.text)

        fontDisplay = wd.find_element(By.ID, 'fontDisplay')
        if check_time:
            global fontDisplay_text
            fontDisplay_text = fontDisplay.text
        else:
            fontDisplay_text = fontDisplay.text
        print(fontDisplay.text)



    except Exception as e:
        print("Error on crawling")
    # wd.close()


class Window(QWidget):
    def __init__(self):
        super().__init__()
        window = QWidget()
        self.lens_select = QComboBox(self.window())
        self.lens_select.move(100, 50)
        self.lens_select.addItems(lens_list)
        lens_selected = self.lens_select.currentText()
        print(lens_selected)

        lens_label = QLabel(self.window())
        lens_label.move(130, 30)
        lens_label.setText("LENS")
        lens_label.setStyleSheet("color:white")

        self.startDate_select = QComboBox(self.window())
        self.startDate_select.move(250, 50)
        self.startDate_select.addItems(startDate_list)
        startDate_selected = self.startDate_select.currentText()
        print(startDate_selected)

        startDate_label = QLabel(self.window())
        startDate_label.move(280, 30)
        startDate_label.setText("START-DATE")
        startDate_label.setStyleSheet("color:white")

        self.endDate_select = QComboBox(self.window())
        self.endDate_select.move(400, 50)
        self.endDate_select.addItems(endDate_list)
        endDate_selected = self.endDate_select.currentText()
        print(endDate_selected)

        endDate_label = QLabel(self.window())
        endDate_label. move(430, 30)
        endDate_label.setText("END-DATE")
        endDate_label.setStyleSheet("color:white")

        global numUrls_label
        numUrls_label = QLabel(self.window())
        numUrls_label.move(100, 100)
        numUrls_label.setStyleSheet("border-width: 3px;border-style: solid;border-color: white;color:white")
        #numUrls_label.setStyleSheet("background-color:while")
        numUrls_label.setAlignment(Qt.AlignCenter)

        global bytesTotal_label
        bytesTotal_label = QLabel(self.window())
        bytesTotal_label.move(100, 250)
        bytesTotal_label.setStyleSheet("border-width: 3px;border-style: solid;border-color: white;color:white")
        bytesTotal_label.setAlignment(Qt.AlignCenter)

        global reqTotal_label
        reqTotal_label = QLabel(self.window())
        reqTotal_label.move(100, 400)
        reqTotal_label.setStyleSheet("border-width: 3px;border-style: solid;border-color: white;color:white")
        reqTotal_label.setAlignment(Qt.AlignCenter)

        global pctHttps_label
        pctHttps_label = QLabel(self.window())
        pctHttps_label.move(300, 100)
        pctHttps_label.setStyleSheet("border-width: 3px;border-style: solid;border-color: white;color:white")
        pctHttps_label.setAlignment(Qt.AlignCenter)

        global pctVuln_label
        pctVuln_label = QLabel(self.window())
        pctVuln_label.move(300, 250)
        pctVuln_label.setStyleSheet("border-width: 3px;border-style: solid;border-color: white;color:white")
        pctVuln_label.setAlignment(Qt.AlignCenter)

        global tcp_label
        tcp_label = QLabel(self.window())
        tcp_label.move(300, 400)
        tcp_label.setStyleSheet("border-width: 3px;border-style: solid;border-color: white;color:white")
        tcp_label.setAlignment(Qt.AlignCenter)

        global h2_label
        h2_label = QLabel(self.window())
        h2_label.move(500, 100)
        h2_label.setStyleSheet("border-width: 3px;border-style: solid;border-color: white;color:white")
        h2_label.setAlignment(Qt.AlignCenter)

        global h3_label
        h3_label = QLabel(self.window())
        h3_label.move(500, 250)
        h3_label.setStyleSheet("border-width: 3px;border-style: solid;border-color: white;color:white")
        h3_label.setAlignment(Qt.AlignCenter)

        global fontDisplay_label
        fontDisplay_label = QLabel(self.window())
        fontDisplay_label.move(500, 400)
        fontDisplay_label.setStyleSheet("border-width: 3px;border-style: solid;border-color: white;color:white")
        fontDisplay_label.setAlignment(Qt.AlignCenter)

        self.search_button = QPushButton(self.window())
        self.search_button.move(600, 50)
        self.search_button.setText("Search")
        self.search_button.setDefault(False)
        self.search_button.clicked.connect(lambda: self.click_button())

    def click_button(self):

        lens_selected = self.lens_select.currentIndex()
        startDate_selected = self.startDate_select.currentIndex()
        endDate_selected = self.endDate_select.currentIndex()
        if startDate_selected > (endDate_selected - 1):
            print(lens_selected + startDate_selected + endDate_selected)
            crawl_data(lens_selected, startDate_selected, endDate_selected, False)
            self.set_data()
        else:
            msgBox = QMessageBox()
            msgBox.setText("The chosen endDate has to be later that startDate")
            msgBox.setStandardButtons(QMessageBox.Cancel)
            msgBox.setDefaultButton(QMessageBox.Cancel)
            ret = msgBox.exec_()

    def set_data(self):
        numUrls_label.setText(numUrls_text)
        bytesTotal_label.setText(bytesTotal_text)
        reqTotal_label.setText(reqTotal_text)
        pctHttps_label.setText(pctHttps_text)
        pctVuln_label.setText(pctVuln_text)
        tcp_label.setText(tcp_text)
        h2_label.setText(h2_text)
        h3_label.setText(h3_text)
        fontDisplay_label.setText(fontDisplay_text)
        self.window().show()
        QApplication.processEvents()



if __name__ == "__main__":
    crawl_data(1, 1, 1, True)
    app = QApplication(sys.argv)
    win = Window()
    win.setWindowTitle("Httparchive")
    win.setFixedSize(700, 600)
    win.resize(700, 600)
    palette = QtGui.QPalette()
    image = QtGui.QPixmap()
    image.load(r'Background1.jpeg')
    palette.setBrush(win.backgroundRole(), QtGui.QBrush(image))
    win.setPalette(palette)
    win.setAutoFillBackground(True)
    win.set_data()
    sys.exit(app.exec_())
pass
