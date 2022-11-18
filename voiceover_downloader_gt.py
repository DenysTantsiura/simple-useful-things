# import os
from pathlib import Path
import requests
from time import time

def voiceover_downloader_gt(words_file: str, folder: str = 'English', coding: str = 'utf-8', language: str = 'en') -> None:
    """
    Download the pronunciation of words (phrases) from a file in a certain language from 
    Google Translate (GT) and save in separate appropriate audio files (.mp3).
    Each line of the file is a separate word.

    Parameters:
        words_file(str): Path and file name with (Vocabulary words in certain language).
        folder(str): Directory(with path) for saving downloaded audio files. By default 'English'.
        coding(str): Encoding of the file of words. By default 'utf-8'.
        language(str): language marking in the request. By default 'en'. 
            (en - English; fr - French; es - Spanish;...)

    Returns:
        None
    """

    GOOGLE_WAY = 'https://translate.google.com/translate_tts?ie=UTF-&&client=tw-ob&tl='

    almost_complete_link = f'{GOOGLE_WAY}{language}&q='

    try:
        with open(words_file, 'r', encoding=coding) as file:
            words_base = {line.strip(): almost_complete_link + line.strip()
                          for line in file.readlines()}
    except IOError as pc_error:
        print(f'Sorry, but a hardware error has occurred'
              f'({pc_error}) while reading the file: {words_file}')
        return None
    except Exception as err:
        print('OOps: Something Else when trying read file of words.', err)
        return None
    # print(list(words_base.keys()))
    if words_base:
        for word, link_word in words_base.items():
            try:
                response = requests.get(link_word)
            except requests.exceptions.HTTPError as errh:
                print('Http Error:', errh)
                continue
            except requests.exceptions.ConnectionError as errc:
                print('Error Connecting:', errc)
                continue
            except requests.exceptions.Timeout as errt:
                print('Timeout Error:', errt)
                continue
            except requests.exceptions.RequestException as err:
                print('OOps: Something Else when trying download.', err)
                continue

            try:
                if folder:
                    # open(os.path.join(folder, f'{word}.mp3'), 'wb').write(response.content)
                    open(Path(folder).joinpath(f'{word}.mp3'), 'wb').write(response.content)
                else:
                    open(f'{word}.mp3', 'wb').write(response.content)
            except IOError as pc_error:
                print(f'Sorry, but a hardware error has occurred'
                      f'({pc_error}) while writing the file: {words_file}')
            except Exception as err:
                print('OOps: Something Else when trying save audio file \'{word}\'.', err)


start = time()
# print((time.time() - start_d)/60, ' m')
# print(voiceover_downloader_gt('EnList2.txt', ''))
print('By default:\nwords_file:\tNewWords.txt\nDownload folder:\tEnglish\nCoding:\tutf-8\nLanguage:\ten (English)')
words_file = input('Enter the file with words:\n')
if not words_file or not Path(words_file).exists():
    words_file = 'NewWords.txt'
Path('English').mkdir(exist_ok=True, parents=True)
voiceover_downloader_gt(words_file, 'English', 'utf-8', 'en') #  !? utf-8-sig
input(f'Done! {int((time() - start)//60)} m {int((time() - start)%60)} s\nPress Enter to exit...') # int? really?
