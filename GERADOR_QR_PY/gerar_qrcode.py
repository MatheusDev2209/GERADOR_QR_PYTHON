import qrcode

#link que você deseja gerar abaixo

imagem = qrcode.make("https://github.com/MatheusDev2209")

# *****comando para salvar arquivo jpg com o nome desejado***
imagem.save("primeir_qrcode.jpg")