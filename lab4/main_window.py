import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap

# Импортируйте функции из предыдущих заданий
from main import create_annotation_file as create_annotation_file_func
from main import copy_dataset_with_new_names
from main import get_next_instance_by_class

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lab 4")

        self.central_widget = QWidget(self)
        self.layout = QVBoxLayout(self.central_widget)

        self.annotation_button = QPushButton("Create Annotation")
        self.annotation_button.setStyleSheet("background-color : red")
        self.annotation_button.clicked.connect(self.create_annotation)

        self.copy_button = QPushButton("Copy Dataset with New Names")
        self.copy_button.setStyleSheet("background-color : orange")
        self.copy_button.clicked.connect(self.copy_dataset)

        self.next_zebra_button = QPushButton("Next Zebra")
        self.next_zebra_button.setStyleSheet("background-color : blue")
        self.next_zebra_button.clicked.connect(self.get_next_zebra)

        self.next_horse_button = QPushButton("Next Horse")
        self.next_horse_button.setStyleSheet("background-color : purple")
        self.next_horse_button.clicked.connect(self.get_next_horse)

        self.image_label = QLabel()

        self.layout.addWidget(self.annotation_button)
        self.layout.addWidget(self.copy_button)
        self.layout.addWidget(self.next_zebra_button)
        self.layout.addWidget(self.next_horse_button)
        self.layout.addWidget(self.image_label)

        self.setCentralWidget(self.central_widget)

        self.dataset_dir = "D:\\Ucheba\\3 course\\PD\\lab2\\dataset"

    def create_annotation(self):
        self.dataset_dir = QFileDialog.getExistingDirectory(self, "Select Dataset Folder")

        if self.dataset_dir:
            annotation_file_path, _ = QFileDialog.getSaveFileName(self, "Save Annotation File", "", "CSV Files (*.csv)")
            if annotation_file_path:
                create_annotation_file_func(self.dataset_dir, annotation_file_path)  # Вызываем версию функции с двумя аргументами


    def copy_dataset(self):
        self.dataset_dir = QFileDialog.getExistingDirectory(self, "Select Dataset Folder")

        if self.dataset_dir:
            new_dataset_dir = QFileDialog.getExistingDirectory(self, "Select Destination Folder")

            if new_dataset_dir:
                copy_dataset_with_new_names(self.dataset_dir, new_dataset_dir)  # Вызываем функцию с нужными аргументами
                # annotation_file_path, _ = QFileDialog.getSaveFileName(self, "Save Annotation File", "", "CSV Files (*.csv)")
                #
                # if annotation_file_path:
                #     create_annotation_file_func(annotation_data, annotation_file_path)  # Вызываем функцию с правильными аргументами

    def get_next_zebra(self):
        if self.dataset_dir:
            zebra_generator = get_next_instance_by_class("zebra", self.dataset_dir)
            zebra_instance = next(zebra_generator, None)

            if zebra_instance:
                pixmap = QPixmap(zebra_instance)
                self.image_label.setPixmap(pixmap)
                self.image_label.show()
            else:
                self.image_label.clear()
                self.image_label.hide()


    def get_next_horse(self):
        if self.dataset_dir:
            horse_generator = get_next_instance_by_class("bay_horse", self.dataset_dir)
            horse_instance = next(horse_generator, None)

            if horse_instance:
                pixmap = QPixmap(horse_instance)
                self.image_label.setPixmap(pixmap)
                self.image_label.show()
            else:
                self.image_label.clear()
                self.image_label.hide()


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()