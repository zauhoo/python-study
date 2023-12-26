#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 21:08
# @Author  : Xuhaozhang
# @Email   : xuhaozhang_hfut@163.com
# @File    : db_migrate.py

import imp
from migrate.versioning import api
from model import Base
from model import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO

migration = SQLALCHEMY_MIGRATE_REPO + '/versions/d_migration.py' % (api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO) + 1)
tmp_module = imp.new_module('old_model')
old_model = api.create_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
exec (old_model in tmp_module.__dict__)
script = api.make_update_script_for_model(SQLALCHEMY_DATABASE_URI,
                                          SQLALCHEMY_MIGRATE_REPO,
                                          tmp_module.meta, Base.metadata)
open(migration, 'wt').write(script)
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print ('New migration saved as ' + migration)
print ('Current database version: ' + str(api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)))