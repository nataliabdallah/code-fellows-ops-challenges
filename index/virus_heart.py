import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtCore import Qt, QTimer

class TransparentWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_TranslucentBackground)  # Make the window background transparent
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # Remove window decorations and keep on top

        # Load the two heart images and scale them down by 15%
        self.pixmap1 = QPixmap('heart-1.png').scaledToWidth(int(0.85 * QPixmap('heart-1.png').width()), Qt.SmoothTransformation)
        self.pixmap2 = QPixmap('heart-2.png').scaledToWidth(int(0.85 * QPixmap('heart-2.png').width()), Qt.SmoothTransformation)

        self.showFullScreen()  # Make the window full screen

        # Define the base sequence
        base_sequence = [
            ('left', self.pixmap1, 500),
            ('right', self.pixmap1, 500),
            ('top', self.pixmap1, 500),
            ('middle', self.pixmap1, 1000),
            ('left', self.pixmap2, 500),
            ('right', self.pixmap2, 500),
            ('top', self.pixmap2, 500),
            ('middle', self.pixmap2, 1000)
        ]

        # Repeat the base sequence 4 times to form the full sequence
        self.sequence = base_sequence * 4  # Repeat the sequence 4 times

        self.sequenceIndex = 0  # To keep track of the current position in the sequence
        self.showNextHeart()

    def showNextHeart(self):
        if self.sequenceIndex >= len(self.sequence):
            self.sequenceIndex = 0  # Reset the sequence

        position, pixmap, duration = self.sequence[self.sequenceIndex]
        self.sequenceIndex += 1

        label = QLabel(self)
        label.setPixmap(pixmap)

        # Position the heart label
        if position == 'left':
            label.move(0, self.height() // 2 - pixmap.height() // 2)  # Center vertically
        elif position == 'right':
            label.move(self.width() - pixmap.width(), self.height() // 2 - pixmap.height() // 2)  # Center vertically
        elif position == 'top':
            label.move(self.width() // 2 - pixmap.width() // 2, 0)  # Center horizontally
        else:  # Middle
            label.move(self.width() // 2 - pixmap.width() // 2, self.height() // 2 - pixmap.height() // 2)

        label.show()

        # Timer to remove the heart and continue the sequence
        QTimer.singleShot(duration, label.deleteLater)
        QTimer.singleShot(duration, self.showNextHeart)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setOpacity(0.0)  # Set the opacity of the window itself to fully transparent
        painter.setBrush(QColor(255, 255, 255))
        painter.setPen(QColor(255, 255, 255))
        painter.drawRect(self.rect())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TransparentWindow()
    sys.exit(app.exec_())
