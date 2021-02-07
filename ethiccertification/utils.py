import pyzbar.pyzbar as pyzbar
from django.core.files import File
from pdf2image import convert_from_path
import os

from ethiccertification.models import EthicItem


def attach_files():
    dir_path = 'c:/work/Project/SistemaAudit/garbage/'

    # look all files in folder
    for file in os.listdir(dir_path):
        # convert pdf to image
        images = convert_from_path(dir_path + file)
        # decode barcode from image
        barcode = decode(images[0])
        if barcode:
            item_id = int(barcode) - 1000000
            try:
                ethic_item = EthicItem.objects.get(id=item_id)
                f = open(dir_path + file, 'rb')
                my_file = File(f)
                ethic_item.questionnaire_file.save(file, my_file, save=True)
                f.close()
                os.remove(dir_path + file)
            except:
                print(Exception)


def decode(image):
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(image)

    # Print results
    # for obj in decodedObjects:
    #     print('Type : ', obj.type)
    #     print('Data : ', str(obj.data))

    return decodedObjects[0].data
