# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QWidget)
import icons_rc

class Ui_w_MusicDownload(object):
    def setupUi(self, w_MusicDownload):
        if not w_MusicDownload.objectName():
            w_MusicDownload.setObjectName(u"w_MusicDownload")
        w_MusicDownload.resize(734, 546)
        font = QFont()
        font.setPointSize(12)
        w_MusicDownload.setFont(font)
        icon = QIcon()
        icon.addFile(u":/main/music_player.png", QSize(), QIcon.Normal, QIcon.Off)
        w_MusicDownload.setWindowIcon(icon)
        w_MusicDownload.setLocale(QLocale(QLocale.Chinese, QLocale.China))
        self.gridLayout = QGridLayout(w_MusicDownload)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gb_Setup = QGroupBox(w_MusicDownload)
        self.gb_Setup.setObjectName(u"gb_Setup")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei"])
        font1.setPointSize(20)
        self.gb_Setup.setFont(font1)
        self.gb_Setup.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_2 = QHBoxLayout(self.gb_Setup)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lb_Language = QLabel(self.gb_Setup)
        self.lb_Language.setObjectName(u"lb_Language")
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei"])
        font2.setPointSize(16)
        self.lb_Language.setFont(font2)

        self.horizontalLayout_2.addWidget(self.lb_Language)

        self.rb_CN = QRadioButton(self.gb_Setup)
        self.rb_CN.setObjectName(u"rb_CN")
        font3 = QFont()
        font3.setFamilies([u"Microsoft YaHei"])
        font3.setPointSize(14)
        self.rb_CN.setFont(font3)
        self.rb_CN.setChecked(True)

        self.horizontalLayout_2.addWidget(self.rb_CN)

        self.rb_EN = QRadioButton(self.gb_Setup)
        self.rb_EN.setObjectName(u"rb_EN")
        self.rb_EN.setFont(font3)

        self.horizontalLayout_2.addWidget(self.rb_EN)

        self.hspacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.hspacer_1)

        self.cb_theme = QCheckBox(self.gb_Setup)
        self.cb_theme.setObjectName(u"cb_theme")
        self.cb_theme.setStyleSheet(u"QCheckBox::indicator {\n"
"width: 40 px;\n"
"height: 40 px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/light_mode/light_mode.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image:  url(:/dark_mode/dark_mode.png);\n"
"}")

        self.horizontalLayout_2.addWidget(self.cb_theme)


        self.gridLayout.addWidget(self.gb_Setup, 0, 0, 1, 1)

        self.gb_Download = QGroupBox(w_MusicDownload)
        self.gb_Download.setObjectName(u"gb_Download")
        font4 = QFont()
        font4.setFamilies([u"Microsoft YaHei"])
        font4.setPointSize(20)
        font4.setUnderline(False)
        self.gb_Download.setFont(font4)
        self.gb_Download.setAlignment(Qt.AlignCenter)
        self.gridLayou = QGridLayout(self.gb_Download)
        self.gridLayou.setObjectName(u"gridLayou")
        self.gridLayou.setContentsMargins(-1, -1, 9, -1)
        self.lb_DownloadFolder = QLabel(self.gb_Download)
        self.lb_DownloadFolder.setObjectName(u"lb_DownloadFolder")
        font5 = QFont()
        font5.setFamilies([u"Microsoft YaHei"])
        font5.setPointSize(16)
        font5.setUnderline(False)
        self.lb_DownloadFolder.setFont(font5)

        self.gridLayou.addWidget(self.lb_DownloadFolder, 0, 0, 1, 1)

        self.le_DownloadFolder = QLineEdit(self.gb_Download)
        self.le_DownloadFolder.setObjectName(u"le_DownloadFolder")
        font6 = QFont()
        font6.setFamilies([u"Microsoft YaHei"])
        font6.setPointSize(14)
        font6.setUnderline(False)
        self.le_DownloadFolder.setFont(font6)

        self.gridLayou.addWidget(self.le_DownloadFolder, 0, 1, 1, 1)

        self.pb_Browse = QPushButton(self.gb_Download)
        self.pb_Browse.setObjectName(u"pb_Browse")
        self.pb_Browse.setFont(font6)

        self.gridLayou.addWidget(self.pb_Browse, 0, 2, 1, 1)

        self.pb_Download = QPushButton(self.gb_Download)
        self.pb_Download.setObjectName(u"pb_Download")
        self.pb_Download.setFont(font5)
        icon1 = QIcon()
        icon1.addFile(u":/download/download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_Download.setIcon(icon1)

        self.gridLayou.addWidget(self.pb_Download, 1, 0, 1, 3)


        self.gridLayout.addWidget(self.gb_Download, 5, 0, 1, 1)

        self.lb_Msg = QLabel(w_MusicDownload)
        self.lb_Msg.setObjectName(u"lb_Msg")
        font7 = QFont()
        font7.setFamilies([u"Microsoft YaHei"])
        font7.setPointSize(10)
        font7.setItalic(True)
        self.lb_Msg.setFont(font7)

        self.gridLayout.addWidget(self.lb_Msg, 6, 0, 1, 1)

        self.gb_Info = QGroupBox(w_MusicDownload)
        self.gb_Info.setObjectName(u"gb_Info")
        self.gb_Info.setFont(font4)
        self.gb_Info.setAlignment(Qt.AlignCenter)
        self.formLayout = QFormLayout(self.gb_Info)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lb_Title = QLabel(self.gb_Info)
        self.lb_Title.setObjectName(u"lb_Title")
        self.lb_Title.setFont(font5)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lb_Title)

        self.le_Title = QLineEdit(self.gb_Info)
        self.le_Title.setObjectName(u"le_Title")
        self.le_Title.setFont(font5)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_Title)

        self.lb_Author = QLabel(self.gb_Info)
        self.lb_Author.setObjectName(u"lb_Author")
        self.lb_Author.setFont(font5)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lb_Author)

        self.le_Author = QLineEdit(self.gb_Info)
        self.le_Author.setObjectName(u"le_Author")
        self.le_Author.setFont(font5)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_Author)

        self.vspacer_1 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(2, QFormLayout.SpanningRole, self.vspacer_1)


        self.gridLayout.addWidget(self.gb_Info, 4, 0, 1, 1)

        self.gb_Src = QGroupBox(w_MusicDownload)
        self.gb_Src.setObjectName(u"gb_Src")
        self.gb_Src.setFont(font4)
        self.gb_Src.setAlignment(Qt.AlignCenter)
        self.gb_Src.setFlat(False)
        self.horizontalLayout = QHBoxLayout(self.gb_Src)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_Url = QLabel(self.gb_Src)
        self.lb_Url.setObjectName(u"lb_Url")
        self.lb_Url.setFont(font5)

        self.horizontalLayout.addWidget(self.lb_Url)

        self.le_Url = QLineEdit(self.gb_Src)
        self.le_Url.setObjectName(u"le_Url")
        self.le_Url.setFont(font6)

        self.horizontalLayout.addWidget(self.le_Url)

        self.pb_Clear = QPushButton(self.gb_Src)
        self.pb_Clear.setObjectName(u"pb_Clear")
        self.pb_Clear.setFont(font6)

        self.horizontalLayout.addWidget(self.pb_Clear)


        self.gridLayout.addWidget(self.gb_Src, 2, 0, 1, 1)

        QWidget.setTabOrder(self.rb_CN, self.rb_EN)
        QWidget.setTabOrder(self.rb_EN, self.le_Url)
        QWidget.setTabOrder(self.le_Url, self.pb_Clear)
        QWidget.setTabOrder(self.pb_Clear, self.le_Title)
        QWidget.setTabOrder(self.le_Title, self.le_Author)
        QWidget.setTabOrder(self.le_Author, self.le_DownloadFolder)
        QWidget.setTabOrder(self.le_DownloadFolder, self.pb_Browse)
        QWidget.setTabOrder(self.pb_Browse, self.pb_Download)

        self.retranslateUi(w_MusicDownload)

        QMetaObject.connectSlotsByName(w_MusicDownload)
    # setupUi

    def retranslateUi(self, w_MusicDownload):
        w_MusicDownload.setWindowTitle(QCoreApplication.translate("w_MusicDownload", u"Youtube Music MP3 Downloader", None))
        self.gb_Setup.setTitle(QCoreApplication.translate("w_MusicDownload", u"- \u754c\u9762\u8bbe\u7f6e -", None))
        self.lb_Language.setText(QCoreApplication.translate("w_MusicDownload", u"\u8bed\u8a00\uff1a", None))
        self.rb_CN.setText(QCoreApplication.translate("w_MusicDownload", u"\u7b80\u4f53\u4e2d\u6587", None))
        self.rb_EN.setText(QCoreApplication.translate("w_MusicDownload", u"English", None))
        self.cb_theme.setText("")
        self.gb_Download.setTitle(QCoreApplication.translate("w_MusicDownload", u"- \u4e0b\u8f7d -", None))
        self.lb_DownloadFolder.setText(QCoreApplication.translate("w_MusicDownload", u"\u6587\u4ef6\u5939\uff1a", None))
        self.pb_Browse.setText(QCoreApplication.translate("w_MusicDownload", u"\u6d4f\u89c8", None))
        self.pb_Download.setText(QCoreApplication.translate("w_MusicDownload", u"\u70b9\u51fb\u4e0b\u8f7d", None))
        self.lb_Msg.setText("")
        self.gb_Info.setTitle(QCoreApplication.translate("w_MusicDownload", u"- \u6b4c\u66f2\u4fe1\u606f -", None))
        self.lb_Title.setText(QCoreApplication.translate("w_MusicDownload", u"\u6b4c\u540d\uff1a", None))
        self.lb_Author.setText(QCoreApplication.translate("w_MusicDownload", u"\u4f5c\u8005\uff1a", None))
        self.gb_Src.setTitle(QCoreApplication.translate("w_MusicDownload", u"- \u8f93\u5165\u6b4c\u66f2YouTube\u94fe\u63a5 -", None))
        self.lb_Url.setText(QCoreApplication.translate("w_MusicDownload", u"\u94fe\u63a5\uff1a", None))
        self.pb_Clear.setText(QCoreApplication.translate("w_MusicDownload", u"\u6e05\u7a7a", None))
    # retranslateUi

