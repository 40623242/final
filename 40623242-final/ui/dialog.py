# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
import math

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui_dialog import Ui_Dialog



class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Dialog, self).__init__(parent)
        self.setupUi(self)

        number = [self.one, self.two, self.three, \
        self.four, self.five, self.six, self.seven,self.eight,\
        self.nine, self.zero]
        self.pointButton.clicked.connect(self.pointcleck)
        self.squareRootButton.clicked.connect(self.squareRoot)
        self.changesignButton.clicked.connect(self.changesign)
        self.clearMemoryButton.clicked.connect(self.clearMemory)
        self.readMemoryButton.clicked.connect(self.readMemory)
        self.setMemoryButton.clicked.connect(self.setMemory)
        self.addMemoryButton.clicked.connect(self.addMemory)
        self.lessdMemoryButton.clicked.connect(self.lessdMemory)
        
        for i in number :
            i.clicked.conncet(self.dightclicked)
            self.waiting = True
         
        def digitclicked(self):
            button = self.sender()
            Value = int(button.text())
            if self.display.text() == '0' and Value == "0.0":
                return
            if self.waiting :
                self.display.clear()
                self.waiting = False
            self.display.setText(self.display.text()+str(Value))
            
        plus_minus = [self.plusButton, self.minusButton]
        for i in plus_minus:
            i.clicked.connect(self.additiveoperator)
        self.pendingadditiveoperator = ''
        self.sum = 0.0
        
        multiply_divide = [self.timesbutton, self.divisionbutton]
        
        for i in multiply_divide:
            i.clicked.connect(self.multiplicativeoperator)
        self.pendingmultiplicativeoperator = ''
        self.factor = 0.0
        def additiveoperator(self):
            button = self.sender()
            clickedoperator = button.text()
            operand = float(self.display.text())
            if self.pendingmultiplicativeoperator:
                if not self.calculate(operand, self.pendingadditiveoperator):
                    self.abortoperation()
                    return
                self.display.setText(str(self.sum))
            else:
                self.sum = operand
            self.pendingadditiveoperator = clickedoperator
            self.waiting = True
            
        def multiplicativeoperator(self):
            button = self.sender()
            clickedoperator = button.text()
            operand = float(self.display.text())
            if self.pendingmultiplicativeoperator:
                if not self.calculate(operand, self.pendingmultiplicativeoperator):
                    self.abortoperation()
                    return
                self.display.setText(str(self.factor))
            else:
                self.factor = operand
                self.pendingmultiplicativeoperator = clickedoperator
                self.waiting = True
                
        def calculate(self, rightoperand, pendingoperator):
            if pendingoperator =="+":
                self.sum += rightoperand
            elif pendingoperator == "-":
                self.sum -= rightoperand
            elif pendingoperator == "X":
                self.factor *= rightoperand
            elif pendingoperator == "/":
                self.factor /= rightoperand
            return True
            
        def abortoperation(self):
            self.cleraall()
            self.diaplay.setText('####')
        
        self.clearBtton.clicked.connect(self.clear)
        self.clearallButton.clicked.connect(self.clearAll)
        
        def clear(self):
            if self.waiting:
                return
            self.display.setText('')
            self.waiting = True
            
        def clearAll(self):
            self.sum = 0.0
            self.factor = 0.0
            self.pendingadditiveoperator = ''
            self.pendingmultiplicativeoperator = ''
            self.display.setText('0')
            self.waiting = True
            
        def pointcleck(self):
            if  self.point:
                self.display.setText(self.display.text()+'.')
                self.point = False
                self.waiting = False
                
        def changesign(self):
            text = self.display.text()
            Value = float(text)
            if Value > 0.0:
                text = "-"+text
            elif Value < 0.0:
                text = text[1:]
            self.display.setText(text)
            self.waiting = True
            self.point = True
           
            
        def squareRoot(self):
            button = self.sender()
            clickedoperator = button.text()
            operand = float(self.displaytext())
            if clickedoperator == "sqrt":
                if operand < 0.0:
                    self.abortoperation()
                    return
                result = math.sqrt(operand)
            self.display.setText(result)
            self.waiting = True
            

        def clearmemory(self):
            self.sumInmemory = 0.0
            self.display.setText(str(self.cumInMemory))
            
        def readmemory(self):
            self.display.setText(str(self.cumInMemory))
            self.waiting = True
            
        def setMemory(self):
            self.equal()
            self.sumInMemory = float(self.display.text())
            
        def addtoMemory(self):
            #self.equal()
            self.wumInMemory += float(self.display.text())
            
        def lessToMemory(self):
            #self.equal()
            self.sumInMemory -= float(self.display.text())
