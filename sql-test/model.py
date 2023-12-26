#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/16 16:04
# @Author  : Xuhaozhang
# @Email   : xuhaozhang_hfut@163.com
# @File    : model.py

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base  # db 基类
from sqlalchemy import Column, Integer, String, DateTime  # 相应的列
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session  # 执行的相关方法
from sqlalchemy.dialects.mysql import LONGTEXT

import os

"""
设置数据库参数
"""
MYSQL_DB = 'sqlalchemy_migratetest'
MYSQL_USER = 'root'
MYSQL_PASSWD = 'mariadb'
MYSQL_HOST = 'localhost'
MYSQL_POST = 3306

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "mysql://%s:%s@%s:%s/%s?charset=utf8" % (
MYSQL_USER, MYSQL_PASSWD, MYSQL_HOST, MYSQL_POST, MYSQL_DB)
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir,
                                       'db_repository')  # 设置数据库迁移保存的文件夹，用来sqlalchemymigrate

db = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

Base = declarative_base()
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=db))

Base.query = db_session.query_property()


def init_db():
    Base.metadata.create_all(bind=db)


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)

    def __init__(self, username, password, email, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return "" % (self.username, self.password)
