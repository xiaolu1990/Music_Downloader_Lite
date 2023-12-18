#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Application to download music from YouTube
"""

__author__ = "Zhangshun.Lu"
__license__ = "MIT License"
__version__ = "0.0.1"

import sys

from PySide6 import QtCore
from PySide6 import QtWidgets

from Application.UI.main_window import Ui_w_MusicDownload

from pytube import YouTube

from pathlib import Path

import qt_material


class MainWindow(QtWidgets.QWidget, Ui_w_MusicDownload):
    media = None
    best_quality_audio = None
    url = ''
    title = ''
    author = ''
    output_folder = ''

    mode_english = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle(f'{self.windowTitle()}  v{__version__}')

        self.cb_theme.stateChanged.connect(self.process_theme)

        self.le_Url.clear()
        self.le_Title.clear()
        self.le_Author.clear()
        self.le_DownloadFolder.clear()
        self.lb_Msg.clear()

        self.le_Url.textChanged.connect(self.process_url)
        self.le_Title.textChanged.connect(self.process_title)
        self.le_Author.textChanged.connect(self.process_author)
        self.pb_Clear.clicked.connect(self.process_clear)
        self.pb_Browse.clicked.connect(self.process_browse)
        self.pb_Download.clicked.connect(self.process_download)

        self.rb_CN.pressed.connect(self.process_language)
        self.rb_EN.pressed.connect(self.process_language)

    def process_theme(self):
        if self.cb_theme.isChecked():
            qt_material.apply_stylesheet(self, theme='dark_pink.xml', invert_secondary=False)
            self.le_Url.setStyleSheet('color: white')
            self.le_Title.setStyleSheet('color: white')
            self.le_Author.setStyleSheet('color: white')
            self.le_DownloadFolder.setStyleSheet('color: white')
        else:
            qt_material.apply_stylesheet(self, theme='light_pink.xml', invert_secondary=True)
            self.le_Url.setStyleSheet('color: black')
            self.le_Title.setStyleSheet('color: black')
            self.le_Author.setStyleSheet('color: black')
            self.le_DownloadFolder.setStyleSheet('color: black')

    @QtCore.Slot()
    def process_clear(self):
        self.le_Url.clear()
        self.le_Title.clear()
        self.le_Author.clear()

    @QtCore.Slot()
    def process_url(self):
        if self.le_Url.text():  # url not empty, analyze url
            self.url = self.le_Url.text()

            # construct a YouTube object
            self.media = YouTube(self.url)

            # filter the best quality audio
            self.best_quality_audio = self.media.streams.filter(only_audio=True).order_by('abr').desc().first()

            # display music title
            self.le_Title.setText(self.media.title)

            # display music author
            self.le_Author.setText(self.media.author)

            # display in msg box
            self.lb_Msg.setText(f'{self.title}_{self.author}')
        else:
            if self.mode_english:
                self.lb_Msg.setText('Invalid URL')
            else:
                self.lb_Msg.setText('链接无效')

    @QtCore.Slot()
    def process_title(self):
        self.title = self.le_Title.text()
        self.lb_Msg.setText(f'{self.title}_{self.author}')

    @QtCore.Slot()
    def process_author(self):
        self.author = self.le_Author.text()
        self.lb_Msg.setText(f'{self.title}_{self.author}')

    # https://www.pythontutorial.net/pyqt/pyqt-qfiledialog/
    @QtCore.Slot()
    def process_browse(self):
        dialog = QtWidgets.QFileDialog(self)

        # set the default directory to home
        dir_home = str(Path.home())
        dialog.setDirectory(dir_home)

        self.output_folder = dialog.getExistingDirectory(self, 'Select Folder', '')
        if self.output_folder:
            self.le_DownloadFolder.setText(f'{self.output_folder}')

    @QtCore.Slot()
    def process_download(self):
        try:
            f_name = f'{self.title}_{self.author}.mp3'
            self.best_quality_audio.download(output_path=self.le_DownloadFolder.text(), filename=f_name,
                                             skip_existing=True)

            if self.mode_english:
                self.lb_Msg.setText('Download Success!')
            else:
                self.lb_Msg.setText('下载完成！')
        except KeyError:
            if self.mode_english:
                self.lb_Msg.setText('Download Failed!')
            else:
                self.lb_Msg.setText('错误！无法下载')

    @QtCore.Slot()
    def process_language(self):
        rb_text = self.sender().text()

        if rb_text == 'English':
            self.gb_Setup.setTitle('- Preferences -')
            self.gb_Src.setTitle('- Enter YouTube Music URL -')
            self.gb_Info.setTitle('- Information -')
            self.gb_Download.setTitle('- Download -')

            self.lb_Language.setText('Language:')
            self.lb_Url.setText('URL:')
            self.lb_Title.setText('Title:')
            self.lb_Author.setText('Author:')
            self.lb_DownloadFolder.setText('Download Folder:')

            self.pb_Clear.setText('Clear')
            self.pb_Browse.setText('Browse')
            self.pb_Download.setText('Download')

            self.mode_english = True
        elif rb_text == '简体中文':
            self.gb_Setup.setTitle('- 界面设置 -')
            self.gb_Src.setTitle('- 输入歌曲YouTube链接 -')
            self.gb_Info.setTitle('- 歌曲信息 -')
            self.gb_Download.setTitle('- 下载歌曲 -')

            self.lb_Language.setText('语言:')
            self.lb_Url.setText('链接:')
            self.lb_Title.setText('歌名:')
            self.lb_Author.setText('作者:')
            self.lb_DownloadFolder.setText('文件夹:')

            self.pb_Clear.setText('清空')
            self.pb_Browse.setText('浏览')
            self.pb_Download.setText('点击下载')

            self.mode_english = False


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()

    qt_material.apply_stylesheet(window, theme='light_pink.xml')

    window.show()

    sys.exit(app.exec())
