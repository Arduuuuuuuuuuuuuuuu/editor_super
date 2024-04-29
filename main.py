
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QListWidget, QFileDialog
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageFilter
from PyQt5.QtCore import Qt
import os


class ImageProcessor():
    def __init__(self):
        self.picture = None
        self.folder = None
        self.picture_name = None
        self.modified_folder = 'Modified/'

    def load_image(self, folder, name):
        self.folder = folder
        self.picture_name = name
        image_path = os.path.join(self.folder, self.picture_name)
        self.picture = Image.open(image_path)

    def show_image(self, path):
        image_label.hide()

        pixmapimage = QPixmap(path)
        w, h = image_label.width(), image_label.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        image_label.setPixmap(pixmapimage)
        image_label.show()

    def save_image(self):
        path = os.path.join(workdir, self.modified_folder)
        if not (os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.picture_name)
        self.picture.save(image_path)

    def do_bw(self):
        self.picture = self.picture.convert("L")
        self.save_image()
        image_path = os.path.join(workdir, self.modified_folder, self.picture_name)
        self.show_image(image_path)

    def do_mirror(self):
        self.picture = self.picture.transpose(Image.FLIP_LEFT_RIGHT)
        self.save_image()
        image_path = os.path.join(workdir, self.modified_folder, self.picture_name)
        self.show_image(image_path)

    def do_left(self):
        self.picture = self.picture.rotate(90)
        self.save_image()
        image_path = os.path.join(workdir, self.modified_folder, self.picture_name)
        self.show_image(image_path)

    def do_right(self):
        self.picture = self.picture.rotate(-90)
        self.save_image()
        image_path = os.path.join(workdir, self.modified_folder, self.picture_name)
        self.show_image(image_path)

    def do_sharpness(self):
        self.picture = self.picture.filter(ImageFilter.SHARPEN)
        self.save_image()
        image_path = os.path.join(workdir, self.modified_folder, self.picture_name)
        self.show_image(image_path)


work_image = ImageProcessor()


def show_chosen_image():
    if list_widget.currentRow() >= 0:
        naziv = list_widget.currentItem().text()
        work_image.load_image(workdir, naziv)
        image_path = os.path.join(workdir, work_image.picture_name)
        work_image.show_image(image_path)


app = QApplication([])

folder_button = QPushButton('Open Folder')
list_widget = QListWidget()

left_button = QPushButton('Left')
right_button = QPushButton('Right')
mirror_button = QPushButton('Mirror')
sharpness_button = QPushButton('Sharpness')
bw_button = QPushButton('B/W')

image_label = QLabel()
image_label.setAlignment(Qt.AlignCenter)

main_layout = QHBoxLayout()

left_layout = QVBoxLayout()
left_layout.addWidget(folder_button)
left_layout.addWidget(list_widget)

main_layout.addLayout(left_layout)

right_layout = QVBoxLayout()

button_layout = QHBoxLayout()
button_layout.addWidget(left_button)
button_layout.addWidget(right_button)
button_layout.addWidget(mirror_button)
button_layout.addWidget(sharpness_button)
button_layout.addWidget(bw_button)

right_layout.addWidget(image_label)
right_layout.addLayout(button_layout, 20)

main_layout.addLayout(right_layout, 80)

workdir = ''


def directory():
    global workdir
    workdir = QFileDialog.getExistingDirectory()


def graphic_files():
    directory()
    filenames = os.listdir(workdir)
    extension = [".jpg", ".png", ".svg", ".gif"]
    list_widget.clear()
    cleaned = []
    for f in filenames:
        for e in extension:
            if f.endswith(e):
                cleaned.append(f)

    for f in cleaned:
        list_widget.addItem(f)


list_widget.currentRowChanged.connect(show_chosen_image)
bw_button.clicked.connect(work_image.do_bw)
mirror_button.clicked.connect(work_image.do_mirror)
left_button.clicked.connect(work_image.do_left)
right_button.clicked.connect(work_image.do_right)
sharpness_button.clicked.connect(work_image.do_sharpness)

folder_button.clicked.connect(graphic_files)

main_window = QWidget()
main_window.setLayout(main_layout)
main_window.setWindowTitle('Photo Editor')
main_window.setGeometry(100, 100, 800, 400)
main_window.show()

list_widget.currentRowChanged.connect(show_chosen_image)

app.exec_()
































































































































































'''
def load_image(item):
   
    image_path = item.text()
    pixmap = QPixmap(image_path)
    image_label.setPixmap(pixmap)

def rotate_left():
 
    image_path = list_widget.currentItem().text()
    img = Image.open(image_path)
    img = img.rotate(90)
    img.save(image_path)
    load_image(list_widget.currentItem())

def rotate_right():
    # Rotate the displayed image to the right
    image_path = list_widget.currentItem().text()
    img = Image.open(image_path)
    img = img.rotate(-90)
    img.save(image_path)
    load_image(list_widget.currentItem())

def mirror_image():

    image_path = list_widget.currentItem().text()
    img = Image.open(image_path)
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    img.save(image_path)
    load_image(list_widget.currentItem())

folder_button.clicked.connect(open_folder)
list_widget.itemClicked.connect(load_image)
left_button.clicked.connect(rotate_left)
right_button.clicked.connect(rotate_right)
mirror_button.clicked.connect(mirror_image)


'''
   



'''
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QListWidget, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from PIL.ImageQt import ImageQt
from PIL import Image
import os

app = QApplication([])

class ImageProcessor:
    def __init__(self):
        self.current_image = None
        self.current_file_name = ''

    def loadImage(self):
        file_path = os.path.join(workdir, self.current_file_name)
        self.current_image = Image.open(file_path)

    def showImage(self):
        if self.current_image:
            q_image = ImageQt.ImageQt(self.current_image)
            pixmap = QPixmap.fromImage(QImage(q_image))
            image_label.setPixmap(pixmap)

def showChosenImage():
    selected_item = list_widget.currentItem()
    if selected_item:
        image_processor.current_file_name = selected_item.text()
        image_processor.loadImage()
        image_processor.showImage()

image_processor = ImageProcessor()

folder_button = QPushButton('Open Folder')
list_widget = QListWidget()

left_button = QPushButton('Left')
right_button = QPushButton('Right')
mirror_button = QPushButton('Mirror')
sharpness_button = QPushButton('Sharpness')
bw_button = QPushButton('B/W')

image_label = QLabel()
image_label.setAlignment(Qt.AlignCenter)

main_layout = QHBoxLayout()

left_layout = QVBoxLayout()
left_layout.addWidget(folder_button)
left_layout.addWidget(list_widget)

main_layout.addLayout(left_layout)

right_layout = QVBoxLayout()

button_layout = QHBoxLayout()
button_layout.addWidget(left_button)
button_layout.addWidget(right_button)
button_layout.addWidget(mirror_button)
button_layout.addWidget(sharpness_button)
button_layout.addWidget(bw_button)

right_layout.addWidget(image_label)
right_layout.addLayout(button_layout, 20)

main_layout.addLayout(right_layout, 80)

workdir = ''

def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def filter():
    global workdir
    if not workdir:
        return []
    
    filenames = os.listdir(workdir)
    extension = [".jpg", ".png", ".svg", ".gif"]
    cleaned = []
    for f in filenames:
        for e in extension:
            if f.endswith(e):
                cleaned.append(f)
    return cleaned

def folder_button_clicked():
    chooseWorkdir()
    graphic_files = filter()
    list_widget.clear()
    for f in graphic_files:
        list_widget.addItem(f)

def showChosenImage():
    selected_item = list_widget.currentItem()
    if selected_item:
        image_processor.current_file_name = selected_item.text()
        image_processor.loadImage()
        image_processor.showImage()

folder_button.clicked.connect(folder_button_clicked)
list_widget.itemClicked.connect(showChosenImage)

'''
























































































