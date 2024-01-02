import pyotp
import qrcode
import io
from PIL import Image

# 生成一個密鑰，此密鑰應與用戶帳戶關聯並安全保存
secret_key = pyotp.random_base32()

# 創建一個 TOTP 對象（基於時間的一次性密碼）
totp = pyotp.TOTP(secret_key)

# 生成 TOTP URI
totp_uri = totp.provisioning_uri("user@example.com", issuer_name="MyApp")

# 創建 QR 碼對象
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(totp_uri)
qr.make(fit=True)

# 創建 Pillow 圖像對象
img = qr.make_image(fill_color="black", back_color="white")

# 顯示 QR 碼圖片
img.show()

# 或者將 QR 碼圖片保存到文件
img.save("qrcode.png")

print("QR code generated and displayed. Secret key:", secret_key)
