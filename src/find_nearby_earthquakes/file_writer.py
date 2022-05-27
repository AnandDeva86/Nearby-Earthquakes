import os
import logging

# -----------------------------------------------------------
# File name: file_writer.py
# Author: Anand Devarajan
# Date created: 25/05/2022
# Date last modified: 25/05/2022
# Python Version: >3.9
# -----------------------------------------------------------


logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


class FileWriter:
    def write_text(self, data, path="./data"):
        isExist = os.path.exists(path)
        if not isExist:
            os.makedirs(path)
        file_path = os.path.join(path, 'Result.txt')

        with open(file_path, 'w') as file:
            file.write('\n'.join(data))
        file.close()
