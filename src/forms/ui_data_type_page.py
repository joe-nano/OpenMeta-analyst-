# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_type_page.ui'
#
# Created: Thu Jun 27 10:21:34 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DataTypePage(object):
    def setupUi(self, DataTypePage):
        DataTypePage.setObjectName(_fromUtf8("DataTypePage"))
        DataTypePage.resize(450, 350)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DataTypePage.sizePolicy().hasHeightForWidth())
        DataTypePage.setSizePolicy(sizePolicy)
        DataTypePage.setMinimumSize(QtCore.QSize(450, 350))
        DataTypePage.setMaximumSize(QtCore.QSize(450, 350))
        self.verticalLayout = QtGui.QVBoxLayout(DataTypePage)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(DataTypePage)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.onearm_proportion_Button = QtGui.QToolButton(DataTypePage)
        self.onearm_proportion_Button.setMinimumSize(QtCore.QSize(90, 65))
        self.onearm_proportion_Button.setMaximumSize(QtCore.QSize(90, 65))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/new_dataset/startscreens/proportion.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.onearm_proportion_Button.setIcon(icon)
        self.onearm_proportion_Button.setIconSize(QtCore.QSize(40, 40))
        self.onearm_proportion_Button.setCheckable(True)
        self.onearm_proportion_Button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.onearm_proportion_Button.setObjectName(_fromUtf8("onearm_proportion_Button"))
        self.buttonGroup = QtGui.QButtonGroup(DataTypePage)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.onearm_proportion_Button)
        self.horizontalLayout_3.addWidget(self.onearm_proportion_Button)
        self.onearm_mean_Button = QtGui.QToolButton(DataTypePage)
        self.onearm_mean_Button.setMinimumSize(QtCore.QSize(90, 65))
        self.onearm_mean_Button.setMaximumSize(QtCore.QSize(90, 65))
        self.onearm_mean_Button.setBaseSize(QtCore.QSize(10, 10))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/new_dataset/startscreens/mean.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.onearm_mean_Button.setIcon(icon1)
        self.onearm_mean_Button.setIconSize(QtCore.QSize(40, 40))
        self.onearm_mean_Button.setCheckable(True)
        self.onearm_mean_Button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.onearm_mean_Button.setObjectName(_fromUtf8("onearm_mean_Button"))
        self.buttonGroup.addButton(self.onearm_mean_Button)
        self.horizontalLayout_3.addWidget(self.onearm_mean_Button)
        self.onearm_single_reg_coef_Button = QtGui.QToolButton(DataTypePage)
        self.onearm_single_reg_coef_Button.setMinimumSize(QtCore.QSize(120, 65))
        self.onearm_single_reg_coef_Button.setMaximumSize(QtCore.QSize(120, 65))
        self.onearm_single_reg_coef_Button.setBaseSize(QtCore.QSize(10, 10))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/new_dataset/startscreens/single_reg_coef.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.onearm_single_reg_coef_Button.setIcon(icon2)
        self.onearm_single_reg_coef_Button.setIconSize(QtCore.QSize(40, 40))
        self.onearm_single_reg_coef_Button.setCheckable(True)
        self.onearm_single_reg_coef_Button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.onearm_single_reg_coef_Button.setObjectName(_fromUtf8("onearm_single_reg_coef_Button"))
        self.buttonGroup.addButton(self.onearm_single_reg_coef_Button)
        self.horizontalLayout_3.addWidget(self.onearm_single_reg_coef_Button)
        self.onearm_generic_effect_size_Button = QtGui.QToolButton(DataTypePage)
        self.onearm_generic_effect_size_Button.setMinimumSize(QtCore.QSize(90, 65))
        self.onearm_generic_effect_size_Button.setMaximumSize(QtCore.QSize(90, 65))
        self.onearm_generic_effect_size_Button.setBaseSize(QtCore.QSize(10, 10))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/new_dataset/startscreens/gen_eff_size.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.onearm_generic_effect_size_Button.setIcon(icon3)
        self.onearm_generic_effect_size_Button.setIconSize(QtCore.QSize(40, 40))
        self.onearm_generic_effect_size_Button.setCheckable(True)
        self.onearm_generic_effect_size_Button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.onearm_generic_effect_size_Button.setArrowType(QtCore.Qt.NoArrow)
        self.onearm_generic_effect_size_Button.setObjectName(_fromUtf8("onearm_generic_effect_size_Button"))
        self.buttonGroup.addButton(self.onearm_generic_effect_size_Button)
        self.horizontalLayout_3.addWidget(self.onearm_generic_effect_size_Button)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line_2 = QtGui.QFrame(DataTypePage)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.label_4 = QtGui.QLabel(DataTypePage)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.twoarm_proportions_Button = QtGui.QToolButton(DataTypePage)
        self.twoarm_proportions_Button.setMinimumSize(QtCore.QSize(90, 65))
        self.twoarm_proportions_Button.setMaximumSize(QtCore.QSize(90, 65))
        self.twoarm_proportions_Button.setBaseSize(QtCore.QSize(10, 10))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/new_dataset/startscreens/proportions.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.twoarm_proportions_Button.setIcon(icon4)
        self.twoarm_proportions_Button.setIconSize(QtCore.QSize(72, 44))
        self.twoarm_proportions_Button.setCheckable(True)
        self.twoarm_proportions_Button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.twoarm_proportions_Button.setObjectName(_fromUtf8("twoarm_proportions_Button"))
        self.buttonGroup.addButton(self.twoarm_proportions_Button)
        self.horizontalLayout_2.addWidget(self.twoarm_proportions_Button)
        self.twoarm_means_Button = QtGui.QToolButton(DataTypePage)
        self.twoarm_means_Button.setMinimumSize(QtCore.QSize(90, 65))
        self.twoarm_means_Button.setMaximumSize(QtCore.QSize(90, 65))
        self.twoarm_means_Button.setBaseSize(QtCore.QSize(10, 10))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/new_dataset/startscreens/means.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.twoarm_means_Button.setIcon(icon5)
        self.twoarm_means_Button.setIconSize(QtCore.QSize(54, 40))
        self.twoarm_means_Button.setCheckable(True)
        self.twoarm_means_Button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.twoarm_means_Button.setObjectName(_fromUtf8("twoarm_means_Button"))
        self.buttonGroup.addButton(self.twoarm_means_Button)
        self.horizontalLayout_2.addWidget(self.twoarm_means_Button)
        self.twoarm_smds_Button = QtGui.QToolButton(DataTypePage)
        self.twoarm_smds_Button.setMinimumSize(QtCore.QSize(90, 65))
        self.twoarm_smds_Button.setMaximumSize(QtCore.QSize(90, 65))
        self.twoarm_smds_Button.setBaseSize(QtCore.QSize(10, 10))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/new_dataset/startscreens/smd.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.twoarm_smds_Button.setIcon(icon6)
        self.twoarm_smds_Button.setIconSize(QtCore.QSize(40, 40))
        self.twoarm_smds_Button.setCheckable(True)
        self.twoarm_smds_Button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.twoarm_smds_Button.setObjectName(_fromUtf8("twoarm_smds_Button"))
        self.buttonGroup.addButton(self.twoarm_smds_Button)
        self.horizontalLayout_2.addWidget(self.twoarm_smds_Button)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line_4 = QtGui.QFrame(DataTypePage)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout.addWidget(self.line_4)
        self.label_5 = QtGui.QLabel(DataTypePage)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.diagnostic_Button = QtGui.QToolButton(DataTypePage)
        self.diagnostic_Button.setMinimumSize(QtCore.QSize(90, 65))
        self.diagnostic_Button.setMaximumSize(QtCore.QSize(90, 65))
        self.diagnostic_Button.setBaseSize(QtCore.QSize(10, 10))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/new_dataset/startscreens/diagnostic.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.diagnostic_Button.setIcon(icon7)
        self.diagnostic_Button.setIconSize(QtCore.QSize(85, 44))
        self.diagnostic_Button.setCheckable(True)
        self.diagnostic_Button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.diagnostic_Button.setObjectName(_fromUtf8("diagnostic_Button"))
        self.buttonGroup.addButton(self.diagnostic_Button)
        self.horizontalLayout.addWidget(self.diagnostic_Button)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DataTypePage)
        QtCore.QMetaObject.connectSlotsByName(DataTypePage)

    def retranslateUi(self, DataTypePage):
        DataTypePage.setWindowTitle(_translate("DataTypePage", "WizardPage", None))
        DataTypePage.setTitle(_translate("DataTypePage", "What type of data do you have?", None))
        self.label_2.setText(_translate("DataTypePage", "One piece of data from each study or studies with one group", None))
        self.onearm_proportion_Button.setText(_translate("DataTypePage", "proportion", None))
        self.onearm_mean_Button.setText(_translate("DataTypePage", "mean", None))
        self.onearm_single_reg_coef_Button.setText(_translate("DataTypePage", "regression coefficient", None))
        self.onearm_generic_effect_size_Button.setText(_translate("DataTypePage", "generic\n"
"effect size", None))
        self.label_4.setText(_translate("DataTypePage", "Data on two or more groups per study", None))
        self.twoarm_proportions_Button.setText(_translate("DataTypePage", "proportions", None))
        self.twoarm_means_Button.setText(_translate("DataTypePage", "means", None))
        self.twoarm_smds_Button.setText(_translate("DataTypePage", "SMD", None))
        self.label_5.setText(_translate("DataTypePage", "Data on test performance", None))
        self.diagnostic_Button.setText(_translate("DataTypePage", "diagnostic", None))

import icons_rc
