#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 11:14
# @Author  : Xuhaozhang
# @Email   : xuhaozhang_hfut@163.com
# @File    : db_create.py

from model import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, db, Base
from migrate.versioning import api
import os.path

Base.metadata.create_all(bind=db)

if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO,
                        api.version(SQLALCHEMY_MIGRATE_REPO))