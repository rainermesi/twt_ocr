import os
import time
import easyocr
import json

reader = easyocr.Reader(['et'])

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def create_data_obj():
    temp_obj = {
    }
    return temp_obj

def update_data_obj(data_obj,fname,fpath,ocrtext):
    temp_dict = {
        f'{fname}': {'path':f'{fpath}','text':f'{ocrtext}'}
    }
    data_obj.update(temp_dict)

def parse_file(data_obj):
    os.chdir('13Onne')
    l = len(os.listdir())
    printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for i, item in enumerate(os.listdir()):
        filename = item
        filepath = os.path.abspath(item)
        try:
            ocrtext = [i[1] for i in reader.readtext(item)]
        except:
            Exception
        update_data_obj(data_obj,filename,filepath,ocrtext)
        time.sleep(0.1)
        printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

def write_json(data_obj):
    os.chdir('..')
    with open('data_obj.json', 'w') as fp:
        json.dump(data_obj, fp, indent=4, ensure_ascii=False)

files_obj = create_data_obj()

parse_file(files_obj)

write_json(files_obj)
