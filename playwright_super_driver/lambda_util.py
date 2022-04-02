import os
import shutil
import glob
TMP_DIR = '/tmp/bin/'


def setup_bin():
    copy_bin()
    os.environ['PLAYWRIGHT_BROWSERS_PATH'] = TMP_DIR


def copy_bin():
    # playwrightのバイナリを/tmp下にコピーする
    src = os.environ['PLAYWRIGHT_BROWSERS_PATH']
    dest = TMP_DIR
    if src == dest:
        return
    if os.path.exists(dest):
        return

    shutil.copytree(src, dest)

def delete_bin():
    cleanup(TMP_DIR + '*')

def cleanup(pathName='/tmp/' + '*'):
    for p in glob.glob(pathName):
        if os.path.isfile(p):
            os.remove(p)
