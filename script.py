from codecs import encode
import os
import easyocr
import json

reader = easyocr.Reader(['et'])

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
    for item in os.listdir():
        filename = item
        filepath = os.path.abspath(item)
        ocrtext = reader.readtext(item)
        update_data_obj(data_obj,filename,filepath,ocrtext)

def write_json(data_obj):
    os.chdir('..')
    with open('data_obj.json', 'w') as fp:
        json.dump(data_obj, fp, indent=4, ensure_ascii=False)

files_obj = create_data_obj()

parse_file(files_obj)

write_json(files_obj)
