# -*- coding: utf-8 -*-
import os

# Data Settings
CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
GHTORRENT_IMPORT_PATH = '/opt/pull-request-conflicts/ghtorrent_data/projects_for_ml_3' #os.path.join(CURRENT_PATH, '../ghtorrent_data/projects_for_ml_2')

CONFLICT_MATRIX_PATH = os.path.join(CURRENT_PATH, '../conflict_matrix')
REPOSITORIES_BASE_PATH = '/opt/projects'

# Github API
GITHUB_TOKEN = "9767f1c10603cf6a0ce5423bbe016b938b268451"
