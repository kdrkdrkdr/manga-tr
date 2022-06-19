
from typing import Text
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import os, glob
from lib.translate import translate_image



class RunTranslate(QThread):
    changeValue = Signal(int)

    def __init__(self, window, gmail):
        QThread.__init__(self)
        self.window = window
        self.ltsd = gmail.split('@gmail.com')[0]
        

    def stop(self):
        self.terminate()


    def run(self):
        self.changeValue.emit(0)
        src_dir = self.window.transed_file_dir.text().replace('/', '\\')

        imageTypes = ('jpeg', 'jpg', 'png', 'webp')
        imageList = []
        for ext in imageTypes:
            imageList.extend(glob.glob(f'{src_dir}\\*.{ext}'))


        if len(imageList) == 0:
            self.window.run_translate_btn.setText('번역하기')
            return


        for i, j in enumerate(imageList):

            src_path = f'{src_dir}\\{os.path.basename(j)}'
            dst_dir = f'{src_dir}\\TRANSLATED'
            
            if not os.path.isdir(dst_dir):
                os.mkdir(dst_dir)

            t = translate_image(
                server_base_url=f'https://mts-{self.ltsd}.loca.lt',
                image_path=src_path,
                output_path=f'{dst_dir}\\{os.path.basename(j)}',
            )

            self.window.f_log_browser.append(f'{t} 에 저장되었습니다.')
            self.changeValue.emit(int(100* (i+1)/len(imageList)))
            self.window.f_log_browser.verticalScrollBar().setValue(self.window.f_log_browser.verticalScrollBar().maximum())


        self.window.f_log_browser.append('\n번역 완료!')
        self.window.run_translate_btn.setText('번역하기')
        