import qrcode
from PIL import Image
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

def genQr(url):   
    basewidth = 130
    logo = Image.open('logo.png')
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize))
    QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, border=1)
    QRcode.add_data(url)
    QRcode.make()
    QRimg = QRcode.make_image(image_factory= StyledPilImage, module_drawer=RoundedModuleDrawer(),
    color_mask=RadialGradiantColorMask(back_color = (255,255,255), center_color = (255, 165, 0), edge_color = (138,43,226)))
    pos = ((QRimg.size[0] - logo.size[0]) // 2, (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)
    return QRimg
