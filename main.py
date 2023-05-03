import qrcode

def getQrCode(url='https://www.google.com/', name='default'):
    qr = qrcode.make(data=url)
    qr.save(stream=f'{name}.png')

    return f'(QR code was created successfully, Open the{name}.png)'

def main():
    print(getQrCode(url='https://github.com/ArturGalstyan96', name='Github'))
    print(getQrCode(url='https://www.linkedin.com/in/artur-galstyan-77bb84164/', name='Linkedin'))


if __name__ == '__main__':
    main()