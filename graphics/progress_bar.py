import time
import random


BAR = chr(9608)


def main():
    print('Progress Bar Simulation!')
    print()

    bytes_downloaded = 0
    download_size = 4096

    while bytes_downloaded < download_size:
        bytes_downloaded += random.randint(1, 100)
        bar_str = get_progress_bar(bytes_downloaded, download_size)
        print(bar_str, end='', flush=True)

        time.sleep(0.2)
        print('\b' * len(bar_str), end='', flush=True)


def get_progress_bar(progress, total, bar_width=40):
    progress_bar = '[ '

    if progress > total:
        progress = total
    if progress < 0:
        progress = 0

    num_of_bars = int((progress / total) * bar_width)

    progress_bar += BAR * num_of_bars
    progress_bar += ' ]'
    percent_complete = round(progress / total * 100, 1)
    progress_bar += f' {percent_complete}%'
    progress_bar += f' {progress}/{total}'

    return progress_bar


if __name__ == '__main__':
    main()
