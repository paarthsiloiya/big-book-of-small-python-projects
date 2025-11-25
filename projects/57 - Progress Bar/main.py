import random, time

BAR = chr(9608)

def main():
    bytes_downloaded = 0
    download_size = 4096
    
    while bytes_downloaded < download_size:
        bytes_downloaded += random.randint(0, 100)
        if bytes_downloaded > download_size:
            bytes_downloaded = download_size
            
        bar_str = get_progress_bar(bytes_downloaded, download_size)
        print(bar_str, end='', flush=True)
        time.sleep(0.2)
        print('\b' * len(bar_str), end='', flush=True)

def get_progress_bar(progress, total, bar_width=40):
    progress = max(0, min(progress, total))
    filled_length = int(bar_width * progress / total)
    bar = BAR * filled_length + ' ' * (bar_width - filled_length)
    percent = round(100.0 * progress / total, 1)
    return f'[{bar}] {percent}% {progress}/{total}'

if __name__ == '__main__':
    main()
