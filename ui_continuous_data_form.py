# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'continuous_data_form.ui'
#
# Created: Tue Jun 08 13:06:15 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ContinuousDataForm(object):
    def setupUi(self, ContinuousDataForm):
        ContinuousDataForm.setObjectName("ContinuousDataForm")
        ContinuousDataForm.resize(670, 418)
        ContinuousDataForm.setMinimumSize(QtCore.QSize(670, 0))
        ContinuousDataForm.setMaximumSize(QtCore.QSize(670, 452))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        ContinuousDataForm.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/meta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ContinuousDataForm.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(ContinuousDataForm)
        self.buttonBox.setGeometry(QtCore.QRect(470, 380, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.grp_box_pre_post = QtGui.QGroupBox(ContinuousDataForm)
        self.grp_box_pre_post.setGeometry(QtCore.QRect(20, 110, 631, 261))
        self.grp_box_pre_post.setObjectName("grp_box_pre_post")
        self.grp_1_lbl = QtGui.QLabel(self.grp_box_pre_post)
        self.grp_1_lbl.setGeometry(QtCore.QRect(10, 60, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.grp_1_lbl.setFont(font)
        self.grp_1_lbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grp_1_lbl.setObjectName("grp_1_lbl")
        self.grp_2_lbl = QtGui.QLabel(self.grp_box_pre_post)
        self.grp_2_lbl.setGeometry(QtCore.QRect(10, 160, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.grp_2_lbl.setFont(font)
        self.grp_2_lbl.setObjectName("grp_2_lbl")
        self.g1_pre_post_table = QtGui.QTableWidget(self.grp_box_pre_post)
        self.g1_pre_post_table.setGeometry(QtCore.QRect(70, 21, 550, 81))
        self.g1_pre_post_table.setMinimumSize(QtCore.QSize(550, 0))
        self.g1_pre_post_table.setMaximumSize(QtCore.QSize(550, 16777215))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.g1_pre_post_table.setFont(font)
        self.g1_pre_post_table.setFrameShape(QtGui.QFrame.NoFrame)
        self.g1_pre_post_table.setFrameShadow(QtGui.QFrame.Plain)
        self.g1_pre_post_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.g1_pre_post_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.g1_pre_post_table.setAlternatingRowColors(True)
        self.g1_pre_post_table.setShowGrid(True)
        self.g1_pre_post_table.setGridStyle(QtCore.Qt.DashLine)
        self.g1_pre_post_table.setRowCount(2)
        self.g1_pre_post_table.setColumnCount(8)
        self.g1_pre_post_table.setObjectName("g1_pre_post_table")
        self.g1_pre_post_table.setColumnCount(8)
        self.g1_pre_post_table.setRowCount(2)
        item = QtGui.QTableWidgetItem()
        self.g1_pre_post_table.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.g1_pre_post_table.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.g1_pre_post_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.g1_pre_post_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.g1_pre_post_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.g1_pre_post_table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.g1_pre_post_table.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.g1_pre_post_table.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.g1_pre_post_table.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.g1_pre_post_table.setHorizontalHeaderItem(7, item)
        self.g2_pre_post_table = QtGui.QTableWidget(self.grp_box_pre_post)
        self.g2_pre_post_table.setGeometry(QtCore.QRect(70, 120, 550, 81))
        self.g2_pre_post_table.setMinimumSize(QtCore.QSize(550, 0))
        self.g2_pre_post_table.setMaximumSize(QtCore.QSize(550, 16777215))
        self.g2_pre_post_table.setFrameShape(QtGui.QFrame.NoFrame)
        self.g2_pre_post_table.setFrameShadow(QtGui.QFrame.Plain)
        self.g2_pre_post_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.g2_pre_post_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.g2_pre_post_table.setAlternatingRowColors(True)
        self.g2_pre_post_table.setGridStyle(QtCore.Qt.DashLine)
        self.g2_pre_post_table.setRowCount(2)
        self.g2_pre_post_table.setColumnCount(8)
        self.g2_pre_post_table.setObjectName("g2_pre_post_table")
        self.g2_pre_post_table.setColumnCount(8)
        self.g2_pre_post_table.setRowCount(2)
        item = QtGui.QTableWidgetItem()
        self.g2_pre_post_table.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.g2_pre_post_table.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.g2_pre_post_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.g2_pre_post_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.g2_pre_post_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.g2_pre_post_table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.g2_pre_post_table.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.g2_pre_post_table.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.g2_pre_post_table.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.g2_pre_post_table.setHorizontalHeaderItem(7, item)
        self.label = QtGui.QLabel(self.grp_box_pre_post)
        self.label.setGeometry(QtCore.QRect(10, 230, 71, 16))
        self.label.setObjectName("label")
        self.correlation_edit = QtGui.QLineEdit(self.grp_box_pre_post)
        self.correlation_edit.setGeometry(QtCore.QRect(80, 230, 41, 16))
        self.correlation_edit.setObjectName("correlation_edit")
        self.simple_table = QtGui.QTableWidget(ContinuousDataForm)
        self.simple_table.setGeometry(QtCore.QRect(60, 10, 550, 80))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.simple_table.sizePolicy().hasHeightForWidth())
        self.simple_table.setSizePolicy(sizePolicy)
        self.simple_table.setMinimumSize(QtCore.QSize(550, 80))
        self.simple_table.setMaximumSize(QtCore.QSize(550, 80))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.simple_table.setFont(font)
        self.simple_table.setFrameShape(QtGui.QFrame.NoFrame)
        self.simple_table.setFrameShadow(QtGui.QFrame.Plain)
        self.simple_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.simple_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.simple_table.setAlternatingRowColors(True)
        self.simple_table.setGridStyle(QtCore.Qt.DashLine)
        self.simple_table.setRowCount(2)
        self.simple_table.setColumnCount(8)
        self.simple_table.setObjectName("simple_table")
        self.simple_table.setColumnCount(8)
        self.simple_table.setRowCount(2)
        item = QtGui.QTableWidgetItem()
        self.simple_table.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.simple_table.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.simple_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.simple_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.simple_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.simple_table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.simple_table.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.simple_table.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.simple_table.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.simple_table.setHorizontalHeaderItem(7, item)
        self.label_2 = QtGui.QLabel(ContinuousDataForm)
        self.label_2.setGeometry(QtCore.QRect(20, 390, 16, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.alpha_edit = QtGui.QLineEdit(ContinuousDataForm)
        self.alpha_edit.setGeometry(QtCore.QRect(40, 390, 31, 16))
        self.alpha_edit.setObjectName("alpha_edit")
        self.ci_label = QtGui.QLabel(ContinuousDataForm)
        self.ci_label.setGeometry(QtCore.QRect(80, 390, 251, 16))
        self.ci_label.setObjectName("ci_label")

        self.retranslateUi(ContinuousDataForm)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ContinuousDataForm.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ContinuousDataForm.reject)
        QtCore.QMetaObject.connectSlotsByName(ContinuousDataForm)

    def retranslateUi(self, ContinuousDataForm):
        ContinuousDataForm.setWindowTitle(QtGui.QApplication.translate("ContinuousDataForm", "Continuous Data", None, QtGui.QApplication.UnicodeUTF8))
        self.grp_box_pre_post.setTitle(QtGui.QApplication.translate("ContinuousDataForm", "pre / post", None, QtGui.QApplication.UnicodeUTF8))
        self.grp_1_lbl.setText(QtGui.QApplication.translate("ContinuousDataForm", "group 1", None, QtGui.QApplication.UnicodeUTF8))
        self.grp_2_lbl.setText(QtGui.QApplication.translate("ContinuousDataForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Verdana\'; font-size:8pt; font-weight:600; font-style:italic;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt;\">group 2</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.g1_pre_post_table.verticalHeaderItem(0).setText(QtGui.QApplication.translate("ContinuousDataForm", "pre", None, QtGui.QApplication.UnicodeUTF8))
        self.g1_pre_post_table.verticalHeaderItem(1).setText(QtGui.QApplication.translate("ContinuousDataForm", "post", None, QtGui.QApplication.UnicodeUTF8))
        self.g1_pre_post_table.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("ContinuousDataForm", "n", None, QtGui.QApplication.UnicodeUTF8))
        self.g1_pre_post_table.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("ContinuousDataForm", "mean", None, QtGui.QApplication.UnicodeUTF8))
        self.g1_pre_post_table.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("ContinuousDataForm", "sd", None, QtGui.QApplication.UnicodeUTF8))
        self.g1_pre_post_table.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("ContinuousDataForm", "se", None, QtGui.QApplication.UnicodeUTF8))
        self.g1_pre_post_table.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("ContinuousDataForm", "var", None, QtGui.QApplication.UnicodeUTF8))
        self.g1_pre_post_table.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("ContinuousDataForm", "pval", None, QtGui.QApplication.UnicodeUTF8))
        self.g1_pre_post_table.horizontalHeaderItem(6).setText(QtGui.QApplication.translate("ContinuousDataForm", "low", None, QtGui.QApplication.UnicodeUTF8))
        self.g1_pre_post_table.horizontalHeaderItem(7).setText(QtGui.QApplication.translate("ContinuousDataForm", "high", None, QtGui.QApplication.UnicodeUTF8))
        self.g2_pre_post_table.verticalHeaderItem(0).setText(QtGui.QApplication.translate("ContinuousDataForm", "pre", None, QtGui.QApplication.UnicodeUTF8))
        self.g2_pre_post_table.verticalHeaderItem(1).setText(QtGui.QApplication.translate("ContinuousDataForm", "post", None, QtGui.QApplication.UnicodeUTF8))
        self.g2_pre_post_table.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("ContinuousDataForm", "n", None, QtGui.QApplication.UnicodeUTF8))
        self.g2_pre_post_table.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("ContinuousDataForm", "mean", None, QtGui.QApplication.UnicodeUTF8))
        self.g2_pre_post_table.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("ContinuousDataForm", "sd", None, QtGui.QApplication.UnicodeUTF8))
        self.g2_pre_post_table.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("ContinuousDataForm", "se", None, QtGui.QApplication.UnicodeUTF8))
        self.g2_pre_post_table.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("ContinuousDataForm", "var", None, QtGui.QApplication.UnicodeUTF8))
        self.g2_pre_post_table.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("ContinuousDataForm", "pval", None, QtGui.QApplication.UnicodeUTF8))
        self.g2_pre_post_table.horizontalHeaderItem(6).setText(QtGui.QApplication.translate("ContinuousDataForm", "low", None, QtGui.QApplication.UnicodeUTF8))
        self.g2_pre_post_table.horizontalHeaderItem(7).setText(QtGui.QApplication.translate("ContinuousDataForm", "high", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ContinuousDataForm", "correlation:", None, QtGui.QApplication.UnicodeUTF8))
        self.correlation_edit.setText(QtGui.QApplication.translate("ContinuousDataForm", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.simple_table.verticalHeaderItem(0).setText(QtGui.QApplication.translate("ContinuousDataForm", "group 1", None, QtGui.QApplication.UnicodeUTF8))
        self.simple_table.verticalHeaderItem(1).setText(QtGui.QApplication.translate("ContinuousDataForm", "group 2", None, QtGui.QApplication.UnicodeUTF8))
        self.simple_table.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("ContinuousDataForm", "n", None, QtGui.QApplication.UnicodeUTF8))
        self.simple_table.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("ContinuousDataForm", "mean", None, QtGui.QApplication.UnicodeUTF8))
        self.simple_table.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("ContinuousDataForm", "sd", None, QtGui.QApplication.UnicodeUTF8))
        self.simple_table.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("ContinuousDataForm", "se", None, QtGui.QApplication.UnicodeUTF8))
        self.simple_table.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("ContinuousDataForm", "var", None, QtGui.QApplication.UnicodeUTF8))
        self.simple_table.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("ContinuousDataForm", "pval", None, QtGui.QApplication.UnicodeUTF8))
        self.simple_table.horizontalHeaderItem(6).setText(QtGui.QApplication.translate("ContinuousDataForm", "low", None, QtGui.QApplication.UnicodeUTF8))
        self.simple_table.horizontalHeaderItem(7).setText(QtGui.QApplication.translate("ContinuousDataForm", "high", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ContinuousDataForm", "α:", None, QtGui.QApplication.UnicodeUTF8))
        self.alpha_edit.setText(QtGui.QApplication.translate("ContinuousDataForm", ".05", None, QtGui.QApplication.UnicodeUTF8))
        self.ci_label.setText(QtGui.QApplication.translate("ContinuousDataForm", "(95% confidence interval)", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc