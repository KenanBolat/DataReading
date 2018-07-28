import os
import csv

class Handle:

    def __init__(self):
        pass

    def get_file_tags(self, filename, delimiter="_"):
        file_tag = os.path.splitext(os.path.basename(filename))[0]
        date_tag = file_tag.split(delimiter)
        return date_tag

    def _check_file_exists(self, filename):
        return os.path.exists(filename)

    def write_data(self,filename):
        """if self._check_file_exists(filename):
            print "there is a::::::::::::::: ", filename
        else:
            print "there is not a ", filename
        """
