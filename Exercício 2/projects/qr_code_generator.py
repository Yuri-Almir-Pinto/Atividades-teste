import qrcode as qrcode

def create_qr_code(string: str) -> None:
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4,
    )

    qr.add_data(string)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("./artifacts/url_qrcode.png")