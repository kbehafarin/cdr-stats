#
# CDR-Stats License
# http://www.cdr-stats.org
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2012 Star2Billing S.L.
#
# The Initial Developer of the Original Code is
# Arezqui Belaid <info@star2billing.com>
#
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

TIME_ZONE = 'Europe/Madrid'

APPLICATION_DIR = os.path.dirname(globals()['__file__'])

#DATABASE SETTINGS
#=================
DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2','postgresql','mysql','sqlite3','oracle'
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'DATABASENAME',
        'USER': 'DB_USERNAME',
        'PASSWORD': 'DB_PASSWORD',
        'HOST': 'DB_HOSTNAME',
        'PORT': 'DB_PORT',
        'OPTIONS': {
            #Needed on Mysql
            # 'init_command': 'SET storage_engine=INNODB',
            #Postgresql Autocommit
            'autocommit': True,
        }
    }
}


#CELERY SETTINGS
#===============
CARROT_BACKEND = 'redis'
BROKER_HOST = 'localhost'  # Maps to redis host.
BROKER_PORT = 6379         # Maps to redis port.
BROKER_VHOST = 0        # Maps to database number.

CELERY_RESULT_BACKEND = 'redis'
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0
#REDIS_CONNECT_RETRY = True

#EMAIL BACKEND
#=============
# Email configuration
DEFAULT_FROM_EMAIL = 'CDR-Stats <cdr-stats@localhost.com>'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'username@gmail.com'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_SUBJECT_PREFIX = '[CDR-Stats] '

#TASTYPIE
#========
API_ALLOWED_IP = [
    '127.0.0.1',
    'localhost',
    #'SERVER_IP',
]

#SOCKETIO
#========
SOCKETIO_HOST = 'SERVER_IP'
SOCKETIO_PORT = 9000
SOCKETIO_CALLNUM_DEFAULT = 0

#GENERAL
#=======
# PHONENUMBER_PREFIX_LIMIT_MIN & PHONENUMBER_PREFIX_LIMIT_MAX are used to know
# how many digits are used to match against the dialcode prefix database
PHONENUMBER_PREFIX_LIMIT_MIN = 2
PHONENUMBER_PREFIX_LIMIT_MAX = 5

# If PN is lower than PN_MIN_DIGITS it will be considered as an extension
# If PN is longer than PN_MIN_DIGITS but lower than PN_MAX_DIGITS then
# The PN will be considered as local call and the LOCAL_DIALCODE will be added
LOCAL_DIALCODE = 1  # Set the Dialcode of your country (44 for UK, 1 for US)
PN_MIN_DIGITS = 6
PN_MAX_DIGITS = 9

# List of phonenumber prefix to ignore, this will be remove prior analysis
PREFIX_TO_IGNORE = "+,0,00,000,0000,00000,011,55555,99999"

# When the dialed number is less or equal to INTERNAL_CALL, the call will be considered
# as a internal call, for example when dialed number is 41200
INTERNAL_CALL = 5

#Realtime Graph : set the Y axis limit
REALTIME_Y_AXIS_LIMIT = 300

#ASTERISK IMPORT
#===============
ASTERISK_PRIMARY_KEY = 'acctid'  # acctid, _id

#CDR_BACKEND
#===========
#list of CDR Backends to import
CDR_BACKEND = {
    'MYSQL_IMPORT_CDR_HOST': {
        'db_engine': 'mysql',  # mysql, pgsql, mongo
        'cdr_type': 'asterisk',  # asterisk or freeswitch
        'db_name': 'MYSQL_IMPORT_CDR_DBNAME',
        'table_name': 'MYSQL_IMPORT_CDR_TABLENAME',
        'host': 'MYSQL_IMPORT_CDR_HOST',
        'port': 3306,  # 3306 mysql, 5432 pgsql
        'user': 'MYSQL_IMPORT_CDR_USER',
        'password': 'MYSQL_IMPORT_CDR_PASSWORD',
    },
    # '127.0.0.1': {
    #     'db_engine': 'mysql',  # mysql, pgsql, mongodb
    #     'cdr_type': 'asterisk',  # asterisk or freeswitch
    #     'db_name': 'asteriskcdr',
    #     'table_name': 'cdr',  # collection if mongodb
    #     'host': 'localhost',
    #     'port': 3306,  # 3306 mysql, 5432 pgsql, 27017 mongodb
    #     'user': 'root',
    #     'password': 'password',
    # },
    # '127.0.0.1': {
    #     'db_engine': 'mongodb',  # mysql, pgsql, mongodb
    #     'cdr_type': 'freeswitch',  # asterisk or freeswitch
    #     'db_name': 'freeswitch_cdr',
    #     'table_name': 'cdr',  # collection if mongodb
    #     'host': 'localhost',
    #     'port': 27017,  # 3306 mysql, 5432 pgsql, 27017 mongodb
    #     'user': '',
    #     'password': '',
    # },
}

#Define the IP of your local Switch, it needs to exist in the CDR_BACKEND list
LOCAL_SWITCH_IP = 'SERVER_IP'

#Asterisk Manager / Used for Realtime and Concurrent calls
ASTERISK_MANAGER_HOST = 'localhost'
ASTERISK_MANAGER_USER = 'cdrstats_user'
ASTERISK_MANAGER_SECRET = 'cdrstats_secret'

#MONGODB
#=======
#Settings of CDR-Stats MongoDB server, this is used to store the analytic data
MONGO_CDRSTATS = {
    'DB_NAME': 'cdr-stats',
    'HOST': 'localhost',
    'PORT': 27017,
    'CDR_COMMON': 'cdr_common',
    'DAILY_ANALYTIC': 'daily_analytic',
    'MONTHLY_ANALYTIC': 'monthly_analytic',
    'CONC_CALL': 'concurrent_call',
    'CONC_CALL_AGG': 'concurrent_call_aggregate',
    'URI': 'mongodb://localhost:27017'
}
