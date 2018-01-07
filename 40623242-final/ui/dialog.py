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

        self.pointButton.clicked.connect(self.pointclicked)
        self.squareRootButton.clicked.connect(self.squareRoot)
        self.plusminusButton.clicked.connect(self.changesign)
        self.clearMemoryButton.clicked.connect(self.clearMemory)
        self.readMemoryButton.clicked.connect(self.readMemory)
        self.setMemoryButton.clicked.connect(self.setMemory)
        self.addToMemoryButton.clicked.connect(self.addToMemory)
        self.lessToMemoryButton.clicked.connect(self.lessToMemory)
        self.clearButton.clicked.connect(self.clear)
        self.clearAllButton.clicked.connect(self.clearAll)
        self.equalButton.clicked.connect(self.equalClicked)
        self.pendingadditiveoperator = ''
        for i in number :
            i.clicked.connect(self.digitclicked)
            self.waiting = True
        self.sum = 0.0
        plus_minus = [self.plusButton, self.minusButton]
        
        for i in plus_minus:
            i.clicked.connect(self.additiveoperator)
        multiply_divide = [self.timesButton, self.divisionButton]
        
        for i in multiply_divide:
            i.clicked.connect(self.multiplicativeoperator)
        self.pendingmultiplicativeoperator = ''
        self.factor = 0.0
        
    def equalClicked(self):
        operand = float(self.display.text())
        if self.pendingmultiplicativeoperator:
            if not self.calculate(operand, self.pendingmultiplicativeoperator):
                self.abortOperation()
                return
            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''
        if self.pendingadditiveoperator:
            if not self.calculate(operand, self.pendingadditiveoperator):
                self.abortOperation()
                return
            self.pendingadditiveoperator = ''
        else:
            self.sum = operand
        self.display.setText(str(self.sum))
        self.sum = 0.0
        self.waiting = True

    def digitclicked(self):
        button = self.sender()
        Value = int(button.text())
        if self.display.text() == '0' and Value == 0:
            return
        if self.waiting :
            self.display.clear()
            self.waiting = False
        self.display.setText(self.display.text()+str(Value))
        

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
    
    def pointclicked(self):
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
        operand = float(self.display.text())
        if clickedoperator == "sqrt":
            if operand < 0.0:
                self.abortoperation()
                return
            result = math.sqrt(operand)
        self.display.setText(str(result))
        self.waiting = True
            

    def clearMemory(self):
        self.sumInmemory = 0.0
        self.display.setText(str(self.cumInMemory))
            
    def readMemory(self):
        self.display.setText(str(self.cumInMemory))
        self.waiting = True
            
    def setMemory(self):
        self.equal()
        self.sumInMemory = float(self.display.text())
            
    def addToMemory(self):
        self.equal()
        self.wumInMemory += float(self.display.text())
            
    def lessToMemory(self):
        self.equal()
        self.sumInMemory -= float(self.display.text())
