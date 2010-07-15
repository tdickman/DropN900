# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'managerwidget.ui'
#
# Created: Thu Jul 15 03:23:37 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ManagerWidget(object):
    def setupUi(self, ManagerWidget):
        ManagerWidget.setObjectName("ManagerWidget")
        ManagerWidget.resize(721, 393)
        ManagerWidget.setStyleSheet("QFrame#frame_controls_bottom, #frame_controls_right {\n"
"    background: black;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #0099FF;\n"
"}\n"
"\n"
"QLabel#thumb_container {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QTreeWidget#tree_widget {\n"
"    background-color: transparent;\n"
"    font-size: 15px;\n"
"    border: 0px;\n"
"    border-bottom: 2px solid rgba(255,255,255,200);\n"
"    border-right: 2px solid rgba(255,255,255,200);\n"
"    border-bottom-right-radius: 10px;\n"
"    padding-bottom: 5px;\n"
"}")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(ManagerWidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tree_widget = QtGui.QTreeWidget(ManagerWidget)
        self.tree_widget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tree_widget.setFrameShadow(QtGui.QFrame.Sunken)
        self.tree_widget.setLineWidth(1)
        self.tree_widget.setUniformRowHeights(True)
        self.tree_widget.setAnimated(True)
        self.tree_widget.setObjectName("tree_widget")
        self.tree_widget.header().setVisible(True)
        self.tree_widget.header().setDefaultSectionSize(300)
        self.tree_widget.header().setMinimumSectionSize(75)
        self.verticalLayout.addWidget(self.tree_widget)
        self.frame_controls_bottom = QtGui.QFrame(ManagerWidget)
        self.frame_controls_bottom.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_controls_bottom.setLineWidth(0)
        self.frame_controls_bottom.setObjectName("frame_controls_bottom")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_controls_bottom)
        self.verticalLayout_3.setContentsMargins(8, 8, 0, 8)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.public_link_line_edit = QtGui.QLineEdit(self.frame_controls_bottom)
        self.public_link_line_edit.setReadOnly(True)
        self.public_link_line_edit.setObjectName("public_link_line_edit")
        self.horizontalLayout_3.addWidget(self.public_link_line_edit)
        self.button_open_public_link = QtGui.QPushButton(self.frame_controls_bottom)
        self.button_open_public_link.setObjectName("button_open_public_link")
        self.horizontalLayout_3.addWidget(self.button_open_public_link)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.selected_icon_label = QtGui.QLabel(self.frame_controls_bottom)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selected_icon_label.sizePolicy().hasHeightForWidth())
        self.selected_icon_label.setSizePolicy(sizePolicy)
        self.selected_icon_label.setMinimumSize(QtCore.QSize(24, 24))
        self.selected_icon_label.setMaximumSize(QtCore.QSize(24, 24))
        self.selected_icon_label.setText("")
        self.selected_icon_label.setObjectName("selected_icon_label")
        self.horizontalLayout_4.addWidget(self.selected_icon_label)
        self.selected_name_label = QtGui.QLabel(self.frame_controls_bottom)
        self.selected_name_label.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.selected_name_label.setFont(font)
        self.selected_name_label.setText("")
        self.selected_name_label.setObjectName("selected_name_label")
        self.horizontalLayout_4.addWidget(self.selected_name_label)
        spacerItem = QtGui.QSpacerItem(40, 24, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.modified_label = QtGui.QLabel(self.frame_controls_bottom)
        self.modified_label.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.modified_label.setFont(font)
        self.modified_label.setText("")
        self.modified_label.setObjectName("modified_label")
        self.horizontalLayout_4.addWidget(self.modified_label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.frame_controls_bottom)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.frame_controls_right = QtGui.QFrame(ManagerWidget)
        self.frame_controls_right.setMinimumSize(QtCore.QSize(275, 0))
        self.frame_controls_right.setMaximumSize(QtCore.QSize(275, 16777215))
        self.frame_controls_right.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_controls_right.setLineWidth(0)
        self.frame_controls_right.setObjectName("frame_controls_right")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_controls_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setMargin(8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.button_download = QtGui.QPushButton(self.frame_controls_right)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_download.setFont(font)
        self.button_download.setStyleSheet("None")
        self.button_download.setObjectName("button_download")
        self.verticalLayout_2.addWidget(self.button_download)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.button_remove = QtGui.QPushButton(self.frame_controls_right)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_remove.setFont(font)
        self.button_remove.setObjectName("button_remove")
        self.horizontalLayout_5.addWidget(self.button_remove)
        self.button_rename = QtGui.QPushButton(self.frame_controls_right)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_rename.setFont(font)
        self.button_rename.setObjectName("button_rename")
        self.horizontalLayout_5.addWidget(self.button_rename)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.button_new_folder = QtGui.QPushButton(self.frame_controls_right)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_new_folder.setFont(font)
        self.button_new_folder.setObjectName("button_new_folder")
        self.horizontalLayout_6.addWidget(self.button_new_folder)
        self.button_upload = QtGui.QPushButton(self.frame_controls_right)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_upload.setFont(font)
        self.button_upload.setObjectName("button_upload")
        self.horizontalLayout_6.addWidget(self.button_upload)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.action_layout = QtGui.QVBoxLayout()
        self.action_layout.setSpacing(0)
        self.action_layout.setObjectName("action_layout")
        spacerItem1 = QtGui.QSpacerItem(1, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.action_layout.addItem(spacerItem1)
        self.thumb_container = QtGui.QLabel(self.frame_controls_right)
        self.thumb_container.setLineWidth(0)
        self.thumb_container.setText("")
        self.thumb_container.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.thumb_container.setObjectName("thumb_container")
        self.action_layout.addWidget(self.thumb_container)
        spacerItem2 = QtGui.QSpacerItem(1, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.action_layout.addItem(spacerItem2)
        spacerItem3 = QtGui.QSpacerItem(1, 1, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.action_layout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.action_layout)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(8)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem4 = QtGui.QSpacerItem(1, 24, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.label_username = QtGui.QLabel(self.frame_controls_right)
        self.label_username.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_username.setFont(font)
        self.label_username.setText("")
        self.label_username.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_username.setObjectName("label_username")
        self.horizontalLayout_8.addWidget(self.label_username)
        self.label_username_icon = QtGui.QLabel(self.frame_controls_right)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_username_icon.sizePolicy().hasHeightForWidth())
        self.label_username_icon.setSizePolicy(sizePolicy)
        self.label_username_icon.setMinimumSize(QtCore.QSize(24, 24))
        self.label_username_icon.setMaximumSize(QtCore.QSize(24, 24))
        self.label_username_icon.setText("")
        self.label_username_icon.setObjectName("label_username_icon")
        self.horizontalLayout_8.addWidget(self.label_username_icon)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_2.addWidget(self.frame_controls_right)

        self.retranslateUi(ManagerWidget)
        QtCore.QMetaObject.connectSlotsByName(ManagerWidget)

    def retranslateUi(self, ManagerWidget):
        ManagerWidget.setWindowTitle(QtGui.QApplication.translate("ManagerWidget", "ManagerWidget", None, QtGui.QApplication.UnicodeUTF8))
        self.tree_widget.headerItem().setText(0, QtGui.QApplication.translate("ManagerWidget", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.tree_widget.headerItem().setText(1, QtGui.QApplication.translate("ManagerWidget", "Size", None, QtGui.QApplication.UnicodeUTF8))
        self.button_open_public_link.setText(QtGui.QApplication.translate("ManagerWidget", "Open Public Link", None, QtGui.QApplication.UnicodeUTF8))
        self.button_download.setText(QtGui.QApplication.translate("ManagerWidget", "Download", None, QtGui.QApplication.UnicodeUTF8))
        self.button_remove.setText(QtGui.QApplication.translate("ManagerWidget", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.button_rename.setText(QtGui.QApplication.translate("ManagerWidget", "Rename", None, QtGui.QApplication.UnicodeUTF8))
        self.button_new_folder.setText(QtGui.QApplication.translate("ManagerWidget", "New Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.button_upload.setText(QtGui.QApplication.translate("ManagerWidget", "Upload File", None, QtGui.QApplication.UnicodeUTF8))

