import os
import sys

# 添加以下行
os.environ["MESA_LOADER_DRIVER_OVERRIDE"] = "i965"
# 或者嘗試
# os.environ["LIBGL_ALWAYS_SOFTWARE"] = "1"

import jaydebeapi
from jpype import JClass
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                               QLabel, QLineEdit, QPushButton, QPlainTextEdit, 
                               QMessageBox, QTableWidget, QTableWidgetItem, QHeaderView,
                               QMainWindow, QStatusBar)
from PySide6.QtGui import QFont, QPalette, QColor, QKeySequence, QShortcut
from PySide6.QtCore import Qt

print("程序開始執行")

# 設置jt400.jar的路徑
jt400_path = "/root/SourceDoc/jt400-20.0.7.jar"

# 確保jt400.jar存在
if not os.path.exists(jt400_path):
    print(f"錯誤：jt400.jar 文件未找到：{jt400_path}")
    sys.exit(1)

# 設置JAVA_HOME環境變量
java_home = "/Library/Java/JavaVirtualMachines/jdk-22.jdk/Contents/Home"
os.environ["JAVA_HOME"] = java_home
os.environ["PATH"] = f"{java_home}/bin:{os.environ.get('PATH', '')}"
os.environ["CLASSPATH"] = f"{jt400_path}:{os.environ.get('CLASSPATH', '')}"

print(f"JAVA_HOME 設置為: {java_home}")
print(f"CLASSPATH 設置為: {os.environ['CLASSPATH']}")

class AS400ConnectorGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        print("初始化 AS400ConnectorGUI")
        self.initUI()
        self.conn = None

    def initUI(self):
        self.setWindowTitle('DB400 查詢工具')
        self.setGeometry(300, 300, 800, 600)
        
        # 創建中心部件和佈局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 設置背景顏色
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(240, 240, 240))
        self.setPalette(palette)

        # 標題
        title_label = QLabel('DB400 查詢工具')
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setFont(QFont('Arial', 18, QFont.Weight.Bold))
        layout.addWidget(title_label)

        # 輸入欄位
        for field in ['系統名稱', '用戶名', '密碼']:
            hbox = QHBoxLayout()
            label = QLabel(field)
            label.setFont(QFont('Arial', 12))
            hbox.addWidget(label)
            line_edit = QLineEdit()
            line_edit.setObjectName(field)
            if field == '密碼':
                line_edit.setEchoMode(QLineEdit.EchoMode.Password)
            line_edit.returnPressed.connect(self.connect_to_as400)
            hbox.addWidget(line_edit)
            layout.addLayout(hbox)

        # 連接和中斷連接按鈕
        button_layout = QHBoxLayout()
        self.connect_button = QPushButton('連接')
        self.connect_button.setFont(QFont('Arial', 12))
        self.connect_button.clicked.connect(self.connect_to_as400)
        button_layout.addWidget(self.connect_button)

        self.disconnect_button = QPushButton('中斷連接')
        self.disconnect_button.setFont(QFont('Arial', 12))
        self.disconnect_button.clicked.connect(self.disconnect_from_as400)
        self.disconnect_button.setEnabled(False)
        button_layout.addWidget(self.disconnect_button)
        layout.addLayout(button_layout)

        # SQL查詢輸入
        self.query_input = QPlainTextEdit()
        self.query_input.setPlaceholderText("在此輸入SQL查詢...")
        self.query_input.setMaximumHeight(100)
        layout.addWidget(self.query_input)

        # 執行查詢按鈕
        self.execute_button = QPushButton('執行查詢')
        self.execute_button.setFont(QFont('Arial', 12))
        self.execute_button.clicked.connect(self.execute_query)
        self.execute_button.setEnabled(False)
        layout.addWidget(self.execute_button)

        # 結果顯示
        self.result_display = QTableWidget()
        self.result_display.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        layout.addWidget(self.result_display)

        # 狀態欄
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("準備就緒")

        # 快捷鍵
        QShortcut(QKeySequence(Qt.Key.Key_Escape), self, self.disconnect_from_as400)
        QShortcut(QKeySequence("Ctrl+Return"), self, self.execute_query)

        # 設置全局字體
        font = QFont()
        font.setPointSize(14)  # 設置字體大小為14
        QApplication.setFont(font)

        print("UI 初始化完成")

    def connect_to_as400(self):
        print("嘗試連接到 AS400")
        host_input = self.findChild(QLineEdit, '系統名稱')
        if isinstance(host_input, QLineEdit):
            host = host_input.text()
        else:
            print("錯誤：未找到'系統名稱'輸入框或類型不正確")
            QMessageBox.critical(self, "錯誤", "未找到'系統名稱'輸入框或類型不正確")
            return
        
        user_input = self.findChild(QLineEdit, '用戶名')
        password_input = self.findChild(QLineEdit, '密碼')
        
        if isinstance(user_input, QLineEdit) and isinstance(password_input, QLineEdit):
            user = user_input.text()
            password = password_input.text()
        else:
            print("錯誤：未找到'用戶名'或'密碼'輸入框或類型不正確")
            QMessageBox.critical(self, "錯誤", "未找到'用戶名'或'密碼'輸入框或類型不正確")
            return
        
        try:
            jclassname = "com.ibm.as400.access.AS400JDBCDriver"
            url = f"jdbc:as400://{host};prompt=false;translate binary=true;errors=full"
            self.conn = jaydebeapi.connect(jclassname, url, [user, password], jt400_path)
            print("成功連接到 AS400")
            QMessageBox.information(self, "連接成功", "已成功連接到AS400系統")
            self.execute_button.setEnabled(True)
            self.connect_button.setEnabled(False)
            self.disconnect_button.setEnabled(True)
            self.status_bar.showMessage(f"已連接 {host}")  # 修改這裡
        except Exception as e:
            print(f"連接失敗：{str(e)}")
            QMessageBox.critical(self, "連接失敗", f"無法連接到AS400系統: {str(e)}")

    def disconnect_from_as400(self):
        if self.conn:
            try:
                self.conn.close()
                print("已斷開與 AS400 的連接")
                QMessageBox.information(self, "斷開連接", "已成功斷開與AS400系統的連接")
                self.execute_button.setEnabled(False)
                self.connect_button.setEnabled(True)
                self.disconnect_button.setEnabled(False)
                self.status_bar.showMessage("已斷開連接")  # 修改這裡
                self.conn = None
            except Exception as e:
                print(f"斷開連接時發生錯誤：{str(e)}")
                QMessageBox.critical(self, "斷開連接失敗", f"斷開連接時發生錯誤: {str(e)}")
        else:
            print("沒有活動的連接")
            QMessageBox.warning(self, "無連接", "當前沒有活動的連接")

    def execute_query(self):
        print("執行查詢")
        if not self.conn:
            QMessageBox.warning(self, "無連接", "請先連接到數據庫")
            return
        
        query = self.query_input.toPlainText()
        if not query:
            print("查詢為空")
            QMessageBox.warning(self, "查詢為空", "請輸入SQL查詢")
            return

        try:
            with self.conn.cursor() as cursor:
                cursor.execute(query)
                if cursor.description:
                    columns = [desc[0] for desc in cursor.description]
                    result = cursor.fetchall()
                else:
                    columns = []
                    result = []
                
                # 設置表格
                self.result_display.setColumnCount(len(columns))
                self.result_display.setRowCount(len(result))
                self.result_display.setHorizontalHeaderLabels(columns)

                # 填充數據
                for row, data in enumerate(result):
                    for col, value in enumerate(data):
                        item = QTableWidgetItem(str(value))
                        self.result_display.setItem(row, col, item)

                # 調整列寬以適應內容
                self.result_display.resizeColumnsToContents()

                print("查詢執行成功")
                self.status_bar.showMessage(f"查詢成功，返回 {len(result)} 行結果")  # 修改這裡
        except Exception as e:
            print(f"查詢執行失敗：{str(e)}")
            QMessageBox.critical(self, "查詢失敗", f"執行查詢時發生錯誤: {str(e)}")
            self.status_bar.showMessage("查詢執行失敗")  # 修改這裡

    def closeEvent(self, event):
        if self.conn:
            self.conn.close()
            print("關閉數據庫連接")
        event.accept()

if __name__ == '__main__':
    print("進入主程序")
    app = QApplication(sys.argv)
    print("QApplication 創建成功")
    ex = AS400ConnectorGUI()
    print("AS400ConnectorGUI 實例創建成功")
    ex.show()
    print("顯示窗口")
    sys.exit(app.exec())