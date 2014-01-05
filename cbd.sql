-- --------------------------------------------------------
-- 主机:                           192.168.201.75
-- 服务器版本:                        5.5.32 - MySQL Community Server (GPL)
-- 服务器操作系统:                      linux2.6
-- HeidiSQL 版本:                  8.1.0.4545
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- 导出 cbd 的数据库结构
CREATE DATABASE IF NOT EXISTS `cbd` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `cbd`;


-- 导出  表 cbd.auth_group 结构
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  cbd.auth_group 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;


-- 导出  表 cbd.auth_group_permissions 结构
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_bda51c3c` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`),
  CONSTRAINT `group_id_refs_id_3cea63fe` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_a7792de1` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  cbd.auth_group_permissions 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;


-- 导出  表 cbd.auth_permission 结构
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_e4470c6e` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_728de91f` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;

-- 正在导出表  cbd.auth_permission 的数据：~30 rows (大约)
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(1, 'Can add permission', 1, 'add_permission'),
	(2, 'Can change permission', 1, 'change_permission'),
	(3, 'Can delete permission', 1, 'delete_permission'),
	(4, 'Can add group', 2, 'add_group'),
	(5, 'Can change group', 2, 'change_group'),
	(6, 'Can delete group', 2, 'delete_group'),
	(7, 'Can add user', 3, 'add_user'),
	(8, 'Can change user', 3, 'change_user'),
	(9, 'Can delete user', 3, 'delete_user'),
	(10, 'Can add content type', 4, 'add_contenttype'),
	(11, 'Can change content type', 4, 'change_contenttype'),
	(12, 'Can delete content type', 4, 'delete_contenttype'),
	(13, 'Can add session', 5, 'add_session'),
	(14, 'Can change session', 5, 'change_session'),
	(15, 'Can delete session', 5, 'delete_session'),
	(16, 'Can add site', 6, 'add_site'),
	(17, 'Can change site', 6, 'change_site'),
	(18, 'Can delete site', 6, 'delete_site'),
	(19, 'Can add dinner', 7, 'add_dinner'),
	(20, 'Can change dinner', 7, 'change_dinner'),
	(21, 'Can delete dinner', 7, 'delete_dinner'),
	(22, 'Can add dinner applier', 8, 'add_dinnerapplier'),
	(23, 'Can change dinner applier', 8, 'change_dinnerapplier'),
	(24, 'Can delete dinner applier', 8, 'delete_dinnerapplier'),
	(25, 'Can add message', 9, 'add_message'),
	(26, 'Can change message', 9, 'change_message'),
	(27, 'Can delete message', 9, 'delete_message'),
	(28, 'Can add user', 10, 'add_user'),
	(29, 'Can change user', 10, 'change_user'),
	(30, 'Can delete user', 10, 'delete_user');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;


-- 导出  表 cbd.auth_user 结构
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- 正在导出表  cbd.auth_user 的数据：~1 rows (大约)
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` (`id`, `username`, `first_name`, `last_name`, `email`, `password`, `is_staff`, `is_active`, `is_superuser`, `last_login`, `date_joined`) VALUES
	(1, 'root', '', '', 'maolingzhi@jd.com', 'pbkdf2_sha256$10000$q6WCGJcM2Nnz$WavEFlxUhyXGobzWDih+mkZ63T3uwV7RQLZrZsxhZEk=', 1, 1, 1, '2013-12-04 05:53:00', '2013-12-04 05:53:00');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;


-- 导出  表 cbd.auth_user_groups 结构
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_fbfc09f1` (`user_id`),
  KEY `auth_user_groups_bda51c3c` (`group_id`),
  CONSTRAINT `user_id_refs_id_831107f1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `group_id_refs_id_f0ee9890` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  cbd.auth_user_groups 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;


-- 导出  表 cbd.auth_user_user_permissions 结构
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_fbfc09f1` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`),
  CONSTRAINT `user_id_refs_id_f2045483` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `permission_id_refs_id_67e79cb` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  cbd.auth_user_user_permissions 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;


-- 导出  表 cbd.dinner_dinner 结构
CREATE TABLE IF NOT EXISTS `dinner_dinner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `purpose` varchar(400) DEFAULT NULL,
  `count` int(11) NOT NULL,
  `girl_count` int(11) NOT NULL,
  `boy_count` int(11) NOT NULL,
  `location` varchar(400) DEFAULT NULL,
  `time` datetime NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dinner_dinner_516bb1bd` (`count`),
  KEY `dinner_dinner_2e2065ab` (`girl_count`),
  KEY `dinner_dinner_60fde368` (`boy_count`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  cbd.dinner_dinner 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `dinner_dinner` DISABLE KEYS */;
/*!40000 ALTER TABLE `dinner_dinner` ENABLE KEYS */;


-- 导出  表 cbd.dinner_dinnerapplier 结构
CREATE TABLE IF NOT EXISTS `dinner_dinnerapplier` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  cbd.dinner_dinnerapplier 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `dinner_dinnerapplier` DISABLE KEYS */;
/*!40000 ALTER TABLE `dinner_dinnerapplier` ENABLE KEYS */;


-- 导出  表 cbd.dinner_message 结构
CREATE TABLE IF NOT EXISTS `dinner_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `to` varchar(40) DEFAULT NULL,
  `msg` varchar(400) DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  cbd.dinner_message 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `dinner_message` DISABLE KEYS */;
/*!40000 ALTER TABLE `dinner_message` ENABLE KEYS */;


-- 导出  表 cbd.dinner_user 结构
CREATE TABLE IF NOT EXISTS `dinner_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(40) DEFAULT NULL,
  `passwd` varchar(400) DEFAULT NULL,
  `intro` varchar(400) DEFAULT NULL,
  `hometown` varchar(40) DEFAULT NULL,
  `qq` varchar(40) DEFAULT NULL,
  `sina` varchar(40) DEFAULT NULL,
  `wechat` varchar(40) DEFAULT NULL,
  `industry` varchar(40) DEFAULT NULL,
  `career` varchar(40) DEFAULT NULL,
  `interest` varchar(40) DEFAULT NULL,
  `photo1` varchar(40) DEFAULT NULL,
  `photo2` varchar(40) DEFAULT NULL,
  `coordinate` varchar(40) DEFAULT NULL,
  `born` datetime DEFAULT NULL,
  `edu` varchar(40) DEFAULT NULL,
  `returned` tinyint(1) NOT NULL,
  `gender` tinyint(1) NOT NULL,
  `forgen` tinyint(1) NOT NULL,
  `soe` tinyint(1) NOT NULL,
  `civil` tinyint(1) NOT NULL,
  `institution` tinyint(1) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- 正在导出表  cbd.dinner_user 的数据：~2 rows (大约)
/*!40000 ALTER TABLE `dinner_user` DISABLE KEYS */;
INSERT INTO `dinner_user` (`id`, `username`, `passwd`, `intro`, `hometown`, `qq`, `sina`, `wechat`, `industry`, `career`, `interest`, `photo1`, `photo2`, `coordinate`, `born`, `edu`, `returned`, `gender`, `forgen`, `soe`, `civil`, `institution`, `created_at`, `updated_at`) VALUES
	(1, '1', '1', '此生，你我永隔着遥远的距离梦中的小城让我在美好的日子里，遇见春暖花开红尘，隔着岁月的彼岸闲愁几许，岁月忽已晚花开花谢，刹那永恒秋韵阑珊，盈心此间阿莲我的爱情不是海千指百指弹，柔肠万转故秋情愫我是爸爸的包包转身，流年似水依依落雪，幽幽岁月百载春秋，眼睫匆匆浮尘在最美的年华里遇见你梅雪盛极，心络依依莲的心事回眸，忆千年，为你，倾一世不老的情', '中国', NULL, NULL, NULL, NULL, NULL, NULL, '/static/imgs/album-bb.jpg', '/static/imgs/album-bb.jpg', NULL, NULL, NULL, 0, 1, 0, 0, 0, 0, '2013-12-04 05:59:38', '2013-12-04 05:59:38'),
	(2, 'mlzboy', 'zhoubt', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '/static/imgs/album-bb.jpg', '/static/imgs/album-bb.jpg', NULL, NULL, NULL, 0, 1, 0, 0, 0, 0, '2013-12-04 14:05:06', '2013-12-04 14:05:06');
/*!40000 ALTER TABLE `dinner_user` ENABLE KEYS */;


-- 导出  表 cbd.django_content_type 结构
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- 正在导出表  cbd.django_content_type 的数据：~10 rows (大约)
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` (`id`, `name`, `app_label`, `model`) VALUES
	(1, 'permission', 'auth', 'permission'),
	(2, 'group', 'auth', 'group'),
	(3, 'user', 'auth', 'user'),
	(4, 'content type', 'contenttypes', 'contenttype'),
	(5, 'session', 'sessions', 'session'),
	(6, 'site', 'sites', 'site'),
	(7, 'dinner', 'dinner', 'dinner'),
	(8, 'dinner applier', 'dinner', 'dinnerapplier'),
	(9, 'message', 'dinner', 'message'),
	(10, 'user', 'dinner', 'user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;


-- 导出  表 cbd.django_session 结构
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_c25c2c28` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  cbd.django_session 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;


-- 导出  表 cbd.django_site 结构
CREATE TABLE IF NOT EXISTS `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- 正在导出表  cbd.django_site 的数据：~1 rows (大约)
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
	(1, 'example.com', 'example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
