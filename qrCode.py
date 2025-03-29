import qrcode
import pygame

class QrCode():
    def __init__(self):
        self.url = "https://retronova.fr"

        qr = qrcode.QRCode(
            version=1, 
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        qr.add_data(self.url)
        qr.make(fit=True)

        self.img = qr.make_image(fill='black', back_color='white')
        self.img.save("qr_code_retronova.png")
        
        self.size = 326
        
        self.image = pygame.image.load("qr_code_retronova.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
    
    def show(self, screen):
        screen.blit(self.image, (1301, 719))
        
    def run(self, screen):
        self.show(screen)