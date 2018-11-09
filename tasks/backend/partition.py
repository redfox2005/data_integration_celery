#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author  : MG
@Time    : 2018/11/9 18:14
@File    : partition.py
@contact : mmmaaaggg@163.com
@desc    : 
"""
from tasks.backend import engine_md
from tasks.utils.db_utils import execute_sql, with_db_session
from datetime import datetime


def partition_table():
    sql_str = """ALTER TABLE `pytdx_stock_tick` 
        PARTITION BY RANGE(date) ( 
        PARTITION p2000 VALUES LESS THAN ('2001-01-01'),  
        PARTITION p2001 VALUES LESS THAN ('2002-01-01'),  
        PARTITION p2002 VALUES LESS THAN ('2003-01-01'),  
        PARTITION p2003 VALUES LESS THAN ('2004-01-01'),  
        PARTITION p2004 VALUES LESS THAN ('2005-01-01'),  
        PARTITION p2005 VALUES LESS THAN ('2006-01-01'),  
        PARTITION p2006 VALUES LESS THAN ('2007-01-01'),  
        PARTITION p2007 VALUES LESS THAN ('2008-01-01'),  
        PARTITION p2008 VALUES LESS THAN ('2009-01-01'),  
        PARTITION p2009 VALUES LESS THAN ('2010-01-01'),  
        PARTITION p2010 VALUES LESS THAN ('2011-01-01'),  
        PARTITION p2011 VALUES LESS THAN ('2012-01-01'),  
        PARTITION p2012 VALUES LESS THAN ('2013-01-01'),  
        PARTITION p2013 VALUES LESS THAN ('2014-01-01'),  
        PARTITION p2014 VALUES LESS THAN ('2015-01-01'),  
        PARTITION p2015 VALUES LESS THAN ('2016-01-01'),  
        PARTITION p2016 VALUES LESS THAN ('2017-01-01'),  
        PARTITION p2017 VALUES LESS THAN ('2018-01-01'),  
        PARTITION p2018 VALUES LESS THAN ('2019-01-01'),  
        PARTITION p2019 VALUES LESS THAN ('2020-01-01'),  
        PARTITION p2020 VALUES LESS THAN ('2021-01-01'),  
        PARTITION pother VALUES LESS THAN (MAXVALUE)
        ) """
    datetime_start = datetime.now()
    with with_db_session(engine_md) as session:
        session.execute(sql_str)

    datetime_end = datetime.now()
    span = datetime_end - datetime_start
    print('花费时间 ', span)


if __name__ == "__main__":
    partition_table()
