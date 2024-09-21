import os
import sys
import jaydebeapi
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                               QLabel, QLineEdit, QPushButton, QPlainTextEdit, 
                               QMessageBox, QTableWidget, QTableWidgetItem,
                               QMainWindow, QFileDialog, QFrame, QComboBox, QStyledItemDelegate,
                               QTabWidget, QDialog, QDialogButtonBox, QStackedWidget)
from PySide6.QtGui import QFont, QShortcut, QKeySequence, QColor
from PySide6.QtCore import Qt, QCoreApplication
from openpyxl import Workbook

# 確保程序完全退出
def force_quit():
    QCoreApplication.quit()
    sys.exit(0)

import os

# 使用 os.path.join 來創建路徑，以確保跨平台兼容性
import os
import sys
import platform

# 使用 os.path.join 來創建路徑，以確保跨平台兼容性
jt400_path = os.path.join("C:\\", "Users", "User", "Downloads", "jt400-20.0.7.jar")

# 檢查文件是否存在
if not os.path.exists(jt400_path):
    print(f"錯誤：jt400.jar 文件未找到：{jt400_path}")
    sys.exit(1)

java_home = "/Library/Java/JavaVirtualMachines/jdk-22.jdk/Contents/Home"
os.environ["JAVA_HOME"] = java_home
os.environ["PATH"] = f"{java_home}/bin:{os.environ.get('PATH', '')}"

# 根據操作系統選擇適當的分隔符
path_separator = ';' if platform.system() == 'Windows' else ':'

os.environ["CLASSPATH"] = f"{jt400_path}{path_separator}{os.environ.get('CLASSPATH', '')}"

class CustomItemDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        if index.data(Qt.UserRole) == "category":
            option.font.setBold(True)
            option.font.setPointSize(option.font.pointSize() + 2)
            option.backgroundBrush = QColor("#E2E8F0")
        super().paint(painter, option, index)

class AS400ConnectorGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connections = {}  # 存儲多個連接
        self.current_connection = None
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
            QComboBox {
                background-color: #EDF2F7;
                color: #4A5568;
                border: 1px solid #CBD5E0;
                border-radius: 5px;
                padding: 5px;
                min-height: 30px;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 15px;
                border-left-width: 1px;
                border-left-color: #CBD5E0;
                border-left-style: solid;
                border-top-right-radius: 3px;
                border-bottom-right-radius: 3px;
            }
            QComboBox::down-arrow {
                image: url(down_arrow.png);
            }
            QComboBox QAbstractItemView {
                background-color: #EDF2F7;
                color: #4A5568;
                selection-background-color: #BEE3F8;
            }
            QTabWidget::pane {
                border: 1px solid #CBD5E0;
                background: #F0F4F8;
            }
            QTabBar::tab {
                background: #E2E8F0;
                border: 1px solid #CBD5E0;
                padding: 5px;
            }
            QTabBar::tab:selected {
                background: #F0F4F8;
            }
        """)

    def initUI(self):
        self.setWindowTitle('DB400 多系統查詢工具')
        self.setGeometry(300, 300, 800, 600)

        # 創建中央窗口部件
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        # 創建堆疊小部件
        self.stacked_widget = QStackedWidget()
        self.main_layout.addWidget(self.stacked_widget)

        # 創建主界面和系統監控界面
        self.main_page = QWidget()
        self.system_monitor_page = SystemMonitorGUI(self)

        # 將兩個界面添加到堆疊小部件中
        self.stacked_widget.addWidget(self.main_page)
        self.stacked_widget.addWidget(self.system_monitor_page)

        # 設置主界面佈局
        self.setup_main_page()

        self.statusBar().showMessage("準備就緒")
        self.statusBar().setStyleSheet("color: #4A5568; background-color: #E2E8F0;")

        # 快捷鍵
        QShortcut(QKeySequence(Qt.Key.Key_Return), self, self.connect_to_as400)
        QShortcut(QKeySequence(Qt.Key.Key_Escape), self, self.show_disconnect_dialog)
        QShortcut(QKeySequence("Ctrl+Return"), self, self.execute_query)

    def setup_main_page(self):
        layout = QVBoxLayout(self.main_page)

        # 創建標題和切換按鈕的水平佈局
        title_layout = QHBoxLayout()
        
        title_label = QLabel('DB400 多系統查詢工具')
        title_label.setFont(QFont('Arial', 24, QFont.Weight.Bold))
        title_label.setStyleSheet("color: #4299E1; margin: 10px 0;")
        title_layout.addWidget(title_label)
        
        title_layout.addStretch(1)  # 添加彈性空間
        
        self.switch_button = QPushButton('切換到系統監控')
        self.switch_button.clicked.connect(self.switch_interface)
        self.switch_button.setFixedSize(120, 30)  # 設置按鈕大小
        title_layout.addWidget(self.switch_button)
        
        layout.addLayout(title_layout)

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

        # 將連接和中斷按鈕添加到輸入欄位後面
        self.connect_button = QPushButton('連接')
        self.connect_button.clicked.connect(self.connect_to_as400)
        input_layout.addWidget(self.connect_button)

        # 連接輸入欄位的textChanged信號到更新按鈕顏色的方法
        self.host_input.textChanged.connect(self.update_connect_button_color)
        self.user_input.textChanged.connect(self.update_connect_button_color)
        self.password_input.textChanged.connect(self.update_connect_button_color)

        self.disconnect_button = QPushButton('中斷')
        self.disconnect_button.clicked.connect(self.show_disconnect_dialog)
        self.disconnect_button.setEnabled(False)
        input_layout.addWidget(self.disconnect_button)

        layout.addLayout(input_layout)

        add_separator()

        # 添加系統選擇下拉選單
        self.system_combo = QComboBox()
        self.system_combo.addItem("選擇系統...")
        self.system_combo.currentIndexChanged.connect(self.switch_system)
        layout.addWidget(self.system_combo)

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

    def update_connect_button_color(self):
        if self.host_input.text() and self.user_input.text() and self.password_input.text():
            self.connect_button.setStyleSheet("""
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
            """)
        else:
            self.connect_button.setStyleSheet("""
                QPushButton {
                    background-color: #A0AEC0;
                    color: #FFFFFF;
                    border: none;
                    border-radius: 5px;
                    padding: 8px 15px;
                }
            """)

    def connect_to_as400(self):
        host = self.host_input.text()
        user = self.user_input.text()
        password = self.password_input.text()

        if not host or not user or not password:
            QMessageBox.warning(self, "輸入錯誤", "請填寫所有必要的連接信息")
            return

        try:
            connection_string = f"jdbc:as400://{host}"
            connection = jaydebeapi.connect("com.ibm.as400.access.AS400JDBCDriver",
                                            connection_string,
                                            [user, password],
                                            jt400_path)
            
            self.connections[host] = connection
            self.current_connection = host
            
            QMessageBox.information(self, "連接成功", f"已成功連接到IBM i系統: {host}")
            self.statusBar().showMessage(f"成功連接到 {host}")
            self.connect_button.setEnabled(False)
            self.disconnect_button.setEnabled(True)
            self.execute_button.setEnabled(True)
            
            if self.system_combo.findText(host) == -1:
                self.system_combo.addItem(host)
            self.system_combo.setCurrentText(host)
            
            # 清空輸入欄位
            self.host_input.clear()
            self.user_input.clear()
            self.password_input.clear()
            
            self.connection_error = None
        except Exception as e:
            self.connection_error = str(e)
            QMessageBox.critical(self, "連接失敗", f"無法連接到 {host}: {str(e)}")
            self.statusBar().showMessage("連接失敗")

    def show_disconnect_dialog(self):
        if not self.connections:
            QMessageBox.warning(self, "無連接", "當前沒有活動的連接")
            return

        dialog = QDialog(self)
        dialog.setWindowTitle("選擇要中斷的連接")
        layout = QVBoxLayout(dialog)

        combo = QComboBox()
        for host in self.connections.keys():
            combo.addItem(host)
        layout.addWidget(combo)

        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)
        layout.addWidget(button_box)

        shortcut = QShortcut(QKeySequence(Qt.Key.Key_Return), dialog)
        shortcut.activated.connect(dialog.accept)

        if dialog.exec() == QDialog.DialogCode.Accepted:
            selected_host = combo.currentText()
            self.disconnect_from_as400(selected_host)

    def disconnect_from_as400(self, host):
        if host in self.connections:
            try:
                self.connections[host].close()
                del self.connections[host]
                index = self.system_combo.findText(host)
                if index != -1:
                    self.system_combo.removeItem(index)
                QMessageBox.information(self, "斷開連接", f"已成功斷開與IBM i系統 {host} 的連接")
                
                if self.connections:
                    self.current_connection = next(iter(self.connections))
                    self.system_combo.setCurrentText(self.current_connection)
                    self.statusBar().showMessage(f"已切換到 {self.current_connection}")
                else:
                    self.current_connection = None
                    self.connect_button.setEnabled(True)
                    self.disconnect_button.setEnabled(False)
                    self.execute_button.setEnabled(False)
                    self.export_button.setEnabled(False)
                    self.statusBar().showMessage("已斷開所有連接")
            except Exception as e:
                QMessageBox.warning(self, "斷開連接警告", f"斷開連接時發生錯誤：{str(e)}")
        else:
            QMessageBox.warning(self, "無效的連接", f"找不到與 {host} 的連接")

    def switch_system(self, index):
        if index == 0:  # "選擇系統..." 項
            return
        
        selected_system = self.system_combo.currentText()
        if selected_system != self.current_connection:
            self.current_connection = selected_system
            self.statusBar().showMessage(f"已切換到系統: {selected_system}")

    def execute_query(self):
        if not self.current_connection:
            QMessageBox.warning(self, "無連接", "請先連接到一個系統")
            return

        query = self.query_input.toPlainText()
        if not query:
            QMessageBox.warning(self, "查詢為空", "請輸入SQL查詢")
            return

        try:
            with self.connections[self.current_connection].cursor() as cursor:
                cursor.execute(query)
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
            ws = wb.active
            
            columns = [self.result_display.horizontalHeaderItem(i).text() for i in range(self.result_display.columnCount())]
            ws.append(columns)

            for row in self.result:
                ws.append(row)

            wb.save(file_path)
            QMessageBox.information(self, "匯出成功", f"查詢結果已成功匯出到:\n{file_path}")
        except Exception as e:
            QMessageBox.critical(self, "匯出失敗", f"匯出結果時發生錯誤: {str(e)}")
    
    def switch_interface(self):
        if self.stacked_widget.currentWidget() == self.main_page:
            self.stacked_widget.setCurrentWidget(self.system_monitor_page)
            self.switch_button.setText('切換到主界面')
        else:
            self.stacked_widget.setCurrentWidget(self.main_page)
            self.switch_button.setText('切換到系統監控')

    def closeEvent(self, event):
        for conn in self.connections.values():
            conn.close()
        event.accept()
        
class SystemMonitorGUI(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent_gui = parent
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        # 創建標題和切換按鈕的水平佈局
        title_layout = QHBoxLayout()
        
        title_label = QLabel('系統監控')
        title_label.setFont(QFont('Arial', 24, QFont.Weight.Bold))
        title_label.setStyleSheet("color: #4299E1; margin: 10px 0;")
        title_layout.addWidget(title_label)
        
        title_layout.addStretch(1)  # 添加彈性空間
        
        switch_to_main_button = QPushButton('切換到主界面')
        switch_to_main_button.clicked.connect(self.parent_gui.switch_interface)
        switch_to_main_button.setFixedSize(120, 30)  # 設置按鈕大小
        title_layout.addWidget(switch_to_main_button)
        
        layout.addLayout(title_layout)

        # 創建選項卡窗口部件
        self.tab_widget = QTabWidget()
        layout.addWidget(self.tab_widget)

        # 添加 QSYSOPR 消息隊列監控選項卡
        self.add_qsysopr_tab(self.tab_widget)

        # 添加歷史日誌監控選項卡
        self.add_history_log_tab(self.tab_widget)

        # 添加作業日誌監控選項卡
        self.add_job_log_tab(self.tab_widget)

    def add_qsysopr_tab(self, tab_widget):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        query_button = QPushButton('查詢 QSYSOPR 消息')
        query_button.clicked.connect(self.query_qsysopr)
        layout.addWidget(query_button)

        self.qsysopr_result = QTableWidget()
        layout.addWidget(self.qsysopr_result)

        tab_widget.addTab(tab, 'QSYSOPR 消息')

    def query_qsysopr(self):
        query = """
        SELECT MESSAGE_TEXT, MESSAGE_ID, SEVERITY, FROM_JOB, MESSAGE_TIMESTAMP 
        FROM QSYS2.MESSAGE_QUEUE_INFO
        WHERE MESSAGE_QUEUE_NAME = 'QSYSOPR' AND SEVERITY > 10
        ORDER BY MESSAGE_TIMESTAMP DESC
        FETCH FIRST 100 ROWS ONLY
        """
        self.execute_query(query, self.qsysopr_result)

    def add_history_log_tab(self, tab_widget):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        query_button = QPushButton('查詢歷史日誌')
        query_button.clicked.connect(self.query_history_log)
        layout.addWidget(query_button)

        self.history_log_result = QTableWidget()
        layout.addWidget(self.history_log_result)

        tab_widget.addTab(tab, '歷史日誌')

    def query_history_log(self):
        query = """
        SELECT MESSAGE_TEXT, MESSAGE_ID, SEVERITY, FROM_JOB, MESSAGE_TIMESTAMP 
        FROM TABLE(QSYS2.HISTORY_LOG_INFO(
            START_TIME => CURRENT TIMESTAMP - 24 HOURS)) X
        WHERE SEVERITY >= '30'
        ORDER BY MESSAGE_TIMESTAMP DESC
        """
        self.execute_query(query, self.history_log_result)

    def add_job_log_tab(self, tab_widget):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        job_input = QLineEdit()
        job_input.setPlaceholderText('輸入作業名稱 (例如: 123456/USERNAME/JOBNAME)')
        job_input.textChanged.connect(lambda text: job_input.setText(text.upper()))  # 將輸入轉換為大寫
        layout.addWidget(job_input)

        query_button = QPushButton('查詢作業日誌')
        query_button.clicked.connect(lambda: self.query_job_log(job_input.text()))
        layout.addWidget(query_button)

        self.job_log_result = QTableWidget()
        layout.addWidget(self.job_log_result)

        tab_widget.addTab(tab, '作業日誌')

    def query_job_log(self, job_name):
        query = f"""
        SELECT MESSAGE_TEXT, MESSAGE_ID, MESSAGE_TYPE, MESSAGE_TIMESTAMP
        FROM TABLE(QSYS2.JOBLOG_INFO('{job_name}')) AS X
        ORDER BY MESSAGE_TIMESTAMP DESC
        FETCH FIRST 100 ROWS ONLY
        """
        self.execute_query(query, self.job_log_result)

    def execute_query(self, query, result_widget):
        if not self.parent_gui.current_connection:
            QMessageBox.warning(self, "無連接", "請先選擇一個連接的系統")
            return

        try:
            with self.parent_gui.connections[self.parent_gui.current_connection].cursor() as cursor:
                cursor.execute(query)
                columns = [desc[0] for desc in cursor.description]
                result = cursor.fetchall()
                
                result_widget.setColumnCount(len(columns))
                result_widget.setRowCount(len(result))
                result_widget.setHorizontalHeaderLabels(columns)

                for row, data in enumerate(result):
                    for col, value in enumerate(data):
                        result_widget.setItem(row, col, QTableWidgetItem(str(value)))

                result_widget.resizeColumnsToContents()
        except Exception as e:
            QMessageBox.critical(self, "查詢失敗", f"執行查詢時發生錯誤: {str(e)}")
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # 使用 Fusion 風格以獲得更現代的外觀
    ex = AS400ConnectorGUI()
    ex.show()
    sys.exit(app.exec())