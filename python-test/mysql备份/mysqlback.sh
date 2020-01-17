#!/bin/bash
#数据表自动备份脚本
# Name:bakmysql.sh
# This is a ShellScript For Auto DB Backup and Delete old Backup

#备份存放路径
backupdir=/home/dbback
#时间格式
time=` date +%Y%m%d%H `

#本地备份单个数据库（结构+数据）：mysqldump路径+用户+用户密码+数据库名> $存放路径/备份包命名$时间格式
/usr/local/mysql/bin/mysqldump -u root -p密码 --databases dbname | gzip > $backupdir/dbbackname$time.sql.gz

#备份远程主机数据库
#/usr/local/mysql/bin/mysqldump -h '远程主机IP' -u root -p密码 --databases dbname | gzip > $backupdir/dbbackname$time.sql.gz

#备份多个数据库
#/usr/local/mysql/bin/mysqldump -u root -p密码 --databases 数据库1 数据库2 | gzip > $backupdir/dbbackname$time.sql.gz

#备份所有数据库（-A：结构+数据）（-A -d：只备份结构）
#/usr/local/mysql/bin/mysqldump -u root -p密码 -A -d | gzip > $backupdir/dbbackname$time.sql.gz

#删除1天前（-mtime +1）的文件
rm -rf $(find  /home/dbback/ -mtime +1 -name "*.sql.gz")