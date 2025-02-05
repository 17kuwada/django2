# QRコードライブラリ
# ※ Pillowライブラリを使う
# pip install qrcode

import qrcode
import qrcode.constants
# **簡易版
# im = qrcode.make('穴吹ビジネス専門学校')
# im.save('qrcode.png')

# **詳細版
qr = qrcode.QRCode(
    # QRコードの面積 1~40、1が一番面積が小さい
    version=12,
    # ERROR_CORRECT_L   約7%の破損に対応
    # ERROR_CORRECT_M   約15%の破損に対応
    # ERROR_CORRECT_Q   約25%の破損に対応
    # ERROR_CORRECT_H   約30%の破損に対応
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=2,
    border=8
)
qr.add_data('穴吹ビジネス専門学校')
qr.make()
im = qr.make_image()
im.save('qrcode.png')