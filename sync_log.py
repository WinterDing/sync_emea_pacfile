#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Winter Ding"
# Email: flyawaydxd@126.com
import logging
from logging import handlers
import os

log_file = r'D:\test\pacfile_synclog\sync_log.txt'
log_folder = os.path.dirname(log_file)
if not os.path.exists(log_folder):
    os.mkdir(log_folder)

current_user = os.environ['USERNAME']

logger = logging.getLogger(current_user)
logger.setLevel(level=logging.INFO)

rotateLog = handlers.RotatingFileHandler(log_file, maxBytes=10*1024, backupCount=3)
rotateLog.setLevel(level=logging.DEBUG)

formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
rotateLog.setFormatter(formatter)

logger.addHandler(rotateLog)



