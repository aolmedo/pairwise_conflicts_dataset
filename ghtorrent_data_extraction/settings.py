# -*- coding: utf-8 -*-
import os

# GHTorrent DB Settings
DB_NAME = 'ghtorrent_restore'
DB_USER = 'aolmedo'
DB_PASSWORD = ''
DB_HOST = '192.168.0.225'
DB_PORT = '5432'

# Data Settings
CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
GHTORRENT_EXPORT_PATH = '/home/aolmedo/phd/repo/pull-request-conflicts/ghtorrent_data/projects_for_ml_3'  # os.path.join(CURRENT_PATH, '../ghtorrent_data/projects_for_ml/')
