import sys, subprocess, shutil, os

try:
    import pyttsx3
except Exception:
    pyttsx3 = None

engine = None
rate = None
voice_choice = None
volume = None

if pyttsx3:
    engine = pyttsx3.init()

def list_voices():
    if not engine:
        print('No pyttsx3 available to list voices.')
        return
    v = engine.getProperty('voices')
    for i, voice in enumerate(v, 1):
        print(i, '-', voice.name)

def speak_text(text):
    if engine:
        if rate is not None:
            engine.setProperty('rate', rate)
        if volume is not None:
            engine.setProperty('volume', volume)
        if voice_choice:
            vs = engine.getProperty('voices')
            for vv in vs:
                if voice_choice.lower() in vv.name.lower() or voice_choice.lower() in vv.id.lower():
                    engine.setProperty('voice', vv.id)
                    break
        engine.say(text)
        engine.runAndWait()
        return
    if sys.platform == 'darwin' and shutil.which('say'):
        subprocess.run(['say', text])
        return
    if shutil.which('espeak'):
        subprocess.run(['espeak', text])
        return
    print('No TTS backend found. Install pyttsx3 or a system TTS (say/espeak).')

def save_audio(text, filename):
    if not engine:
        print('Saving audio requires pyttsx3.')
        return
    engine.save_to_file(text, filename)
    engine.runAndWait()
    print('Saved to', filename)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    global rate, voice_choice, volume
    clear()
    print('Text To Speech Talker')
    print('Type text to speak or commands: VOICES, RATE n, VOICE name, VOL 0.0-1.0, SAVE file.wav, QUIT')

    while True:
        try:
            cmd = input('> ').strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not cmd:
            continue
        up = cmd.upper()
        if up == 'QUIT':
            break
        if up == 'VOICES':
            list_voices()
            continue
        if up.startswith('RATE '):
            try:
                rate = int(cmd.split(maxsplit=1)[1])
                print('Rate set to', rate)
            except Exception:
                print('Invalid rate')
            continue
        if up.startswith('VOL ') or up.startswith('VOLUME '):
            try:
                volume = float(cmd.split(maxsplit=1)[1])
                if not 0.0 <= volume <= 1.0:
                    raise ValueError
                print('Volume set to', volume)
            except Exception:
                print('Volume must be 0.0–1.0')
            continue
        if up.startswith('VOICE '):
            voice_choice = cmd.split(maxsplit=1)[1]
            print('Voice choice set to', voice_choice)
            continue
        if up.startswith('SAVE '):
            filename = cmd.split(maxsplit=1)[1]
            save_audio(filename=filename, text=filename) if False else save_audio(text=cmd.split(maxsplit=1)[1], filename=filename)
            continue
        speak_text(cmd)

if __name__ == '__main__':
    main()
