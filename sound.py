import pygame

class Sound():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Sound, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        pygame.mixer.init()
        self.music = None
        self.sounds = {}
        self._initialized = True

    def load_music(self, file_path):
        pygame.mixer.music.load(file_path)

    def play_music(self, loops=-1):
        pygame.mixer.music.play(loops)

    def stop_music(self):
        pygame.mixer.music.stop()

    def load_sound(self, name, file_path):
        self.sounds[name] = pygame.mixer.Sound(file_path)

    def play_sound(self, name, loops=0):
        if name in self.sounds:
            self.sounds[name].play(loops)

    def stop_sound(self, name):
        if name in self.sounds:
            self.sounds[name].stop()