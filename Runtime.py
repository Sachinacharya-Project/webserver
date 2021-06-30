import pyttsx3, time, random
engine = pyttsx3.init()
engine.setProperty('voice', engine.getProperty('voices')[0])
def speak(text):
 engine.say(text)
 engine.runAndWait()
array = ['A', 'C', 'D', 'E', 'G']
while True:
 out = array[random.randint()*len(array)-1]
 speak(str(out))
 time.sleep(1)
