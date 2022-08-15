import qrcode

qrData = 'www.naver.com'
qrImg = qrcode.make(qrData)

savePath = '4 - QR코드 생성기\\' + qrData + '.png'
qrImg.save(savePath)