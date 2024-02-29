from busanLibrary import BusanLibrary
# file : p41_naverNewsApp.py
# desc : PyQt5,QtDesigner naver API 연동 뉴스검색 앱 만들기

import sys
from PyQt5 import QtGui,QtCore,QtWidgets,uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import webbrowser
import datetime
import time

class qtApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self): # UI 파일을 로드해서 화면 디자인
        #self.setWindowIcon(QIcon('./images/newspaper.png'))
        uic.loadUi('./json/busanLibrary.ui',self)
        self.btnSearch.clicked.connect(self.btnSearchClicked) #버튼 서치 클릭시 처리
        self.tblSearch.cellDoubleClicked.connect(self.tblResultDoubleClicked) # 셀 더블 클릭시 처리
        self.show()

    def tblResultDoubleClicked(self): #셀 클릭시 처리
        selectRow = self.tblSearch.currentRow() #현재 선택된 행의 인덱스
        url = self.tblSearch.item(selectRow,3).text()
        webbrowser.open(url) # 웹브라우저에서 열기

    def btnSearchClicked (self): #버튼 서치 클릭시 처리
        searchWord = self.comboarea.currentText()
        if len(searchWord) == 0: #Validation Check(입력 검증)
            QMessageBox.about(self,'부산 도서관','검색어를 입력해주세요')
            return # 함수 탈출
        else:
            pass
        #검색 시작
        app = BusanLibrary() #api 객체 생성
        jsonSearch = app.getSearchResult(searchWord)
        # print(jsonSearch)
        self.makeTable(jsonSearch) # 검색 결과로 리스트뷰를 만드는 함수 호출


    def makeTable(self,data):
        try:
            result = data['getLibraryInfo']['body']['items']['item']
            self.tblSearch.setColumnCount(4)
            self.tblSearch.setRowCount(len(result))
            self.tblSearch.setHorizontalHeaderLabels(['도서관 이름','도서관 주소','도서관 전화 번호','도서관 홈페이지'])
            n = 0
            for post in result:
                self.tblSearch.setItem(n,0,QTableWidgetItem(post['library_nm']))
                self.tblSearch.setItem(n,1,QTableWidgetItem(post['library_addr']))
                self.tblSearch.setItem(n,2,QTableWidgetItem(post['library_tel']))
                self.tblSearch.setItem(n,3,QTableWidgetItem(post['library_hompage']))
                n+=1
            self.tblSearch.resizeColumnsToContents()
        except TypeError:
            QMessageBox.warning(self,'경고','제대로 된 구를 입력해주세요',buttons=QMessageBox.Ok)
            

    def closeEvent(self, QCloseEvent): # 오버라이드(재정의)
        re = QMessageBox.question(self,'종료확인','종료하시겠습니까?',QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
        if re == QMessageBox.Yes: #진짜 닫음
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
            QMessageBox.about(self,'취소','종료하지 않습니다.')

app = QApplication(sys.argv) #
inst = qtApp() #객체 생성

app.exec() # 실행



