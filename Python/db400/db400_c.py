import os
import sys
import jaydebeapi
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                               QLabel, QLineEdit, QPushButton, QPlainTextEdit, 
                               QMessageBox, QTableWidget, QTableWidgetItem,
                               QMainWindow, QFileDialog, QFrame, QComboBox, QStyledItemDelegate)
from PySide6.QtGui import QFont, QShortcut, QKeySequence, QColor
from PySide6.QtCore import Qt, QCoreApplication
from openpyxl import Workbook

# 確保程序完全退出
def force_quit():
    QCoreApplication.quit()
    sys.exit(0)

jt400_path = "/Users/clark/Desktop/DDSC/Clark文件/13-JavaCode/jt400.jar"
if not os.path.exists(jt400_path):
    print(f"錯誤：jt400.jar 文件未找到：{jt400_path}")
    sys.exit(1)

java_home = "/Library/Java/JavaVirtualMachines/jdk-22.jdk/Contents/Home"
os.environ["JAVA_HOME"] = java_home
os.environ["PATH"] = f"{java_home}/bin:{os.environ.get('PATH', '')}"
os.environ["CLASSPATH"] = f"{jt400_path}:{os.environ.get('CLASSPATH', '')}"

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
        """)

    def initUI(self):
        self.setWindowTitle('DB400 查詢工具')
        self.setGeometry(300, 300, 800, 600)

        # 創建中央窗口部件
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

        # 添加預定義查詢下拉選單
        self.query_combo = QComboBox()
        self.query_combo.setItemDelegate(CustomItemDelegate())
        self.query_combo.addItem("選擇預定義查詢...")
        self.add_predefined_queries(self.query_combo)
        self.query_combo.currentIndexChanged.connect(self.load_predefined_query)
        layout.addWidget(self.query_combo)

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

    def add_predefined_queries(self, combo):
        queries = {
            "1.Backup and Recovery Services": [
                ("  #磁帶櫃資訊", "SELECT * FROM QSYS2.MEDIA_LIBRARY_INFO"),
                ("  #磁帶資訊", "SELECT * FROM QSYS2.TAPE_CARTRIDGE_INFO WHERE STATUS <> 'AVAILABLE'"),
                ("  #儲存檔案的備份物件數量", "SELECT SAVE_FILE_LIBRARY, SAVE_FILE, SAVE_TIMESTAMP, OBJECTS_SAVED FROM QSYS2.SAVE_FILE_INFO  WHERE SAVE_FILE_LIBRARY = 'QGPL' AND SAVE_FILE = 'IQUERY'"),
            ],
            "2.Communication Services": [
                ("  #特定port連線資訊", "SELECT * FROM QSYS2.NETSTAT_INFO WHERE LOCAL_PORT = '23'"),
                ("  #特定lind連線資訊", "SELECT * FROM QSYS2.NETSTAT_INTERFACE_INFO WHERE LINE_DESCRIPTION = 'ETHLINE'"),
            ],
            "3.Configuration Services": [
                ("  #硬體資訊", "SELECT \n    text_description AS \"Text\", resource_category AS \"Category\", resource_name AS \"Name\",\n    status AS \"Status\", device_type AS \"Type\", device_model AS \"Model\", serial_number AS \"S/N\",\n    location_code AS \"Location\" \nFROM QSYS2.HARDWARE_RESOURCE_INFO"),
            ],
            "4.IFS Services": [
                ("  #查詢特定副檔名或檔案", "SELECT CAST(PATH_NAME AS VARCHAR(1000)) AS \"PATH_NAME\", OBJECT_TYPE, DATA_SIZE, OBJECT_OWNER\n    FROM TABLE (QSYS2.IFS_OBJECT_STATISTICS(START_PATH_NAME => '/QSYS.LIB/CLARK.LIB', \n                                            SUBTREE_DIRECTORIES => 'YES'))\n    WHERE PATH_NAME LIKE '%.PGM'"),
            ],
            "5.Journal Services": [
                ("  #User對物件的稽核軌跡", "SELECT journal_code, journal_entry_type, object, object_type, X.*\n    FROM TABLE(QSYS2.Display_Journal(\n        JOURNAL_NAME => 'QAUDJRN',\n        JOURNAL_LIBRARY => '*LIBL',\n        OBJECT_LIBRARY => '*TEST', OBJECT_NAME => '*STRJP',\n        OBJECT_OBJTYPE => '*FILE', OBJECT_MEMBER => '*FIRST'\n    )) AS X\n    WHERE journal_entry_type IN ('DL', 'PT', 'PX', 'UP') AND CURRENT_USER = 'CLARK'\n    ORDER BY entry_timestamp DESC"),
                ("  #物件掛載的Journal清單", "SELECT * FROM QSYS2.JOURNALED_OBJECTS WHERE JOURNAL_LIBRARY = '*LIBL' AND JOURNAL_NAME = 'QAUDJRN'"),
            ],
            "6.Librarian Services": [
                ("  #Library內指定類型的物件", "SELECT * FROM TABLE (QSYS2.OBJECT_STATISTICS('*ALLUSR','*DTAARA','*ALLSIMPLE')) X"),
                ("  #修改過的預設指令", "SELECT * FROM TABLE(QSYS2.OBJECT_STATISTICS('QSYS', '*CMD'))\n    WHERE APAR_ID = 'CHGDFT'"),
            ],
            "7.Message Handling Services": [
                ("  #Log進階查詢", "SELECT MESSAGE_SECOND_LEVEL_TEXT, X.* FROM TABLE(QSYS2.HISTORY_LOG_INFO(\n    Start_time => current_date -2 day)) X\n  WHERE SEVERITY >= '30'"),
                ("  #指定Job的輸入軌跡", "SELECT message_text as \"Message Text\"\n FROM TABLE(QSYS2.JOBLOG_INFO('141254/CLARK/LIONA0')) AS X\nWHERE message_type = 'REQUEST'"),
                ("  #Message Queue進階查詢", "SELECT MESSAGE_TEXT, MESSAGE_ID, SEVERITY, FROM_JOB, MESSAGE_TIMESTAMP, MESSAGE_SECOND_LEVEL_TEXT \n   FROM QSYS2.MESSAGE_QUEUE_INFO\n   WHERE MESSAGE_QUEUE_NAME = 'QSYSOPR' AND SEVERITY > 10"),
            ],
            "8.Product Services": [
                ("  #授權程式到期日查詢", "SELECT LICENSE_EXPIRATION , X.* FROM QSYS2.LICENSE_INFO X\nWHERE license_expiration <= CURRENT_DATE + 5 YEAR"),
                ("  #檢查安裝的授權程式", "SELECT * FROM TABLE(SYSTOOLS.CHECK_PRODUCT_OPTIONS( ))"),
            ],
            "9.PTF Services": [
                ("  #PTF Group狀態", "SELECT * FROM QSYS2.GROUP_PTF_INFO"),
                ("  #查詢需IPL的PTF", "SELECT PTF_IDENTIFIER, PTF_IPL_ACTION, PTF_PRODUCT_ID\n  FROM QSYS2.PTF_INFO \n  WHERE PTF_IPL_ACTION <> 'NONE'"),
                ("  #PTF的可升級資訊", "SELECT * FROM SYSTOOLS.GROUP_PTF_CURRENCY \n   ORDER BY PTF_GROUP_LEVEL_AVAILABLE - PTF_GROUP_LEVEL_INSTALLED DESC"),
            ],
            "10.Security Services": [
                ("  #查詢憑證到期日", "SELECT * FROM TABLE(QSYS2.CERTIFICATE_INFO(CERTIFICATE_STORE_PASSWORD=> 'password'))\n   WHERE VALIDITY_END < CURRENT DATE + 1 MONTH"),
                ("  #檢查密碼是否合規", "SELECT * FROM TABLE(QSYS2.CHECK_PASSWORD('amIvalid?'))\n-- SELECT * FROM TABLE(QSYS2.CHECK_PASSWORD('P@ssw0rd'))"),
                ("  #列出*PUBLIC權限不為*EXCLUDE的物件", "SELECT *\n   FROM QSYS2.OBJECT_PRIVILEGES\n   WHERE SYSTEM_OBJECT_SCHEMA = 'CLARK' AND\n         OBJECT_TYPE = '*FILE' AND\n         AUTHORIZATION_NAME = '*PUBLIC' AND\n         OBJECT_AUTHORITY <> '*EXCLUDE'"),
                ("  #列出有登入失敗的使用者", "SELECT * FROM QSYS2.USER_INFO\n  WHERE SIGN_ON_ATTEMPTS_NOT_VALID > 0"),
                ("  #列出含有特殊權限的使用者", "SELECT * FROM SYSTOOLS.SPECIAL_AUTHORITY_DATA_MART\nORDER BY AUTHORIZATION_NAME"),
                ("  #列出Library中所有File的欄位資訊", "SELECT * FROM QSYS2.SYSCOLUMNS2\nWHERE TABLE_SCHEMA = 'TEST'"),
            ],
            "11.Spool Services": [
                ("  #查詢使用者報表", "SELECT * \n  FROM TABLE(QSYS2.OUTPUT_QUEUE_ENTRIES('*LIBL', 'QPRINT', 'NO')) \n  WHERE USER_NAME = 'CLARK'\n ORDER BY SIZE DESC\n FETCH FIRST 100 ROWS ONLY"),
                ("  #檢視報表內容", "SELECT * FROM TABLE(SYSTOOLS.SPOOLED_FILE_DATA(\n                             JOB_NAME          =>'143448/CLARK/RPGPRT', \n                             SPOOLED_FILE_NAME =>'TSTPRTF'))\nORDER BY ORDINAL_POSITION"),
            ],
        }
        
        for category, items in queries.items():
            combo.addItem(category, userData="category")
            for name, query in items:
                combo.addItem(f"  {name}", userData=query)

    def load_predefined_query(self, index):
        query = self.query_combo.itemData(index)
        if query and query != "category":
            self.query_input.setPlainText(query)

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
            QMessageBox.warning(self, "無連接", "當前沒有活動的連接")

    def execute_query(self):
        query = self.query_input.toPlainText()
        if not query:
            QMessageBox.warning(self, "查詢為空", "請輸入SQL查詢")
            return

        try:
            with self.conn.cursor() as cursor:
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