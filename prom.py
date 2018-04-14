#!/usr/bin/env python
# coding: utf8
# Устанавливаем стандартную внешнюю кодировку = utf8
import mysql.connector as connector
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import logging
from suds.client import Client
logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)
handler = logging.FileHandler('suds.log')
formatter = logging.Formatter('%(levelname)s %(asctime)s %(funcName)s %(message)s')
handler.setFormatter(formatter)
logging.getLogger('suds.client').handlers = []
logging.getLogger('suds.client').addHandler(handler)

cl = Client('http://r23-rc.zdrav.netrika.ru/EMK/EMKService.svc?wsdl')
print(cl)

