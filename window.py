# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mapped.ui'
#
# Created: Sun Jun  9 17:11:17 2013
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(776, 769)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.mapTab = QtGui.QWidget()
        self.mapTab.setObjectName(_fromUtf8("mapTab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.mapTab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.map = QtGui.QGraphicsView(self.mapTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.map.sizePolicy().hasHeightForWidth())
        self.map.setSizePolicy(sizePolicy)
        self.map.setObjectName(_fromUtf8("map"))
        self.gridLayout_2.addWidget(self.map, 0, 0, 1, 1)
        self.palette = QtGui.QGraphicsView(self.mapTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.palette.sizePolicy().hasHeightForWidth())
        self.palette.setSizePolicy(sizePolicy)
        self.palette.setMinimumSize(QtCore.QSize(160, 0))
        self.palette.setMaximumSize(QtCore.QSize(200, 16777215))
        self.palette.setObjectName(_fromUtf8("palette"))
        self.gridLayout_2.addWidget(self.palette, 0, 1, 1, 1)
        self.tabWidget.addTab(self.mapTab, _fromUtf8(""))
        self.movPermissionsTab = QtGui.QWidget()
        self.movPermissionsTab.setObjectName(_fromUtf8("movPermissionsTab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.movPermissionsTab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.movPermissionsMap = QtGui.QGraphicsView(self.movPermissionsTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.movPermissionsMap.sizePolicy().hasHeightForWidth())
        self.movPermissionsMap.setSizePolicy(sizePolicy)
        self.movPermissionsMap.setObjectName(_fromUtf8("movPermissionsMap"))
        self.gridLayout_3.addWidget(self.movPermissionsMap, 0, 0, 1, 1)
        self.MovPermissionsPalette = QtGui.QGraphicsView(self.movPermissionsTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MovPermissionsPalette.sizePolicy().hasHeightForWidth())
        self.MovPermissionsPalette.setSizePolicy(sizePolicy)
        self.MovPermissionsPalette.setMinimumSize(QtCore.QSize(160, 0))
        self.MovPermissionsPalette.setMaximumSize(QtCore.QSize(200, 16777215))
        self.MovPermissionsPalette.setObjectName(_fromUtf8("MovPermissionsPalette"))
        self.gridLayout_3.addWidget(self.MovPermissionsPalette, 0, 1, 1, 1)
        self.tabWidget.addTab(self.movPermissionsTab, _fromUtf8(""))
        self.EventsTab = QtGui.QWidget()
        self.EventsTab.setObjectName(_fromUtf8("EventsTab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.EventsTab)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.eventMap = QtGui.QGraphicsView(self.EventsTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eventMap.sizePolicy().hasHeightForWidth())
        self.eventMap.setSizePolicy(sizePolicy)
        self.eventMap.setObjectName(_fromUtf8("eventMap"))
        self.gridLayout_4.addWidget(self.eventMap, 0, 0, 1, 1)
        self.EventsBox = QtGui.QGroupBox(self.EventsTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EventsBox.sizePolicy().hasHeightForWidth())
        self.EventsBox.setSizePolicy(sizePolicy)
        self.EventsBox.setObjectName(_fromUtf8("EventsBox"))
        self.gridLayout_5 = QtGui.QGridLayout(self.EventsBox)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_2 = QtGui.QLabel(self.EventsBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_5.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.EventsBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_5.addWidget(self.label_5, 4, 1, 1, 1)
        self.label = QtGui.QLabel(self.EventsBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_5.addWidget(self.label, 0, 1, 1, 1)
        self.addTriggerButton = QtGui.QPushButton(self.EventsBox)
        self.addTriggerButton.setEnabled(False)
        self.addTriggerButton.setMaximumSize(QtCore.QSize(27, 16777215))
        self.addTriggerButton.setObjectName(_fromUtf8("addTriggerButton"))
        self.gridLayout_5.addWidget(self.addTriggerButton, 4, 4, 1, 1)
        self.addSignpostButton = QtGui.QPushButton(self.EventsBox)
        self.addSignpostButton.setEnabled(False)
        self.addSignpostButton.setMaximumSize(QtCore.QSize(27, 16777215))
        self.addSignpostButton.setObjectName(_fromUtf8("addSignpostButton"))
        self.gridLayout_5.addWidget(self.addSignpostButton, 5, 4, 1, 1)
        self.label_4 = QtGui.QLabel(self.EventsBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_5.addWidget(self.label_4, 2, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.EventsBox)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_5.addWidget(self.label_8, 5, 2, 1, 1)
        self.addPersonButton = QtGui.QPushButton(self.EventsBox)
        self.addPersonButton.setEnabled(False)
        self.addPersonButton.setMaximumSize(QtCore.QSize(27, 16777215))
        self.addPersonButton.setObjectName(_fromUtf8("addPersonButton"))
        self.gridLayout_5.addWidget(self.addPersonButton, 2, 4, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.EventsBox)
        self.groupBox.setEnabled(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_5.addWidget(self.groupBox, 6, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 0, 3, 1, 1)
        self.label_6 = QtGui.QLabel(self.EventsBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_5.addWidget(self.label_6, 4, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.EventsBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_5.addWidget(self.label_7, 5, 1, 1, 1)
        self.addWarpButton = QtGui.QPushButton(self.EventsBox)
        self.addWarpButton.setEnabled(False)
        self.addWarpButton.setMaximumSize(QtCore.QSize(27, 16777215))
        self.addWarpButton.setObjectName(_fromUtf8("addWarpButton"))
        self.gridLayout_5.addWidget(self.addWarpButton, 0, 4, 1, 1)
        self.label_3 = QtGui.QLabel(self.EventsBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_5.addWidget(self.label_3, 2, 2, 1, 1)
        self.eventsStackedWidget = QtGui.QStackedWidget(self.EventsBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eventsStackedWidget.sizePolicy().hasHeightForWidth())
        self.eventsStackedWidget.setSizePolicy(sizePolicy)
        self.eventsStackedWidget.setObjectName(_fromUtf8("eventsStackedWidget"))
        self.emptyEditor = QtGui.QWidget()
        self.emptyEditor.setObjectName(_fromUtf8("emptyEditor"))
        self.eventsStackedWidget.addWidget(self.emptyEditor)
        self.warpEditor = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.warpEditor.sizePolicy().hasHeightForWidth())
        self.warpEditor.setSizePolicy(sizePolicy)
        self.warpEditor.setObjectName(_fromUtf8("warpEditor"))
        self.formLayout_2 = QtGui.QFormLayout(self.warpEditor)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_10 = QtGui.QLabel(self.warpEditor)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_3 = QtGui.QLineEdit(self.warpEditor)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_9 = QtGui.QLabel(self.warpEditor)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_9)
        self.lineEdit = QtGui.QLineEdit(self.warpEditor)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.label_11 = QtGui.QLabel(self.warpEditor)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_11)
        self.lineEdit_2 = QtGui.QLineEdit(self.warpEditor)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_12 = QtGui.QLabel(self.warpEditor)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_12)
        self.label_13 = QtGui.QLabel(self.warpEditor)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_13)
        self.lineEdit_4 = QtGui.QLineEdit(self.warpEditor)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit_4)
        self.lineEdit_5 = QtGui.QLineEdit(self.warpEditor)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineEdit_5)
        self.lineEdit_6 = QtGui.QLineEdit(self.warpEditor)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_14 = QtGui.QLabel(self.warpEditor)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_14)
        self.eventsStackedWidget.addWidget(self.warpEditor)
        self.personEditor = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.personEditor.sizePolicy().hasHeightForWidth())
        self.personEditor.setSizePolicy(sizePolicy)
        self.personEditor.setObjectName(_fromUtf8("personEditor"))
        self.formLayout = QtGui.QFormLayout(self.personEditor)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_16 = QtGui.QLabel(self.personEditor)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_16)
        self.person_num = QtGui.QLineEdit(self.personEditor)
        self.person_num.setMaxLength(2)
        self.person_num.setObjectName(_fromUtf8("person_num"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.person_num)
        self.label_17 = QtGui.QLabel(self.personEditor)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_17)
        self.sprite_num = QtGui.QLineEdit(self.personEditor)
        self.sprite_num.setMaxLength(2)
        self.sprite_num.setObjectName(_fromUtf8("sprite_num"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.sprite_num)
        self.label_18 = QtGui.QLabel(self.personEditor)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_18)
        self._3 = QtGui.QHBoxLayout()
        self._3.setObjectName(_fromUtf8("_3"))
        self.p_uknown1 = QtGui.QLineEdit(self.personEditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p_uknown1.sizePolicy().hasHeightForWidth())
        self.p_uknown1.setSizePolicy(sizePolicy)
        self.p_uknown1.setMaximumSize(QtCore.QSize(40, 16777215))
        self.p_uknown1.setMaxLength(2)
        self.p_uknown1.setObjectName(_fromUtf8("p_uknown1"))
        self._3.addWidget(self.p_uknown1)
        self.p_uknown2 = QtGui.QLineEdit(self.personEditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p_uknown2.sizePolicy().hasHeightForWidth())
        self.p_uknown2.setSizePolicy(sizePolicy)
        self.p_uknown2.setMaximumSize(QtCore.QSize(40, 16777215))
        self.p_uknown2.setMaxLength(2)
        self.p_uknown2.setObjectName(_fromUtf8("p_uknown2"))
        self._3.addWidget(self.p_uknown2)
        self.formLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self._3)
        self.label_15 = QtGui.QLabel(self.personEditor)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_15)
        self._2 = QtGui.QHBoxLayout()
        self._2.setObjectName(_fromUtf8("_2"))
        self.p_x = QtGui.QLineEdit(self.personEditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p_x.sizePolicy().hasHeightForWidth())
        self.p_x.setSizePolicy(sizePolicy)
        self.p_x.setMaximumSize(QtCore.QSize(40, 16777215))
        self.p_x.setMaxLength(2)
        self.p_x.setObjectName(_fromUtf8("p_x"))
        self._2.addWidget(self.p_x)
        self.p_y = QtGui.QLineEdit(self.personEditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p_y.sizePolicy().hasHeightForWidth())
        self.p_y.setSizePolicy(sizePolicy)
        self.p_y.setMaximumSize(QtCore.QSize(40, 16777215))
        self.p_y.setMaxLength(2)
        self.p_y.setObjectName(_fromUtf8("p_y"))
        self._2.addWidget(self.p_y)
        self.formLayout.setLayout(4, QtGui.QFormLayout.FieldRole, self._2)
        self.label_19 = QtGui.QLabel(self.personEditor)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_19)
        self.p_uknown3 = QtGui.QLineEdit(self.personEditor)
        self.p_uknown3.setMaxLength(2)
        self.p_uknown3.setObjectName(_fromUtf8("p_uknown3"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.p_uknown3)
        self.label_20 = QtGui.QLabel(self.personEditor)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_20)
        self.comboBox = QtGui.QComboBox(self.personEditor)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.comboBox)
        self.label_21 = QtGui.QLabel(self.personEditor)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_21)
        self.p_mov = QtGui.QLineEdit(self.personEditor)
        self.p_mov.setMaxLength(2)
        self.p_mov.setObjectName(_fromUtf8("p_mov"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.p_mov)
        self.label_22 = QtGui.QLabel(self.personEditor)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_22)
        self.p_uknown4 = QtGui.QLineEdit(self.personEditor)
        self.p_uknown4.setMaxLength(2)
        self.p_uknown4.setObjectName(_fromUtf8("p_uknown4"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.p_uknown4)
        self.label_23 = QtGui.QLabel(self.personEditor)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.LabelRole, self.label_23)
        self.p_is_a_trainer = QtGui.QCheckBox(self.personEditor)
        self.p_is_a_trainer.setText(_fromUtf8(""))
        self.p_is_a_trainer.setObjectName(_fromUtf8("p_is_a_trainer"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.FieldRole, self.p_is_a_trainer)
        self.label_24 = QtGui.QLabel(self.personEditor)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.LabelRole, self.label_24)
        self.label_25 = QtGui.QLabel(self.personEditor)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.formLayout.setWidget(12, QtGui.QFormLayout.LabelRole, self.label_25)
        self.label_26 = QtGui.QLabel(self.personEditor)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.formLayout.setWidget(13, QtGui.QFormLayout.LabelRole, self.label_26)
        self.label_27 = QtGui.QLabel(self.personEditor)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.formLayout.setWidget(14, QtGui.QFormLayout.LabelRole, self.label_27)
        self.p_flag = QtGui.QLineEdit(self.personEditor)
        self.p_flag.setMaxLength(4)
        self.p_flag.setObjectName(_fromUtf8("p_flag"))
        self.formLayout.setWidget(14, QtGui.QFormLayout.FieldRole, self.p_flag)
        self.label_28 = QtGui.QLabel(self.personEditor)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.formLayout.setWidget(15, QtGui.QFormLayout.LabelRole, self.label_28)
        self._6 = QtGui.QHBoxLayout()
        self._6.setObjectName(_fromUtf8("_6"))
        self.p_unknown6 = QtGui.QLineEdit(self.personEditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p_unknown6.sizePolicy().hasHeightForWidth())
        self.p_unknown6.setSizePolicy(sizePolicy)
        self.p_unknown6.setMaximumSize(QtCore.QSize(40, 16777215))
        self.p_unknown6.setMaxLength(2)
        self.p_unknown6.setObjectName(_fromUtf8("p_unknown6"))
        self._6.addWidget(self.p_unknown6)
        self.p_unknown7 = QtGui.QLineEdit(self.personEditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p_unknown7.sizePolicy().hasHeightForWidth())
        self.p_unknown7.setSizePolicy(sizePolicy)
        self.p_unknown7.setMaximumSize(QtCore.QSize(40, 16777215))
        self.p_unknown7.setMaxLength(2)
        self.p_unknown7.setObjectName(_fromUtf8("p_unknown7"))
        self._6.addWidget(self.p_unknown7)
        self.formLayout.setLayout(15, QtGui.QFormLayout.FieldRole, self._6)
        self.p_script_offset = QtGui.QLineEdit(self.personEditor)
        self.p_script_offset.setMaxLength(6)
        self.p_script_offset.setObjectName(_fromUtf8("p_script_offset"))
        self.formLayout.setWidget(13, QtGui.QFormLayout.FieldRole, self.p_script_offset)
        self.p_view_radius = QtGui.QLineEdit(self.personEditor)
        self.p_view_radius.setMaxLength(4)
        self.p_view_radius.setObjectName(_fromUtf8("p_view_radius"))
        self.formLayout.setWidget(12, QtGui.QFormLayout.FieldRole, self.p_view_radius)
        self.p_uknown5 = QtGui.QLineEdit(self.personEditor)
        self.p_uknown5.setMaxLength(2)
        self.p_uknown5.setObjectName(_fromUtf8("p_uknown5"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.FieldRole, self.p_uknown5)
        self.eventsStackedWidget.addWidget(self.personEditor)
        self.triggerEditor = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.triggerEditor.sizePolicy().hasHeightForWidth())
        self.triggerEditor.setSizePolicy(sizePolicy)
        self.triggerEditor.setObjectName(_fromUtf8("triggerEditor"))
        self.formLayout_3 = QtGui.QFormLayout(self.triggerEditor)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.lineEdit_8 = QtGui.QLineEdit(self.triggerEditor)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.lineEdit_8)
        self.label_49 = QtGui.QLabel(self.triggerEditor)
        self.label_49.setObjectName(_fromUtf8("label_49"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_49)
        self.eventsStackedWidget.addWidget(self.triggerEditor)
        self.signpostEditor = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signpostEditor.sizePolicy().hasHeightForWidth())
        self.signpostEditor.setSizePolicy(sizePolicy)
        self.signpostEditor.setObjectName(_fromUtf8("signpostEditor"))
        self.formLayout_4 = QtGui.QFormLayout(self.signpostEditor)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.lineEdit_9 = QtGui.QLineEdit(self.signpostEditor)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.lineEdit_9)
        self.label_50 = QtGui.QLabel(self.signpostEditor)
        self.label_50.setObjectName(_fromUtf8("label_50"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_50)
        self.eventsStackedWidget.addWidget(self.signpostEditor)
        self.gridLayout_5.addWidget(self.eventsStackedWidget, 7, 1, 1, 4)
        self.gridLayout_4.addWidget(self.EventsBox, 0, 1, 1, 1)
        self.tabWidget.addTab(self.EventsTab, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 776, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setMinimumSize(QtCore.QSize(180, 129))
        self.dockWidget.setBaseSize(QtCore.QSize(0, 0))
        self.dockWidget.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.treeView = QtGui.QTreeView(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setMinimumSize(QtCore.QSize(50, 0))
        self.treeView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.treeView.setIndentation(10)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.verticalLayout.addWidget(self.treeView)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.actionLoad_ROM = QtGui.QAction(MainWindow)
        self.actionLoad_ROM.setObjectName(_fromUtf8("actionLoad_ROM"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.menuFile.addAction(self.actionLoad_ROM)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.eventsStackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Blue Spider", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mapTab), _translate("MainWindow", "Map", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.movPermissionsTab), _translate("MainWindow", "Movement Permissions", None))
        self.EventsBox.setTitle(_translate("MainWindow", "Add events", None))
        self.label_2.setText(_translate("MainWindow", "0", None))
        self.label_5.setText(_translate("MainWindow", "Triggers:", None))
        self.label.setText(_translate("MainWindow", "Warps: ", None))
        self.addTriggerButton.setText(_translate("MainWindow", "+", None))
        self.addSignpostButton.setText(_translate("MainWindow", "+", None))
        self.label_4.setText(_translate("MainWindow", "People:", None))
        self.label_8.setText(_translate("MainWindow", "0", None))
        self.addPersonButton.setText(_translate("MainWindow", "+", None))
        self.groupBox.setTitle(_translate("MainWindow", "Edit event", None))
        self.label_6.setText(_translate("MainWindow", "0", None))
        self.label_7.setText(_translate("MainWindow", "Signposts:", None))
        self.addWarpButton.setText(_translate("MainWindow", "+", None))
        self.label_3.setText(_translate("MainWindow", "0", None))
        self.label_10.setText(_translate("MainWindow", "X pos", None))
        self.label_9.setText(_translate("MainWindow", "Y pos", None))
        self.label_11.setText(_translate("MainWindow", "Unknown", None))
        self.label_12.setText(_translate("MainWindow", "Bank num.", None))
        self.label_13.setText(_translate("MainWindow", "Map num.", None))
        self.label_14.setText(_translate("MainWindow", "Warp num.", None))
        self.label_16.setText(_translate("MainWindow", "Person num.", None))
        self.label_17.setText(_translate("MainWindow", "Sprite num.", None))
        self.label_18.setText(_translate("MainWindow", "Unknown", None))
        self.label_15.setText(_translate("MainWindow", "X/Y", None))
        self.label_19.setText(_translate("MainWindow", "Unknown", None))
        self.label_20.setText(_translate("MainWindow", "Mov. type", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "No movement", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "Look around", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "Walk around", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "Walk up and down", None))
        self.label_21.setText(_translate("MainWindow", "Movement", None))
        self.label_22.setText(_translate("MainWindow", "Unknown", None))
        self.label_23.setText(_translate("MainWindow", "Is a trainer", None))
        self.label_24.setText(_translate("MainWindow", "Unknown", None))
        self.label_25.setText(_translate("MainWindow", "Vier radius", None))
        self.label_26.setText(_translate("MainWindow", "Script offset", None))
        self.label_27.setText(_translate("MainWindow", "Flag", None))
        self.label_28.setText(_translate("MainWindow", "Unknown", None))
        self.label_49.setText(_translate("MainWindow", "Trigger", None))
        self.label_50.setText(_translate("MainWindow", "Signpost", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.EventsTab), _translate("MainWindow", "Events", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionLoad_ROM.setText(_translate("MainWindow", "Load ROM", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))

