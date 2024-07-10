# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AppTie.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import numpy
import EIT.eit as TIE
from EIT import Comunica
import time
import cv2
import csv
import threading



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(917, 629)
        MainWindow.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Aplic = QtWidgets.QTabWidget(self.centralwidget)
        self.Aplic.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.Aplic.setAutoFillBackground(False)
        self.Aplic.setObjectName("Aplic")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setMinimumSize(QtCore.QSize(350, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBoxArquivos = QtWidgets.QGroupBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxArquivos.sizePolicy().hasHeightForWidth())
        self.groupBoxArquivos.setSizePolicy(sizePolicy)
        self.groupBoxArquivos.setMinimumSize(QtCore.QSize(300, 200))
        self.groupBoxArquivos.setMaximumSize(QtCore.QSize(500, 200))
        self.groupBoxArquivos.setObjectName("groupBoxArquivos")
        self.formLayout = QtWidgets.QFormLayout(self.groupBoxArquivos)
        self.formLayout.setObjectName("formLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.Bt_sensibilidade = QtWidgets.QPushButton(self.groupBoxArquivos)
        self.Bt_sensibilidade.setMinimumSize(QtCore.QSize(120, 0))
        self.Bt_sensibilidade.setObjectName("Bt_sensibilidade")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Bt_sensibilidade)
        self.Line_sensibilidade = QtWidgets.QLineEdit(self.groupBoxArquivos)
        self.Line_sensibilidade.setObjectName("Line_sensibilidade")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Line_sensibilidade)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.Bt_tense_ref = QtWidgets.QPushButton(self.groupBoxArquivos)
        self.Bt_tense_ref.setMinimumSize(QtCore.QSize(120, 0))
        self.Bt_tense_ref.setMaximumSize(QtCore.QSize(200, 16777215))
        self.Bt_tense_ref.setObjectName("Bt_tense_ref")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Bt_tense_ref)
        self.Line_tense_ref = QtWidgets.QLineEdit(self.groupBoxArquivos)
        self.Line_tense_ref.setObjectName("Line_tense_ref")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Line_tense_ref)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        self.Bt_medidas = QtWidgets.QPushButton(self.groupBoxArquivos)
        self.Bt_medidas.setMinimumSize(QtCore.QSize(120, 0))
        self.Bt_medidas.setObjectName("Bt_medidas")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Bt_medidas)
        self.Line_medida = QtWidgets.QLineEdit(self.groupBoxArquivos)
        self.Line_medida.setObjectName("Line_medida")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.Line_medida)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.LabelRole, spacerItem3)
        self.verticalLayout.addWidget(self.groupBoxArquivos)
        self.groupBoxMetodo = QtWidgets.QGroupBox(self.groupBox)
        self.groupBoxMetodo.setObjectName("groupBoxMetodo")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBoxMetodo)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.radio_landwaber = QtWidgets.QRadioButton(self.groupBoxMetodo)
        self.radio_landwaber.setObjectName("radio_landwaber")
        self.gridLayout_4.addWidget(self.radio_landwaber, 2, 0, 1, 1)
        self.landIntera = QtWidgets.QSpinBox(self.groupBoxMetodo)
        self.landIntera.setMaximum(100)
        self.landIntera.setObjectName("landIntera")
        self.gridLayout_4.addWidget(self.landIntera, 2, 1, 1, 1)
        self.Radio_projeo = QtWidgets.QRadioButton(self.groupBoxMetodo)
        self.Radio_projeo.setObjectName("Radio_projeo")
        self.gridLayout_4.addWidget(self.Radio_projeo, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxMetodo)
        self.groupBoxReconstru = QtWidgets.QGroupBox(self.groupBox)
        self.groupBoxReconstru.setObjectName("groupBoxReconstru")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBoxReconstru)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Bt_reconstruirImagem = QtWidgets.QPushButton(self.groupBoxReconstru)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Img_Eit/ImgTab.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Bt_reconstruirImagem.setIcon(icon)
        self.Bt_reconstruirImagem.setObjectName("Bt_reconstruirImagem")
        self.gridLayout_3.addWidget(self.Bt_reconstruirImagem, 1, 0, 1, 1)
        self.Bt_capturarImagem = QtWidgets.QPushButton(self.groupBoxReconstru)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Img_Eit/ImgRec.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Bt_capturarImagem.setIcon(icon1)
        self.Bt_capturarImagem.setObjectName("Bt_capturarImagem")
        self.gridLayout_3.addWidget(self.Bt_capturarImagem, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxReconstru)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout.addWidget(self.groupBox)
        self.line_12 = QtWidgets.QFrame(self.tab)
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.horizontalLayout.addWidget(self.line_12)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(300, 300))
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem4 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 1, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 0, 1, 1, 1)
        self.Imagem_TIE = QtWidgets.QLabel(self.groupBox_2)
        self.Imagem_TIE.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.Imagem_TIE.setPixmap(QtGui.QPixmap("Img_Eit/LogoEit.png"))
        self.Imagem_TIE.setObjectName("Imagem_TIE")
        self.gridLayout.addWidget(self.Imagem_TIE, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Img_Eit/ImgTab.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Aplic.addTab(self.tab, icon2, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line_11 = QtWidgets.QFrame(self.tab_2)
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.gridLayout_2.addWidget(self.line_11, 1, 2, 1, 1)
        self.line_9 = QtWidgets.QFrame(self.tab_2)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_2.addWidget(self.line_9, 1, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_3)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_5.addWidget(self.progressBar, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_3, 3, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.tab_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 2, 1, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.tab_2)
        self.line_6.setWindowModality(QtCore.Qt.WindowModal)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_2.addWidget(self.line_6, 0, 1, 1, 1)
        self.MedidasTens = QtWidgets.QGroupBox(self.tab_2)
        self.MedidasTens.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.MedidasTens.setAlignment(QtCore.Qt.AlignCenter)
        self.MedidasTens.setObjectName("MedidasTens")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.MedidasTens)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.grupoStatus = QtWidgets.QGroupBox(self.MedidasTens)
        self.grupoStatus.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grupoStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.grupoStatus.setObjectName("grupoStatus")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.grupoStatus)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem8, 1, 2, 1, 1)
        self.Img_status = QtWidgets.QLabel(self.grupoStatus)
        self.Img_status.setMinimumSize(QtCore.QSize(300, 300))
        self.Img_status.setText("")
        self.Img_status.setPixmap(QtGui.QPixmap("Img_Eit/desconhecido.png"))
        self.Img_status.setObjectName("Img_status")
        self.gridLayout_7.addWidget(self.Img_status, 1, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem9, 1, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem10, 2, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem11, 0, 1, 1, 1)
        self.gridLayout_6.addWidget(self.grupoStatus, 1, 1, 5, 1)
        self.pushButton = QtWidgets.QPushButton(self.MedidasTens)
        self.pushButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_6.addWidget(self.pushButton, 2, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.MedidasTens)
        self.pushButton_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_6.addWidget(self.pushButton_2, 3, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem12, 1, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem13, 4, 0, 1, 1)
        self.gridLayout_2.addWidget(self.MedidasTens, 1, 1, 1, 1)
        self.Aplic.addTab(self.tab_2, icon2, "")
        self.horizontalLayout_2.addWidget(self.Aplic)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 917, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.Aplic.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #Variaveis utilizadas no sistema.
        self.routeSensibilidade = None
        self.routeTenseRef = None
        self.routeMeasure = None
        self.imagem = None
        self.listaLeituras = list()


        #set eventos de click
        self.Bt_sensibilidade.clicked.connect(self.setSensibilidade)
        self.Bt_medidas.clicked.connect(self.setMeasure)
        self.Bt_tense_ref.clicked.connect(self.setTenseRef)

        self.Bt_reconstruirImagem.clicked.connect(self.rebuidIMG)

        self.Bt_capturarImagem.clicked.connect(self.saveIMG)
        
        self.pushButton.clicked.connect(self.saveLeituras)

        self.pushButton_2.clicked.connect(self.realizaAquis)
        
        

        
        #desabilitar botões
        self.Bt_capturarImagem.setEnabled(False)
        
        self.pushButton.setEnabled(False)
        
        self.progressBar.setValue(0)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "COMANDOS"))
        self.groupBoxArquivos.setTitle(_translate("MainWindow", "ARQUIVOS DE CONFIGURAÇÕES"))
        self.Bt_sensibilidade.setText(_translate("MainWindow", "Sensibilidade"))
        self.Line_sensibilidade.setText(_translate("MainWindow", ""))
        self.Bt_tense_ref.setText(_translate("MainWindow", " Referência"))
        self.Line_tense_ref.setText(_translate("MainWindow", ""))
        self.Bt_medidas.setText(_translate("MainWindow", "Medidas"))
        self.Line_medida.setText(_translate("MainWindow", ""))
        self.groupBoxMetodo.setTitle(_translate("MainWindow", "Método"))
        self.radio_landwaber.setText(_translate("MainWindow", "LandWeber"))
        self.Radio_projeo.setText(_translate("MainWindow", "Retroprojeção linear"))
        self.groupBoxReconstru.setTitle(_translate("MainWindow", "Reconstrução"))
        self.Bt_reconstruirImagem.setText(_translate("MainWindow", "Reconstruir imagem "))
        self.Bt_capturarImagem.setText(_translate("MainWindow", "Capturar Imagem"))
        self.groupBox_2.setTitle(_translate("MainWindow", "TIE"))
        self.Aplic.setTabText(self.Aplic.indexOf(self.tab), _translate("MainWindow", "Reconstrução"))
        self.MedidasTens.setTitle(_translate("MainWindow", "MEDIÇÕES"))
        self.grupoStatus.setTitle(_translate("MainWindow", "STATUS DA PLACA DE AQUISIÇÕES"))
        self.pushButton.setText(_translate("MainWindow", "Salvar Leitura"))
        self.pushButton_2.setText(_translate("MainWindow", "Iniciar Aquisições"))
        self.Aplic.setTabText(self.Aplic.indexOf(self.tab_2), _translate("MainWindow", "Obter dados"))


    def setSensibilidade(self):
        self.Line_sensibilidade.setText(f"{QtWidgets.QFileDialog.getOpenFileName()[0]}")
    

    def setMeasure(self):
        self.Line_medida.setText(f"{QtWidgets.QFileDialog.getOpenFileName()[0]}")
        
    
    def setTenseRef(self):
        self.Line_tense_ref.setText(f"{QtWidgets.QFileDialog.getOpenFileName()[0]}")
    
    def saveIMG(self):
        arquivo = QtWidgets.QFileDialog.getSaveFileName()[0]
        
        if(arquivo != ""):
            cv2.imwrite(arquivo + '.png', self.imagem)
        

    
    def rebuid(self):
        width = self.Imagem_TIE.width()
        height = self.Imagem_TIE.height()

        if width <= height:
            height = width
        else:
            width = height
        
        intera  = int(self.landIntera.text()) #retorna o valor colocado de interações em landwaber

        imagem = TIE.rebuildImg(width,
                                height,
                                RouteFilejn=self.Line_sensibilidade.text(),
                                RouteFileVobj=self.Line_medida.text(),
                                RouteFileVref=self.Line_tense_ref.text(),
                                method = self.checkedMethod(),
                                intera_LDWBR = intera)
        
        
        

        self.imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2BGR)
        imagem = QtGui.QImage(imagem,width,height,imagem.strides[0],QtGui.QImage.Format_RGB888) # reformula o vetor de imagem para aparever na interface visual
        
    
        
        self.Imagem_TIE.setPixmap(QtGui.QPixmap.fromImage(imagem))

        self.Bt_capturarImagem.setEnabled(True)
    
    
    def rebuidIMG(self):
        if(self.activeRebuidImg()):
            threa = threading.Thread(target = self.rebuid)
            threa.start()

    
    def activeRebuidImg(self):

        if self.existsRouteSensebilidade():
            QMessageBox.about(self.centralwidget,"ERRO","Sem arquivo sensibilidade")
            return False

        if self.existRouteMeasure():
            QMessageBox.about(self.centralwidget,"ERRO","Sem arquivo de Medidas")
            return False
        

        if self.existRouteVref():
            QMessageBox.about(self.centralwidget,"ERRO","Sem arquivo de Tensão referência")
            return False
        
        if self.existRadioMethod():
            QMessageBox.about(self.centralwidget,"ERRO","Escolha entre um dos modelos")
            return False
        
        if self.checkInteraLandweber():
            QMessageBox.about(self.centralwidget,"ERRO","Valor de interações deve ser maior que zero")
            return False
        return True
    

    def existsRouteSensebilidade(self):
        return (self.Line_sensibilidade.text() == "")
    
    
    def existRouteMeasure(self):
        return (self.Line_medida.text() == "")


    def existRouteVref(self):
        return (self.Line_tense_ref.text() == "")
    

    def existRadioMethod(self):
        return not (self.radio_landwaber.isChecked() or self.Radio_projeo.isChecked())
    

    def checkInteraLandweber(self):
        return (self.landIntera.text() == '0')
    

    def checkedMethod(self):

        if self.radio_landwaber.isChecked():
            return "LDWBR"
        if self.Radio_projeo.isChecked():
            return "RPLIN"
        
    
    def realizaAquis(self):
        self.progressBar.setValue(0)
        self.Img_status.setPixmap(QtGui.QPixmap("Img_Eit/conectado.png"))
        threa = threading.Thread(target = self.aquisiSPI)
        threa.start()
    
    
    def saveLeituras(self):
        route = QtWidgets.QFileDialog.getSaveFileName()[0]
        
        if(route != ""):
            with open(route +'.csv', 'w') as f:
                w = csv.writer(f)
                
                w.writerow(self.listaLeituras)
                
                f.close()
            self.listaLeituras = []
            self.pushButton.setEnabled(False)
            self.progressBar.setValue(0)


        
        
    def aquisiSPI(self):
        self.pushButton_2.setEnabled(False)
        arduinoSPI = Comunica.ComunicaSPI()
        arduinoSPI.initSPI()
        
        valor = 0
        
        
        numero= 0        

        for PrimeiroEmissor in range(0,16):
            
            if(PrimeiroEmissor == 15):
                SegundoEmissor = 0
            else:
                SegundoEmissor = PrimeiroEmissor + 1
                

            if(arduinoSPI.correntePin(PrimeiroEmissor,SegundoEmissor)):
                
                time.sleep(0.1)

                for Leituras in range(1,14):
                    PrimeiroEletrodoTensao = SegundoEmissor + Leituras

                    if(PrimeiroEletrodoTensao>14):
                        PrimeiroEletrodoTensao = PrimeiroEletrodoTensao - 15
                    
                    SegundoEletrodoTensao = PrimeiroEletrodoTensao + 1

                    if(arduinoSPI.tensePin(PrimeiroEletrodoTensao,SegundoEletrodoTensao)):
                        arduinoSPI.ativaLeituras()
                        valor = arduinoSPI.Leitura()
                        self.listaLeituras.append(valor)
                        
                        numero += 1
                        progresso = int(numero*100/208)
                        self.progressBar.setValue(progresso)
                        time.sleep(0.1)

        if(len(self.listaLeituras)>=208):
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(True)
            self.Img_status.setPixmap(QtGui.QPixmap("Img_Eit/desconectado.png"))
            
            
