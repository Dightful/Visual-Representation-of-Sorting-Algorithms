
from datetime import datetime
from PyQt5.QtCore import QTime, QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import re
import sys
import sorting_panel_graphical 
import control_panel_graphical2
import SecondaryFile
import sqlite3


#D:\WpSystem\S-1-5-21-2590028653-3541449427-884558286-1010\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\Scripts\pyuic5.exe -x "D:\0Good\SCHOLL\compu\y13 oproject\infomation page (1).ui" -o "D:\0Good\SCHOLL\compu\y13 oproject\part 3\infomation_page_graphical.py"
#C:\Python\Scripts\pyuic5.exe -x "C:\Users\dight\Documents\coding\school\y13 oproject\infomation page.ui" -o "C:\Users\dight\Documents\coding\school\y13 oproject\part 2\infomation_page_graphical.py"



file_location = "D:\\0Good\\coding\\python2\\00mine stuff\\0projects\\NEA visual representation of sorting algos\\white.png"
class SecondWindow(QtWidgets.QMainWindow, sorting_panel_graphical.Ui_MainWindow):              # +
    def __init__(self):
        super(SecondWindow, self).__init__()
        self.setupUi(self)
        
        self.showFullScreen()
        
        self.call_in_image(file_location)
        self.pixmap = QPixmap(file_location)
        self.scale = 1

    def zooming(self,zoom,file_location,way):

        if zoom == True:
            if way == True:
                self.scale *= 1.5
            else:
                self.scale *= 0.5
        else:
            self.pixmap = QPixmap(file_location)
        
        size = self.pixmap.size()

        scaled_pixmap = self.pixmap.scaled(self.scale * size)

        self.label_2.setPixmap(scaled_pixmap)



    def call_in_image(self, file_location):
        self.label_2.setPixmap(QtGui.QPixmap(file_location))
        

    def display_randomized(self,location):      
        self.label_2.setPixmap(QtGui.QPixmap(location))
        self.zooming(False, location, False)

    def display_randomized2(self,location):      
            self.label_2.setPixmap(QtGui.QPixmap(location))
            self.zooming(False, location, False)
            QApplication.processEvents()

    def close(self):
        sys.exit()


class MainWindow(QtWidgets.QMainWindow, control_panel_graphical2.Ui_MainWindow):   

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self) 
        
        #adding items to combo box
        self.comboBox.addItem("Insertion") #DONE 
        self.comboBox.addItem("Shell") #DONE     #
        self.comboBox.addItem("Bubble") #DONE    #   
        self.comboBox.addItem("Cocktail") #DONE  #
        self.comboBox.addItem("Quick") #DONE     #
        self.comboBox.addItem("Selection") #DONE #
        self.comboBox.addItem("Radix") #DONE     #
        self.comboBox.addItem("Bucket") # DONE   
        self.comboBox.addItem("Heap") # DONE     #
        self.image_chosen = False
        self.randomized = False
        self.randomizeddone = False
        self.textEdit_2.setText("0.0s")
        self.hgrouped_together = 0
        self.firstrun = True
        self.startbutton_2.clicked.connect(lambda : self.randomize_img(self.lineEdit.text()))
        self.startbutton.clicked.connect(lambda : self.Start(self.lineEdit.text()))
        self.Close_Sorting_Window_2.clicked.connect(self.close)
        self.pushButton_4.clicked.connect(lambda: w2.zooming(True,file_location, True))
        self.pushButton_5.clicked.connect(lambda: w2.zooming(True,file_location, False))
        self.startbutton_3.clicked.connect(self.open_new_window)
        self.startbutton_5.clicked.connect(self.open_new_window2)
        self.pushButton_3.clicked.connect(self.upload_database)
        self.pushButton_2.clicked.connect(self.to_database)
        self.update_Button.clicked.connect(self.update_times)

    def update_times(self):
        self.display_times()
  
    def repalce(self, char):
        results4 = results4.replace(char,"")
        return results4

    def display_times(self):
        connection3 = sqlite3.connect('D:\\0Good\\coding\\python2\\00mine stuff\\0projects\\NEA visual representation of sorting algos\\database_sorting_algos2.db')
        cur = connection3.cursor()
        if self.image_chosen == False:
            self.textEdit_3.setText("N/A")
            self.textEdit_4.setText("N/A")
            self.textEdit_5.setText("No resolution")
            self.textEdit_6.setText("Choose Image")
        else:
            resolution_not_multiplyed = self.textEdit.toPlainText()
            resolution_not_multiplyed_1 = re.search(r'(.*?)x', resolution_not_multiplyed).group(1)
            resolution = resolution_not_multiplyed[len(resolution_not_multiplyed_1)+1:]
            resolution_multiplyed = int(resolution_not_multiplyed_1) * int(resolution)
            sqlquer2 = (f'SELECT Time FROM Runs2 WHERE Resolution = "{resolution_multiplyed}"')
            sqlquer3 = (f'SELECT Algorithm FROM Runs2 WHERE Resolution = "{resolution_multiplyed}"')
            cur.execute(sqlquer3)
            AlgoResults = cur.fetchall()
            arr1 = []
            for i in AlgoResults:
                i = str(i)
                i = i.replace(",","")
                i = i.replace("(","")
                i = i.replace(")","")
                arr1.append(str(i))
            
            cur.execute(sqlquer2)
            results = cur.fetchall()
            arr2 = []
            for i in results:
                i = str(i)
                i = i.replace(",","")
                i = i.replace("(","")
                i = i.replace(")","")
                arr2.append(str(i))
            if arr2 == []:
                self.textEdit_3.setText("N/A")
                self.textEdit_4.setText("N/A")
            else:
                arr3 = []
                for i in arr2:
                    i = float(i)
                    arr3.append(i)

                minTime = min(arr3)
                maxTime = max(arr3)
                self.textEdit_3.setText(str(minTime))
                self.textEdit_4.setText(str(maxTime))
                indexMin = arr3.index(minTime)
                indexMax = arr3.index(maxTime)
                AlgoMin = arr1[indexMin]
                AlgoMax = arr1[indexMax]
                sqlstr4 = (f'SELECT Algorithm FROM Algorithms WHERE ID = "{(AlgoMin)}" ')
                cur.execute(sqlstr4)
                results4 = (str(cur.fetchall()))
                sqlstr5 = (f'SELECT Algorithm FROM Algorithms WHERE ID = "{(AlgoMax)}" ')
                cur.execute(sqlstr5)
                results5 = (str(cur.fetchall()))
                print(results4)
                AlgoMin = re.search(r"'(.*?)'", results4).group(1)
                AlgoMax = re.search(r"'(.*?)'", results5).group(1)
                self.textEdit_5.setText(AlgoMin)
                self.textEdit_6.setText(AlgoMax)

    def to_database(self):
        plz = DataBWindow()
        method2 = plz.loading
        method2()     

        
        widget.setFixedHeight(800)
        widget.setFixedWidth(1051)
        widget.move(200,200)
        widget.setCurrentIndex(widget.currentIndex()+2)


    def upload_database(self):
        #add data to database
        if self.randomizeddone == True:
            connection2 = sqlite3.connect('D:\\0Good\\coding\\python2\\00mine stuff\\0projects\\NEA visual representation of sorting algos\\database_sorting_algos2.db')
            cur = connection2.cursor()
            
            sqlstr2 = ('SELECT RunID FROM Runs2')
            cur.execute(sqlstr2)
            results = str(cur.fetchall())
            print(results)
            print()
            for i in range(len(str(results))):
                try:
                    if int(results[-(i)] ) / 100000000 != 9:
                        results2 = (int(results[-(i)]))
                        self.firstrun = False
                        break
                except:
                    pass
            if self.firstrun == True:
                runid = 1
            else:
                runid = int(results2) + 1

            algorith = self.comboBox.currentText()
            sqlquer = (f'SELECT ID FROM Algorithms WHERE Algorithm == "{algorith}"')
            cur.execute(sqlquer)
            algorithmId = str(cur.fetchall())
            algorithmId = float(algorithmId[2:3])

            resolution_not_multiplyed = self.textEdit.toPlainText()
            resolution_not_multiplyed_1 = re.search(r'(.*?)x', resolution_not_multiplyed).group(1)
            resolution = resolution_not_multiplyed[len(resolution_not_multiplyed_1)+1:]
            resolution_multiplyed = int(resolution_not_multiplyed_1) * int(resolution)
            time_taken = str(self.textEdit_2.toPlainText())
            time_taken = float(time_taken[:-2])
            
            grouped_together = str(self.lineEdit.text())
            if grouped_together == "":
                grouped_together = 1

            cur.execute(f"INSERT OR IGNORE INTO Runs2 VALUES ({runid},'{resolution_multiplyed}',{grouped_together},'{time_taken}',{algorithmId})")
            connection2.commit()
            connection2.close()

        
    
    def resolution(self, file_location):
        #print(file_location)
        width, heigh = SecondaryFile.resolution_finder(file_location, True)

        self.textEdit.setText(str(width) + " x " + str(heigh))
    
    def open_new_window(self):
        self.image_chosen = True
        widget.setCurrentIndex(widget.currentIndex()-1)
        widget.move(600,200)
        widget.setFixedHeight(550)
        widget.setFixedWidth(1000)
        
    def open_new_window2(self):
        self.image_chosen = True
        widget.setCurrentIndex(widget.currentIndex()-2)
        widget.move(0,0)
        widget.setFixedHeight(1000)
        widget.setFixedWidth(1920)
    
    def randomize_img(self, grouped_together):
        if grouped_together == "":
            grouped_together = 0
        self.randomized = True
        with open ("image_location.txt","r") as file:
            file_location = file.read()
        print()
        if __name__ == "__main__":
            n = int(grouped_together)
            SecondaryFile.runner(w2, file_location, n)

# litrally create a normal python timer, get the current timer every 10 ms and display using self.textEdit_2.setText(str(self.count))
    def close(self):
        sys.exit()


    def time_take(self,time_taken):      
        time_taken = str(time_taken)[0:6]
        self.textEdit_2.setText(str(time_taken) + " s")
  
    def Start(self, grouped):
        if grouped == "":
            grouped = 0
        else:
            grouped = int(grouped)

        if self.randomized == True:
            if __name__ == "__main__":
                sorting_algo = self.comboBox.currentText()
                with open ("values_needed_for_sorting_function.txt","r") as file:
                    if grouped > 0:
                        n2 = file.readlines()
                        n2 = str(n2)
                        n2 = n2[2:-2]
                        #print(n2)
                        dict1 = re.search(r';(.*?);', n2).group(1)
                        length_dict = len(dict1)
                        n2 = n2[length_dict+1:]
                        loc2 = re.search(r';(.*?),', n2).group(1)
                        length_dict = len(loc2)
                        n2 = n2[length_dict+1:]
                        x_value = re.search(r',(.*?),', n2).group(1)
                        length_dict = len(x_value)
                        n2 = n2[length_dict+2:]
                        y_value = n2
                        #print(x_value)
                        SecondaryFile.connecting_randomDict_to_sort_algo(dict1,loc2,x_value,y_value,w2,My_FourthWindow, sorting_algo, grouped)

                    else:
                        x = file.readlines()
                        string_contents = (x[0])
                        #print(string_contents)
                        dict1 = re.search(r'{(.*?)}', string_contents).group(1)
                        dict1 = "{" + dict1 + "}"
                        length_dict = len(dict1)
                        string_contents = string_contents[length_dict+1:]#removing the first part of the string, known how long due to getting the length of dict
                        loc2 = re.search(r'(.*?),', string_contents).group(1)
                        string_contents = string_contents[len(loc2)+1:]
                        xx = re.search(r'(.*?),', string_contents).group(1)
                        string_contents = string_contents[len(xx)+1:]
                        yx = string_contents

                        SecondaryFile.connecting_randomDict_to_sort_algo(dict1,loc2,xx,yx,w2,My_FourthWindow, sorting_algo, grouped)
            open("values_needed_for_sorting_function.txt", "w").close()# this is to remove contents of file so it is clear for the next run
            print("END")
            self.randomizeddone = True
        else:
            print("Sorry you need to randomize image first")
            

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
import re
import PIL


import mainwindow_graphical 

class FirstWindow(QtWidgets.QMainWindow, mainwindow_graphical.Ui_MainWindow):              # +
    def __init__(self):
        super(FirstWindow, self).__init__()
        self.setupUi(self)
        self.random_image_button.clicked.connect(self.next)
        self.pushButton_3.clicked.connect(self.info_window)
        self.pushButton_4.clicked.connect(self.dataB)
    def next(self):
        widget.setFixedHeight(410)
        widget.setFixedWidth(578)
        widget.move(1200,500)
        widget.setCurrentIndex(widget.currentIndex()+3)
    def info_window(self):
        #widget.showFullScreen()
        widget.setCurrentIndex(widget.currentIndex()+4)

    def dataB(self):
        widget.setFixedHeight(800)
        widget.setFixedWidth(1051)
        widget.move(200,200)
        widget.setCurrentIndex(widget.currentIndex()+5)


        
import select_random_graphical

    
class SecondWindow_M(QtWidgets.QMainWindow, select_random_graphical.Ui_MainWindow):              # +
    def __init__(self):
        super(SecondWindow_M, self).__init__()
        self.setupUi(self)
        widget.move(0,0)
        self.count = 0
        self.Wpath = r"D:\\0Good\\coding\\python2\\00mine stuff\\0projects\NEA visual representation of sorting algos\\"
        self.array_of_pics = ["Porsche 911 GT3 manual .jpg","cadilac.png","Mazda RX-7.jpg","Honda Civic Type-R EK9.png","mustang.png","audiR8.jpg","Subaru Impreza WRX STI 1st gen.png","32x32.png"]
        self.pictures.setPixmap(QtGui.QPixmap(self.Wpath + self.array_of_pics[-1]))
        self.reroll_button.clicked.connect(self.re_roll_image)
        self.back_button.clicked.connect(self.back_button2)
        self.continue_button.clicked.connect(lambda : self.continue_to_next(self.Wpath + self.array_of_pics[self.count-1]))
        

    def back_button2(self):
        global widget_order

        widget.setFixedHeight(410)
        widget.setFixedWidth(578)
        widget.move(1200,500)
        widget.setCurrentIndex(widget.currentIndex()+2)
           

    def re_roll_image(self):

        if self.count+2 > len(self.array_of_pics):
            self.pictures.setPixmap(QtGui.QPixmap(self.Wpath + self.array_of_pics[self.count]))
            self.count = 0
        else:
            self.pictures.setPixmap(QtGui.QPixmap(self.Wpath + self.array_of_pics[self.count]))
            self.count += 1

    def continue_to_next(self,image_location):
        global w2
        global My_FourthWindow
        global widget_order
        resolution_of_image = (self.resolution_finder(image_location))
        resolution_of_image = str(resolution_of_image)
        resolution_of_image = ''.join((resolution_of_image,' '))
        width = re.search(r'= (.*?)x', resolution_of_image).group(1)
        height = re.search(r'x(.*?) ', resolution_of_image).group(1)
        widget.setFixedHeight(800)
        widget.setFixedWidth(800)
        with open ("image_location.txt","w") as file:
            file.write(image_location)
        w2.display_randomized(image_location)
        My_FourthWindow.resolution(image_location)
        widget.setCurrentIndex(widget.currentIndex()+2)
        widget_order = False
        widget.setFixedHeight(410)
        widget.setFixedWidth(578)
        widget.move(1200,500)


    def resolution_finder(self, file):
        img = PIL.Image.open(file)

        # fetching the dimensions
        wid, hgt = img.size

        # displaying the dimensions
        resolution = ("Resolution = " + str(wid) + "x" + str(hgt))
        return resolution

import select_image_graphical 

class ThirdWindow(QtWidgets.QMainWindow, select_image_graphical.Ui_MainWindow):              # +
    def __init__(self):
        super(ThirdWindow, self).__init__()
        self.setupUi(self)

        self.actionOpen.triggered.connect(self.browsefiles)
        self.clear_Button.clicked.connect(self.delte_button)
        self.back_button.clicked.connect(self.back_button2)
        self.continue_button.clicked.connect(self.continueing)

    def back_button2(self):
        global widget_order

        widget.setFixedHeight(410)
        widget.setFixedWidth(578)
        widget.move(1200,500)
        widget.setCurrentIndex(widget.currentIndex()+1)
            

    def browsefiles(self):
        #fname = QFileDialog.getOpenFileName(self, "Open file","", "All Files (*);;Python Files (*.py)")
        fname, placeholder = QFileDialog.getOpenFileName(None, 'Select file') #only jpg nd png
        if fname:
            self.lineEdit.setText(fname)
            file_location = str(fname)

    def continueing(self):
        global w2
        global widget
        global widget_order
        file_location = self.lineEdit.text()
        #print(file_location)
        file_location = file_location.replace("/","\\")
        with open ("image_location.txt","w") as file:
            file.write(file_location)
        w2.display_randomized(file_location)
        My_FourthWindow.resolution(file_location)
        #widget.close()
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget_order = False
        widget.setFixedHeight(410)
        widget.setFixedWidth(578)
        widget.move(1200,500)

    def delte_button(self):
        self.lineEdit.setText("")

import infomation_page_graphical 

class InfoWindow(QtWidgets.QMainWindow, infomation_page_graphical.Ui_MainWindow):              # +
    def __init__(self):
        super(InfoWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.back_button)
        self.pushButton_2.clicked.connect(self.exit_button)

    def back_button(self):
        widget.setCurrentIndex(widget.currentIndex()-4)
    def exit_button(self):
        sys.exit()

import sql_graphical


class DataBWindow(QtWidgets.QMainWindow, sql_graphical.Ui_MainWindow):
    def __init__(self):
        super(DataBWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.back)
        self.pushButton_2.clicked.connect(self.exit)
        self.pushButton_3.clicked.connect(self.loading)
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 150)
        self.loading()

    
    def back(self):
        widget.setFixedHeight(1079)
        widget.setFixedWidth(1920)
        widget.move(0,0)
        widget.setCurrentIndex(widget.currentIndex()-5)

    def exit(self):
        sys.exit()

    def loading(self):
        connection = sqlite3.connect('D:\\0Good\\coding\\python2\\00mine stuff\\0projects\\NEA visual representation of sorting algos\\database_sorting_algos2.db')
        cur = connection.cursor()
        sqlstr = 'SELECT * FROM Runs2'
        results = cur.execute(sqlstr)
        tablerow = 0
        self.tableWidget.setRowCount(0)
        self.tableWidget.setRowCount(200)
        for col in results:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(col[0])))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(col[1])))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(col[2])))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(col[3])))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(col[4])))
            tablerow += 1

        sqlstr = 'SELECT * FROM Algorithms'
        results = cur.execute(sqlstr)
        tablerow = 0
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setRowCount(9)
        for col in results:
            self.tableWidget_2.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(col[0])))
            self.tableWidget_2.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(col[1])))
            tablerow += 1
        connection.close()    

if __name__ == "__main__":
    app2 = QApplication(sys.argv)
    w2 = SecondWindow()
    w2.show()
    widget_order = True
    widget = QtWidgets.QStackedWidget()
    My_FirstWindow = FirstWindow()
    My_SecondWindow = SecondWindow_M()
    My_ThirdWindow = ThirdWindow()
    My_FourthWindow = MainWindow()
    My_FifthWindow = InfoWindow()
    My_SixthWindow = DataBWindow()
    widget.addWidget(My_FirstWindow)
    widget.addWidget(My_SecondWindow)
    widget.addWidget(My_ThirdWindow)
    widget.addWidget(My_FourthWindow)
    widget.addWidget(My_FifthWindow)
    widget.addWidget(My_SixthWindow)
    widget.show()
    widget.setFixedHeight(1079)
    widget.setFixedWidth(1920)

    
    sys.exit(app2.exec_())

    