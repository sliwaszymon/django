import base64
from io import BytesIO

import qrcode


def create_qr(full_short_link):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(full_short_link)
    qr.make(fit=True)
    return qr.make_image(fill_color="black", back_color="white")


def qr_to_base64(qr):
    buffered = BytesIO()
    qr.save(buffered)
    return base64.b64encode(buffered.getvalue()).decode('utf-8')