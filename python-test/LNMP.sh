#!/bin/bash
RETVAL=0
NGINX="/usr/local/nginx/sbin/nginx"
PHP="/usr/local/php/sbin/php-fpm" 
nginx_install(){
     #安装软件依赖包
     yum -y groupinstall "Development Tools" "Server PlatformDeveopment"
     yum -y install openssl-devel pcre-devel
     cd /usr/local/src
     yum install -y wget
     #下载nginx包
     wget http://nginx.org/download/nginx-1.12.0.tar.gz
     useradd nginx   #添加nginx运行的用户
     tar zxvf nginx-1.12.0.tar.gz
     cd nginx-1.12.0/
     #安装nginx包
     ./configure --prefix=/usr/local/nginx --user=nginx --group=nginx--with-http_ssl_module --with-http_flv_module --with-http_stub_status_module--with-http_gzip_static_module --with-pcre
     #编译安装
     make && make install
     RETVAL=$?
     if [ $RETVAL -eq 0 ]
     then
         /usr/local/nginx/sbin/nginx  #启动nginx
     else
         echo "nginx编译失败"
     fi
}
nginx_check(){
     if [ -f $NGINX -a -x $NGINX ]
     then
         /usr/local/nginx/sbin/nginx -t   #检查nginx
         RETVAL=$?
         if [ $RETVAL -eq 0 ]
         then
              echo "nginx检查完毕"
              /usr/local/nginx/sbin/nginx
 
              netstat -ntlp | grep nginx
              RETVAL=$?
              if [ $RETVAL -eq 0 ]
              then
                 echo "nginx启动成功"
              else
                  echo "nginx启动失败"
              fi
        else
            echo "please check your nginx"
        fi
    else
        echo "nginx不存在或者没有权限"
    fi
}
php-fpm_install(){
     cd /usr/local/src
     #下载依赖包
     yum -y install libmcrypt-devel bzip2-devel gcc openssl-devel php-mcryptlibmcrypt libxml2-devel libjpeg-devel libpng-devel freetype-devel
     #下载php包
     wget http://cn2.php.net/distributions/php-5.5.38.tar.gz
     tar zxvf php-5.5.38.tar.gz
     cd php-5.5.38/
     #安装php包
     ./configure --prefix=/usr/local/php --with-mysql=mysqlnd --with-pdo-mysql=mysqlnd --with-mysqli=mysqlnd --with-openssl --enable-mbstring --with-freetype-dir --with-jpeg-dir --with-png-dir --with-zlib--with-libxml-dir=/usr --enable-xml --enable-sockets --with-mcrypt  --with-bz2 --enable-fpm --with-gd
     #编译安装     
     make && make install
     RETVAL=$?
     if [ $RETVAL -eq 0 ]
     then
         #开始一些配置步骤
         cp /usr/local/src/php-5.5.38/php.ini-production /usr/local/php/etc/php.ini
         mv /usr/local/php/etc/php-fpm.conf.default /usr/local/php/etc/php-fpm.conf
         #创建php用户
         useradd -M -s /sbin/nologin php
         #修改相关配置
         sed -i -e 's\;pid = run/php-fpm.pid\pid = run/php-fpm.pid\g' -e 's\nobody\php\g' -e 's\listen = 127.0.0.1:9000\listen = 0.0.0.0:9000\g'/usr/local/php/etc/php-fpm.conf
         sed -i 's\;daemonize = yes\daemonize = no\g' /usr/local/php/etc/php-fpm.conf
         #启动php
         /usr/local/php/sbin/php-fpm &
     else
         echo "php编译失败"
     fi
}
 
php-fpm_check(){
     if [ -x $PHP -a -x $PHP ]
     then
         /usr/local/php/sbin/php-fpm -t
         RETVAL=$?
         if [ $RETVAL -eq 0 ]
         then
              echo "php检查完毕"
              /usr/local/php/sbin/php-fpm &
 
              netstat -ntlp | grep php-fpm
              RETVAL=$?
              if [ $RETVAL -eq 0 ]
              then
                  echo "php启动成功"
              else
                  echo "php启动失败"
              fi
         else
              echo "please check yourphp"
         fi
      else
         echo "php不存在或者没有权限"
     fi
}
 
mysql_install(){
     #安装mysql
     yum groupinstall  -ymariadb-server mariadb
     systemctl restart mariadb
     RETVAL=$?
     if [ $RETVAL -eq 0 ]
     then
         systemctl enable mariadb  
         #修改root用户密码
         mysqladmin -u root password "0"
#         #创建一个wordpress数据库
 #        mysql -u root -p0 -e "create database wordpress"
 #        mysql -u root -p0 -e"show databases"
         #给数据库授权
        mysql -uroot -p0 -e "grant all privileges on *.* to 'root'@'%'identified by '0'; FLUSH PRIVILEGES;"
     else
         echo "mysql启动失败"
     fi
}
mysql_check(){
     rpm -qa | grep mariadb
     RETVAL=$?
     if [ $RETVAL -eq 0 ]
     then
         systemctl status mariadb
         RETVAL=$?
         if [ $RETVAL -eq 0 ]
         then
              echo "mysql正在运行中"
         else
              echo "未运行mysql"
         fi
     else
         echo "未安装mysql"
     fi
}
 
 
case "$1" in
     nginx)
          if [ ! -f $NGINX ]
          then
               nginx_install
               nginx_check
          else
               echo "已经安装nginx了"
          fi
          ;;
     php-fpm)
          if [ ! -f $PHP ]
          then
               php-fpm_install
               php-fpm_check
          else
               echo "已经安装php了"
          fi
     mysql)
          rpm -qa | grep mariadb
          RETVAL=$?
          if [ $RETVAL -eq 0 ]
          then
               mysql_install
                        mysql_check
          else
               echo "已经安装mysql了"
          fi
          ;;
esac