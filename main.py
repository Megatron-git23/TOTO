import pygame
import speech_recognition as sr
import pyttsx3
import threading

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Talking Tom (Python)")

cat_idle = pygame.image.load("cat_idle.png")   
cat_talking = pygame.image.load("cat_talking.png")  
cat_idle = pygame.transform.scale(cat_idle, (400, 400))
cat_talking = pygame.transform.scale(cat_talking, (400, 400))

engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("volume", 1)

r = sr.Recognizer()

def tom_repeat():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        try:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, timeout=5)
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            
            threading.Thread(target=speak, args=(text,)).start()
        except Exception as e:
            print("Could not recognize speech.", e)

def speak(text):
    
    global talking
    talking = True
    engine.say(text)
    engine.runAndWait()
    talking = False

running = True
talking = False
clock = pygame.time.Clock()

while running:
    screen.fill((200, 220, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                threading.Thread(target=tom_repeat).start()

    
    if talking:
        screen.blit(cat_talking, (100, 100))
    else:
        screen.blit(cat_idle, (100, 100))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
