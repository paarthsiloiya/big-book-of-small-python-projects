# Text To Speech Talker

A small terminal text-to-speech utility that uses `pyttsx3` when available
and falls back to system tools (`say` on macOS or `espeak` on Linux).

How to use

1.  Run `python main.py`.
2.  Type any text and press Enter to speak it.
3.  Special commands:
    - `VOICES` — list available voices (requires `pyttsx3`).
    - `RATE n` — set speech rate (integer, `pyttsx3` only).
    - `VOL x` — set volume between `0.0` and `1.0`.
    - `VOICE name` — pick a voice by name (partial matches allowed).
    - `SAVE file.wav` — save the last provided text to a WAV file (`pyttsx3`).
    - `QUIT` — exit.

Notes

- Install `pyttsx3` for the best cross-platform experience: `pip install pyttsx3`.
- On macOS the `say` command is used if `pyttsx3` is not installed.
- On Linux install `espeak` for a fallback TTS: `sudo apt install espeak`.
