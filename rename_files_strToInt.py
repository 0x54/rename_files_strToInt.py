#!/usr/bin/env python

"""rename_files_strToInt.py: It renames from 0 to N all the N files in the specified directory, sorting in natural order of the original files name. The output files are saved in the "orderedFiles" directory, created at the same path. The original files are not modified and all the permissions and metadata of renamed files are inalterated."""

__author__ = "Francesco Matarazzo aka Ti @0x54"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "ti.spamy.spam@gmail.it"
__status__ = "Gamma"
__date__ = "24/11/2014"


import re, os, sys, shutil

def human_sorting( l ):
	""" Compute "human" sorting """
	convert = lambda text: int(text) if text.isdigit() else text
	alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
	l.sort( key=alphanum_key )

    
if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        sys.exit('Usage: %s filesPath' % sys.argv[0])

    if not os.path.exists(sys.argv[1]):
        sys.exit('ERROR: directory does not exist!' % sys.argv[1])

    path = sys.argv[1]
    tempdirname = "orderedFiles"
    path_ordered_files = os.path.join(path, tempdirname)
    files = os.listdir(path)

    human_sorting(files)
    os.makedirs(path_ordered_files)

    for idx, x in enumerate(files):
        ext = os.path.splitext(x)[1]
        ext = ext.lower()
        idx += 1
        try:
            shutil.copy2(os.path.join(path, x), os.path.join(path_ordered_files, str(idx)+ext))
        except shutil.Error as e:
            print('Error: %s' % e)
        except IOError as e:
            print('Error: %s' % e.strerror)
        
        print str(idx)+ext

