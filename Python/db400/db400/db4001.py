import os
import sys
import jaydebeapi
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                               QLabel, QLineEdit, QPushButton, QPlainTextEdit, 
                               QMessageBox, QTableWidget, QTableWidgetItem,
                               QMainWindow, QFileDialog, QFrame)
from PySide6.QtGui import QFont, QShortcut, QKeySequence
from PySide6.QtCore import Qt, QCoreApplication
from openpyxl import Workbook

# 確保程序完全退出
def force_quit():
    QCoreApplication.quit()
    sys.exit(0)

jt400_path = "/root/SourceDoc/jt400-20.0.7.jar"
if not os.path.exists(jt400_path):
    print(f"錯誤：jt400.jar 文件未找到：{jt400_path}")
    sys.exit(1)

java_home = "/Library/Java/JavaVirtualMachines/jdk-22.jdk/Contents/Home"
os.environ["JAVA_HOME"] = java_home
os.environ["PATH"] = f"{java_home}/bin:{os.environ.get('PATH', '')}"
os.environ["CLASSPATH"] = f"{jt400_path}:{os.environ.get('CLASSPATH', '')}"

class AS400ConnectorGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.conn = None
        self.result = None
        self.connection_error = None
        self.setStyleSheet("""
            QMainWindow {
                background-color: #F0F4F8;
            }
            QLabel {
                color: #4A5568;
            }
            QLineEdit, QPlainTextEdit {
                background-color: #EDF2F7;
                color: #4A5568;
                border: 1px solid #CBD5E0;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton {
                background-color: #63B3ED;
                color: #FFFFFF;
                border: none;
                border-radius: 5px;
                padding: 8px 15px;
            }
            QPushButton:hover {
                background-color: #4299E1;
            }
            QPushButton:disabled {
                background-color: #A0AEC0;
            }
            QTableWidget {
                background-color: #EDF2F7;
                color: #4A5568;
                gridline-color: #CBD5E0;
            }
            QTableWidget::item:selected {
                background-color: #BEE3F8;
            }
            QHeaderView::section {
                background-color: #E2E8F0;
                color: #4A5568;
                border: 1px solid #CBD5E0;
            }
            QMessageBox {
                background-color: #F0F4F8;
                color: #4A5568;
            }
            QMessageBox QLabel {
                color: #4A5568;
            }
            QMessageBox QPushButton {
                background-color: #63B3ED;
                color: #FFFFFF;
                border: none;
                border-radius: 5px;
                padding: 5px 10px;
            }
        """)

    def initUI(self):
        self.setWindowTitle('DB400 查詢工具')
        self.setGeometry(300, 300, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        title_label = QLabel('DB400 查詢工具')
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setFont(QFont('Arial', 24, QFont.Weight.Bold))
        title_label.setStyleSheet("color: #4299E1; margin: 10px 0;")
        layout.addWidget(title_label)

        def add_separator():
            line = QFrame()
            line.setFrameShape(QFrame.Shape.HLine)
            line.setFrameShadow(QFrame.Shadow.Sunken)
            line.setStyleSheet("background-color: #CBD5E0;")
            layout.addWidget(line)

        add_separator()

        # 輸入欄位（在同一行）
        input_layout = QHBoxLayout()
        self.host_input = QLineEdit()
        self.user_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        input_layout.addWidget(QLabel('系統名稱:'))
        input_layout.addWidget(self.host_input)
        input_layout.addWidget(QLabel('用戶名:'))
        input_layout.addWidget(self.user_input)
        input_layout.addWidget(QLabel('密碼:'))
        input_layout.addWidget(self.password_input)
        layout.addLayout(input_layout)

        add_separator()

        # 連接和中斷連接按鈕（在同一行）
        button_layout = QHBoxLayout()
        self.connect_button = QPushButton('連接')
        self.connect_button.clicked.connect(self.connect_to_as400)
        button_layout.addWidget(self.connect_button)

        self.disconnect_button = QPushButton('中斷連接')
        self.disconnect_button.clicked.connect(self.disconnect_from_as400)
        self.disconnect_button.setEnabled(False)
        button_layout.addWidget(self.disconnect_button)
        layout.addLayout(button_layout)

        add_separator()

        self.query_input = QPlainTextEdit()
        self.query_input.setPlaceholderText("在此輸入SQL查詢...")
        self.query_input.setStyleSheet("font-family: Consolas, Monaco, monospace; font-size: 12px;")
        layout.addWidget(self.query_input)

        self.execute_button = QPushButton('執行查詢')
        self.execute_button.clicked.connect(self.execute_query)
        self.execute_button.setEnabled(False)
        layout.addWidget(self.execute_button)

        add_separator()

        self.result_display = QTableWidget()
        layout.addWidget(self.result_display)

        self.export_button = QPushButton('匯出結果')
        self.export_button.clicked.connect(self.export_results)
        self.export_button.setEnabled(False)
        layout.addWidget(self.export_button)

        self.statusBar().showMessage("準備就緒")
        self.statusBar().setStyleSheet("color: #4A5568; background-color: #E2E8F0;")

        # 快捷鍵
        QShortcut(QKeySequence(Qt.Key.Key_Return), self, self.connect_to_as400)
        QShortcut(QKeySequence(Qt.Key.Key_Escape), self, self.disconnect_from_as400)
        QShortcut(QKeySequence("Ctrl+Return"), self, self.execute_query)

    def connect_to_as400(self):
        host = self.host_input.text()
        user = self.user_input.text()
        password = self.password_input.text()

        try:
            jclassname = "com.ibm.as400.access.AS400JDBCDriver"
            url = f"jdbc:as400://{host}"
            self.conn = jaydebeapi.connect(jclassname, url, [user, password], jt400_path)
            QMessageBox.information(self, "連接成功", "已成功連接到IBM i系統")
            self.execute_button.setEnabled(True)
            self.connect_button.setEnabled(False)
            self.disconnect_button.setEnabled(True)
            self.statusBar().showMessage(f"已連接到 {host}")
        except Exception as e:
            self.connection_error = str(e)
            QMessageBox.critical(self, "連接失敗", f"無法連接到IBM i系統: {self.connection_error}")

    def disconnect_from_as400(self):
        if self.conn:
            try:
                self.conn.close()
                QMessageBox.information(self, "斷開連接", "已成功斷開與IBM i系統的連接")
                self.execute_button.setEnabled(False)
                self.connect_button.setEnabled(True)
                self.disconnect_button.setEnabled(False)
                self.export_button.setEnabled(False)
                self.statusBar().showMessage("已斷開連接")
                self.conn = None
                self.result = None
            except Exception as e:
                QMessageBox.warning(self, "斷開連接警告", f"斷開連接時發生錯誤：{str(e)}")
        else:
            QMessageBox.warning(self, "無連接", "當前沒有活動中的連接")

    def execute_query(self):
        if not self.conn:
            QMessageBox.warning(self, "無連接", "請先連接到數據庫")
            return

        query = self.query_input.toPlainText()
        if not query:
            QMessageBox.warning(self, "查詢為空", "請輸入SQL查詢")
            return

        try:
            with self.conn.cursor() as cursor:
                cursor.execute(query)
                if cursor.description:
                    columns = [desc[0] for desc in cursor.description]
                    self.result = cursor.fetchall()
                    self.result_display.setColumnCount(len(columns))
                    self.result_display.setRowCount(len(self.result))
                    self.result_display.setHorizontalHeaderLabels(columns)

                    for row, data in enumerate(self.result):
                        for col, value in enumerate(data):
                            self.result_display.setItem(row, col, QTableWidgetItem(str(value)))

                    self.result_display.resizeColumnsToContents()
                    self.statusBar().showMessage(f"查詢成功，返回 {len(self.result)} 行結果")
                    self.export_button.setEnabled(True)
                else:
                    self.result = None
                    self.statusBar().showMessage("執行成功，但沒有返回結果")
                    self.export_button.setEnabled(False)
        except Exception as e:
            QMessageBox.critical(self, "查詢失敗", f"執行查詢時發生錯誤: {str(e)}")
            self.statusBar().showMessage("查詢執行失敗")

    def export_results(self):
        if not self.result:
            QMessageBox.warning(self, "無結果", "沒有可匯出的查詢結果")
            return

        file_path, _ = QFileDialog.getSaveFileName(self, "保存Excel文件", "", "Excel Files (*.xlsx)")
        if not file_path:
            return

        try:
            wb = Workbook()
            ws = wb.create_sheet("查詢結果")
            
            columns = [self.result_display.horizontalHeaderItem(i).text() for i in range(self.result_display.columnCount())]
            ws.append(columns)

            for row in self.result:
                ws.append(row)

            wb.save(file_path)
            QMessageBox.information(self, "匯出成功", f"查詢結果已成功匯出到:\n{file_path}")
        except Exception as e:
            QMessageBox.critical(self, "匯出失敗", f"匯出結果時發生錯誤: {str(e)}")

    def closeEvent(self, event):
        if self.conn:
            self.conn.close()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # 使用 Fusion 風格以獲得更現代的外觀
    ex = AS400ConnectorGUI()
    ex.show()
    sys.exit(app.exec())