#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Winter Ding"
# Email: flyawaydxd@126.com
import logging
from logging import handlers
import os

log_file = r'D:\test\pacfile_synclog\sync_log.txt'
# log_file = r'C:\Users\z218680\Desktop\log\log.txt'
log_folder = os.path.dirname(log_file)
if not os.path.exists(log_folder):
    os.mkdir(log_folder)

current_user = os.environ['USERNAME']

logger = logging.getLogger(current_user)
logger.setLevel(level=logging.INFO)

rotateLog = handlers.RotatingFileHandler(log_file, maxBytes=10*1024, backupCount=3)
rotateLog.setLevel(level=logging.INFO)

mail_log = handlers.SMTPHandler('10.225.97.50', 'xiaodong.ding@zf.com', ('xiaodong.ding@zf.com', 'lilian.blaitt@zf.com'), 'apa pacfile sync information')
mail_log.setLevel(level=logging.WARNING)

formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
rotateLog.setFormatter(formatter)

logger.addHandler(rotateLog)
logger.addHandler(mail_log)

logger.warning('test')

