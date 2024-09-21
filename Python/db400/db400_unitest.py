import unittest
from unittest.mock import MagicMock, patch
from PySide6.QtWidgets import QApplication
from db400.db4001 import AS400ConnectorGUI

class TestAS400ConnectorGUI(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # 創建 QApplication 實例
        cls.app = QApplication([])
    
    def setUp(self):
        # 在每個測試方法之前創建 GUI 實例
        self.gui = AS400ConnectorGUI()
    
    def test_init(self):
        # 測試 GUI 初始化
        self.assertIsNotNone(self.gui)
        self.assertEqual(self.gui.windowTitle(), 'DB400 查詢工具')
    
    @patch('db400.db4001.jaydebeapi.connect')
    def test_connect_to_as400_success(self, mock_connect):
        # 測試成功連接到 AS400
        self.gui.host_input.setText('test_host')
        self.gui.user_input.setText('test_user')
        self.gui.password_input.setText('test_password')
        
        self.gui.connect_to_as400()
        
        mock_connect.assert_called_once()
        self.assertTrue(self.gui.execute_button.isEnabled())
        self.assertFalse(self.gui.connect_button.isEnabled())
        self.assertTrue(self.gui.disconnect_button.isEnabled())
    
    @patch('db4001.jaydebeapi.connect', side_effect=Exception('Connection error'))
    def test_connect_to_as400_failure(self, mock_connect):
        try:
            self.gui.host_input.setText('test_host')
            self.gui.user_input.setText('test_user')
            self.gui.password_input.setText('test_password')
            
            self.gui.connect_to_as400()
            
            mock_connect.assert_called_once()
            self.assertFalse(self.gui.execute_button.isEnabled())
            self.assertTrue(self.gui.connect_button.isEnabled())
            self.assertFalse(self.gui.disconnect_button.isEnabled())
        except Exception as e:
            print(f"Unexpected error in test_connect_to_as400_failure: {e}")
            raise
    
    # 可以添加更多測試方法，例如：
    # test_disconnect_from_as400
    # test_execute_query
    # test_export_results
    
    @classmethod
    def tearDownClass(cls):
        # 清理 QApplication 實例
        cls.app.quit()

if __name__ == '__main__':
    unittest.main()
