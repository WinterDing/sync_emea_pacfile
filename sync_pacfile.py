#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Winter Ding"
# Email: flyawaydxd@126.com

'''
sync_pacfile.py - sync pacfile from emea to apa
version: 1.0
'''

from urllib import urlretrieve
import os
import time
import shutil
from sync_log import logger


def create_folder(folder):
    # check if download_folder exists or not, if not, create folder
    if not os.path.exists(folder):
        os.mkdir(folder)


def download_new_file(url, download_folder, filename):
    create_folder(download_folder)
    local_filename = os.path.join(download_folder, filename)
    # download file from given url to local download folder
    try:
        # bug, if file of url does not exist, no error,response url write to
        # file
        urlretrieve(url, local_filename)
    except Exception:
        # remove invalid downloaded file
        if os.path.exists(local_filename):
            os.remove(local_filename)
        logger.error('Fail: EMEA pacfile is not available from "%s"' % url)
        logger.error('Sync failed...')
        res = 'fail'
    else:
        logger.info('Success: EMEA pacfile download into "%s" successfully' % local_filename)
        res = 'success'
    return res


def copy_file(src_folder, dst_folder, filename, backup_flag=False):
    create_folder(dst_folder)
    src_filename = os.path.join(src_folder, filename)
    # if operation is backup, include backup time in the filename
    if backup_flag:
        current_time = time.strftime('_%Y%m%d_%H%M%S')
    else:
        current_time = ''
    dst_filename = ''.join([os.path.join(dst_folder, filename), current_time])
    try:
        shutil.copyfile(src_filename, dst_filename)
    except Exception:
        logger.error('Fail: copy file from "%s" to "%s" fail' % (src_filename, dst_filename))
        logger.error('Sync failed...')
        res = 'fail'
    else:
        logger.info('Success: copy file from "%s" to "%s" succeed' % (src_filename, dst_filename))
        res = 'success'
    return res


def main():
    #todo optimize here
    url = r'http://global.pac'
    pacfile_name = os.path.basename(url)
    download_folder = r'D:\test\pacfile_download'
    backup_folder = r'D:\test\pacfile_backup'
    pacfile_folder = r'D:\test\pacfile_test'

    logger.warning('Start: Sync pacfile from EMEA')

    if download_new_file(url, download_folder, pacfile_name) == 'fail':
        return 'fail'
    if copy_file(pacfile_folder,backup_folder,pacfile_name,backup_flag=True) == 'fail':
        return 'fail'
    if copy_file(download_folder, pacfile_folder, pacfile_name) == 'fail':
        return 'fail'
    return 'success'

