-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: home_service
-- ------------------------------------------------------
-- Server version	8.0.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounts_contactutilisateur`
--

DROP TABLE IF EXISTS `accounts_contactutilisateur`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_contactutilisateur` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `contact` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `utilisateur_id` bigint NOT NULL,
  `type_contact_id` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_contactutil_utilisateur_id_d4f5c8af_fk_accounts_` (`utilisateur_id`),
  CONSTRAINT `accounts_contactutil_utilisateur_id_d4f5c8af_fk_accounts_` FOREIGN KEY (`utilisateur_id`) REFERENCES `accounts_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_contactutilisateur`
--

LOCK TABLES `accounts_contactutilisateur` WRITE;
/*!40000 ALTER TABLE `accounts_contactutilisateur` DISABLE KEYS */;
INSERT INTO `accounts_contactutilisateur` VALUES (1,'Kam zani',9,'1'),(2,'0576897906',9,'2'),(3,'0845874534',9,'3'),(4,'kam@gmail.com',9,'4'),(5,'0756764576',3,'Facebook'),(6,'0756764576',11,'3'),(7,'0756764576',13,'3'),(8,'0756764576',8,'3'),(9,'5456666',14,'WhatsApp'),(10,'09786543',18,'WhatsApp'),(11,'4908773838',18,'WhatsApp'),(12,'09786543',20,'Téléphone'),(13,'jhg',22,'Facebook'),(14,'4908773838',3,'WhatsApp'),(15,'0756764576',24,'3'),(16,'0756764576',2,'2'),(17,'ajauad',2,'1'),(18,'karau',4,'1'),(19,'56-877-ç9_78987',28,'1'),(20,'67800°0987',1,'1'),(21,'67800°0987',13,'2'),(22,'kkz@gmail.com',13,'4'),(23,'67800°0987',14,'3'),(24,'uzo',14,'1');
/*!40000 ALTER TABLE `accounts_contactutilisateur` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_customuser`
--

DROP TABLE IF EXISTS `accounts_customuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_customuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_general_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `role` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `photo` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_customuser`
--

LOCK TABLES `accounts_customuser` WRITE;
/*!40000 ALTER TABLE `accounts_customuser` DISABLE KEYS */;
INSERT INTO `accounts_customuser` VALUES (1,'pbkdf2_sha256$1000000$KbJZK0D2BltGaZNXJZ1HhC$rrtrP7VW1dPLuc8Exo5xMxTjnR5qraWh0xenQ8iO9GM=','2025-06-16 23:52:40.731182',1,'inza@gmail.com','inza','admin',1,1,NULL),(2,'pbkdf2_sha256$1000000$oFF7CVFRbwz6XPdBQfPMgc$nrJXsBD3l3C+LrciP6Mye+NGN2l7ewUrViNEoWKNFYU=','2025-06-16 14:25:09.838575',0,'baka@gmail.com','baka@gmail.com','prestataire',1,0,NULL),(3,'pbkdf2_sha256$1000000$s1VursAttlVKGE3HHFXAyp$nzPrdYor6U6bRAuvXdReBv9GVgEllfhANlePcZphCU4=','2025-06-16 23:07:36.303639',0,'beker@gmail.com','beke ker','prestataire',1,0,NULL),(4,'pbkdf2_sha256$1000000$sWkj7IoKbI5sKEqzIQNDzG$txu+4OiHUmoRxVJLJwVbBFMn6oClIq/yORSq+ai5zFk=','2025-06-16 14:50:46.723231',0,'presta@gmail.com','rge ty','client',1,0,''),(5,'pbkdf2_sha256$1000000$YYegOTls3IOqcenb7X6PfR$EFwKo4r+JPzaPVmO+p1j1KtdeUVdZ42yywzVNMtzhOk=','2025-06-15 06:14:03.729704',0,'roge@gmail.com','rogatat','client',1,0,NULL),(6,'pbkdf2_sha256$1000000$TEJRhRxUwIuaZ0IYQe0Jjl$YdySKBenEDYoTW1ks/vqPazfG9nE3nE7xAapn7ftIGY=','2025-06-15 11:09:20.054294',0,'soul@gmail.com','soul kam','prestataire',1,0,NULL),(7,'pbkdf2_sha256$1000000$vL5RTOvWOuc2XZ4tJgwr9r$G21HuSKz7OD5KFrW2wMHwRTJL2L0qYiLZFseMTywt5I=','2025-06-15 06:37:35.032885',0,'zagui@gmail.com','Inza Gui','prestataire',1,0,NULL),(8,'pbkdf2_sha256$1000000$3zWUOPswkU4wyQWfkQhlDq$2jQ5TZHIjIpsBpyxIuHhRSsAdeC75iwBHuMWpMrVl0s=','2025-06-16 14:06:08.783713',0,'kara@gmail.com','Amy kara','prestataire',1,0,NULL),(9,'pbkdf2_sha256$1000000$THpUWncKOoZ1h4PMOnQuvu$kidgRbf/IULFfJJ0z0WsOudCsOKC7ozTji1Ts8Y9doc=','2025-06-16 04:41:43.408268',0,'zani@gmail.com','zani kam','prestataire',1,0,NULL),(11,'pbkdf2_sha256$1000000$zNUDZtuGdIr64Rbbzohj8a$TcwjQWkf59jcwnmSufUWRHbJeXow6JT+QEJA0LwJT10=','2025-06-16 23:04:33.868316',0,'ely@gmail.com','ely ely','client',1,0,'utilisateurs/photos/Capture_décran_2025-06-12_193215.png'),(13,'pbkdf2_sha256$1000000$lmfD3Yf8YF0okJlR9rdfDt$6KcZg/8oGlVb6IpiIrDtJ99j9qb+3rTSahHHHZ0PPP4=','2025-06-16 23:26:42.928715',0,'her@gmail.com','herman','prestataire',1,0,NULL),(14,'pbkdf2_sha256$1000000$5DsR2MHXIStzJomNaKW2PK$Hp4QgFmJmA7nc//TEEA0UnVMeAsL16gtpSizn8jlaM0=','2025-06-16 23:43:07.751039',0,'uza@gmail.com','uz o','prestataire',1,0,''),(15,'pbkdf2_sha256$1000000$39BKtlZl1wl43jMjwfIy5v$0nPbyJ/nIMRQi5nB/rT7dDM4kGgwGIl9xXRIfUMjsZg=',NULL,0,'zer@gmail.com','zer re','client',1,0,''),(16,'pbkdf2_sha256$1000000$zig4GztV4a5P7FS5yOkzwn$Xvb4v690w1HX8Pres+HoE8LZ5xnqj1zEyvqkZ4KuGu0=',NULL,0,'zera@gmail.com','zer re','client',1,0,''),(17,'pbkdf2_sha256$1000000$dLQ0vJqKZj6jl7ur9lV54T$Wor8ZRw/Y/6yQfaKcYA0druusccrrZzr9TZxz7pMLI4=',NULL,0,'yuta@gmail.com','yut a','client',1,0,''),(18,'pbkdf2_sha256$1000000$4zzKq9MX6xs22w2RXGiEzb$ZSmxsZSHUJmr2zD00woL6E2yBHUvvlGZWY7wEC/oeuI=','2025-06-16 06:35:06.765269',0,'yuj@gmail.com','yuj i','client',1,0,''),(19,'pbkdf2_sha256$1000000$hPyPSszjpYJzAmpvbnre4v$7yicPXbFEmDtH5ogRDAE0AGi/QotOAuf3v4ymlMJSyI=',NULL,0,'fert@gmail.com','yuj i','prestataire',1,0,''),(20,'pbkdf2_sha256$1000000$OL7iB3glZEaAPXAP7Hebgw$PvNMnTcY6NsiMybhnn/hhb1bQrPyCq1tt0vrBpOjzYo=',NULL,0,'jyu@gmail.com','yuh','prestataire',1,0,''),(21,'pbkdf2_sha256$1000000$CvWWHgNM2kVmhxzjFmLg4o$SHlYMW37sqh3X1mtjIFMWWoJ7rAZDSET6QqSMQar0BI=',NULL,0,'juio@gmail.com','gfty zhzj','client',1,0,''),(22,'pbkdf2_sha256$1000000$fnyn7MuYYuAcR0eM8xUIfe$iNa3Gc/0v0Vz+UG6uzYmsX9uPGab2qPGqSW2TvyDhWk=','2025-06-16 04:24:56.578433',0,'jhg@gmail.com','jhg','client',1,0,''),(23,'pbkdf2_sha256$1000000$PcfzKFNn4slpEcAqoHHyLB$iqCqpzvVlzcC3XWDRvJdFi5s6O9FVFOjqdhJj2OWVI0=','2025-06-16 04:42:37.638574',0,'jhy@gmail.com','jhy','prestataire',1,0,''),(24,'pbkdf2_sha256$1000000$lD6b5f748K3cJGqa51GSYn$H69fIvOwUDfWW6ibd71B76hKYhpZAJ75wTpJ8pbu/vA=',NULL,0,'hy@gmail.com','hy','client',1,0,''),(25,'pbkdf2_sha256$1000000$PsBAGZ52Oc43rM5IvsoNOO$g0LIhHxpeZcfaR7hFmS1nz+TKSZX6sei8+OCl+4KIfI=',NULL,0,'j@gmail.com','j','client',1,0,''),(26,'pbkdf2_sha256$1000000$CabCL45nhOVhXXJd265xum$HCXpkIVMI7O4rCq0LF4NUT4EpoPr5fTIOvJvdn/Yvls=',NULL,0,'k@gmail.com','kui ki','prestataire',1,0,''),(27,'pbkdf2_sha256$1000000$j2l3ouAFGgudU4NqCL7blb$3hTwpgaOQHEfDDZKvqMdItcyL54TnTlwcjlMgOx2+gU=','2025-06-16 23:14:33.323247',0,'jui@gmail.com','jui','prestataire',1,0,''),(28,'pbkdf2_sha256$1000000$vozwHsh31z8O8mi1CpG0WI$MAiKD/zF6LZwk4n1khHqrtuvHjSaf/pjrfqTVjBFeT0=',NULL,0,'lo@gmail.com','lo','prestataire',1,0,'');
/*!40000 ALTER TABLE `accounts_customuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_customuser_groups`
--

DROP TABLE IF EXISTS `accounts_customuser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_customuser_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_customuser_groups_customuser_id_group_id_c074bdcb_uniq` (`customuser_id`,`group_id`),
  KEY `accounts_customuser_groups_group_id_86ba5f9e_fk_auth_group_id` (`group_id`),
  CONSTRAINT `accounts_customuser__customuser_id_bc55088e_fk_accounts_` FOREIGN KEY (`customuser_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `accounts_customuser_groups_group_id_86ba5f9e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_customuser_groups`
--

LOCK TABLES `accounts_customuser_groups` WRITE;
/*!40000 ALTER TABLE `accounts_customuser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_customuser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_customuser_user_permissions`
--

DROP TABLE IF EXISTS `accounts_customuser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_customuser_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_customuser_user_customuser_id_permission_9632a709_uniq` (`customuser_id`,`permission_id`),
  KEY `accounts_customuser__permission_id_aea3d0e5_fk_auth_perm` (`permission_id`),
  CONSTRAINT `accounts_customuser__customuser_id_0deaefae_fk_accounts_` FOREIGN KEY (`customuser_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `accounts_customuser__permission_id_aea3d0e5_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_customuser_user_permissions`
--

LOCK TABLES `accounts_customuser_user_permissions` WRITE;
/*!40000 ALTER TABLE `accounts_customuser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_customuser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_typecontact`
--

DROP TABLE IF EXISTS `accounts_typecontact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_typecontact` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_typecontact`
--

LOCK TABLES `accounts_typecontact` WRITE;
/*!40000 ALTER TABLE `accounts_typecontact` DISABLE KEYS */;
INSERT INTO `accounts_typecontact` VALUES (1,'Facebook'),(2,'WhatsApp'),(3,'Téléphone'),(4,'Email');
/*!40000 ALTER TABLE `accounts_typecontact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add custom user',6,'add_customuser'),(22,'Can change custom user',6,'change_customuser'),(23,'Can delete custom user',6,'delete_customuser'),(24,'Can view custom user',6,'view_customuser'),(25,'Can add service',7,'add_service'),(26,'Can change service',7,'change_service'),(27,'Can delete service',7,'delete_service'),(28,'Can view service',7,'view_service'),(29,'Can add prestataire',8,'add_prestataire'),(30,'Can change prestataire',8,'change_prestataire'),(31,'Can delete prestataire',8,'delete_prestataire'),(32,'Can view prestataire',8,'view_prestataire'),(33,'Can add avis',9,'add_avis'),(34,'Can change avis',9,'change_avis'),(35,'Can delete avis',9,'delete_avis'),(36,'Can view avis',9,'view_avis'),(37,'Can add service offert',10,'add_serviceoffert'),(38,'Can change service offert',10,'change_serviceoffert'),(39,'Can delete service offert',10,'delete_serviceoffert'),(40,'Can view service offert',10,'view_serviceoffert'),(41,'Can add reservation',11,'add_reservation'),(42,'Can change reservation',11,'change_reservation'),(43,'Can delete reservation',11,'delete_reservation'),(44,'Can view reservation',11,'view_reservation'),(45,'Can add notification',12,'add_notification'),(46,'Can change notification',12,'change_notification'),(47,'Can delete notification',12,'delete_notification'),(48,'Can view notification',12,'view_notification'),(49,'Can add type contact',13,'add_typecontact'),(50,'Can change type contact',13,'change_typecontact'),(51,'Can delete type contact',13,'delete_typecontact'),(52,'Can view type contact',13,'view_typecontact'),(53,'Can add contact utilisateur',14,'add_contactutilisateur'),(54,'Can change contact utilisateur',14,'change_contactutilisateur'),(55,'Can delete contact utilisateur',14,'delete_contactutilisateur'),(56,'Can view contact utilisateur',14,'view_contactutilisateur'),(57,'Can add message',15,'add_message'),(58,'Can change message',15,'change_message'),(59,'Can delete message',15,'delete_message'),(60,'Can view message',15,'view_message'),(61,'Can add prestataire banni',16,'add_prestatairebanni'),(62,'Can change prestataire banni',16,'change_prestatairebanni'),(63,'Can delete prestataire banni',16,'delete_prestatairebanni'),(64,'Can view prestataire banni',16,'view_prestatairebanni'),(65,'Can add signalement',17,'add_signalement'),(66,'Can change signalement',17,'change_signalement'),(67,'Can delete signalement',17,'delete_signalement'),(68,'Can view signalement',17,'view_signalement'),(69,'Can add newsletter email',18,'add_newsletteremail'),(70,'Can change newsletter email',18,'change_newsletteremail'),(71,'Can delete newsletter email',18,'delete_newsletteremail'),(72,'Can view newsletter email',18,'view_newsletteremail');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_general_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_accounts_customuser_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_accounts_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2025-06-10 21:17:17.658475','1','rge ty - Entretien piscine par baka@gmail.com',3,'',11,1),(2,'2025-06-10 22:29:08.957261','4','rogatat - Entretien piscine par baka@gmail.com',3,'',11,1),(3,'2025-06-10 22:29:08.957339','3','rogatat - plombérie par baka@gmail.com',3,'',11,1),(4,'2025-06-10 22:29:08.957375','2','rge ty - Entretien piscine par baka@gmail.com',3,'',11,1),(5,'2025-06-11 09:13:23.126133','2','Avis de rge ty - 5/5',3,'',9,1),(6,'2025-06-11 09:13:23.126192','1','Avis de rge ty - 4/5',3,'',9,1),(7,'2025-06-11 11:17:38.415135','8','rge ty - Assistant virtuel par Inza Gui',3,'',11,1),(8,'2025-06-11 11:17:38.415202','7','rge ty - plombérie par beke ker',3,'',11,1),(9,'2025-06-11 11:17:38.415240','6','rge ty - plombérie par baka@gmail.com',3,'',11,1),(10,'2025-06-11 11:17:38.415271','5','rge ty - Entretien piscine par baka@gmail.com',3,'',11,1),(11,'2025-06-11 11:31:43.303571','2','Notification pour beke ker - Nouvelle demande de réservation pour votre service plombérie.',3,'',12,1),(12,'2025-06-11 11:31:43.303653','1','Notification pour Inza Gui - Nouvelle réservation pour votre service Assistant virtuel.',3,'',12,1),(13,'2025-06-11 11:31:59.888521','9','rogatat - plombérie par beke ker',3,'',11,1),(14,'2025-06-11 12:26:23.492079','8','Notification pour Inza Gui - Le client a annulé la réservation pour Assistant virtuel.',3,'',12,1),(15,'2025-06-11 12:26:23.492132','7','Notification pour Inza Gui - Nouvelle demande de réservation pour votre service Assistant virtuel.',3,'',12,1),(16,'2025-06-11 12:26:23.492157','6','Notification pour Inza Gui - Le client a annulé la réservation pour Assistant virtuel.',3,'',12,1),(17,'2025-06-11 12:26:23.492178','5','Notification pour rge ty - Le prestataire a confirmé la nouvelle date pour votre réservation du service plombérie.',3,'',12,1),(18,'2025-06-11 12:26:23.492198','4','Notification pour Inza Gui - Nouvelle demande de réservation pour votre service Assistant virtuel.',3,'',12,1),(19,'2025-06-11 12:26:23.492217','3','Notification pour soul kam - Nouvelle demande de réservation pour votre service plombérie.',3,'',12,1),(20,'2025-06-11 12:26:36.041745','12','rge ty - Assistant virtuel par Inza Gui',3,'',11,1),(21,'2025-06-11 12:26:36.041805','11','rge ty - Assistant virtuel par Inza Gui',3,'',11,1),(22,'2025-06-11 12:26:36.041837','10','rge ty - plombérie par soul kam',3,'',11,1),(23,'2025-06-11 20:37:06.146708','1','Facebook',1,'[{\"added\": {}}]',13,1),(24,'2025-06-11 20:38:57.038399','2','WhatsApp',1,'[{\"added\": {}}]',13,1),(25,'2025-06-11 20:39:18.524199','3','Téléphone',1,'[{\"added\": {}}]',13,1),(26,'2025-06-11 20:39:31.040750','4','Email',1,'[{\"added\": {}}]',13,1),(27,'2025-06-12 21:59:52.861125','8','Babysitting par Amy kara',2,'[{\"changed\": {\"fields\": [\"Description\"]}}]',10,1),(28,'2025-06-12 22:00:19.301942','20','rogatat - Babysitting par Amy kara',3,'',11,1),(29,'2025-06-12 22:00:19.302071','19','rge ty - Babysitting par Amy kara',3,'',11,1),(30,'2025-06-12 22:00:19.302181','18','rge ty - Assistant virtuel par Inza Gui',3,'',11,1),(31,'2025-06-12 22:00:19.302264','17','rge ty - plombérie par baka@gmail.com',3,'',11,1),(32,'2025-06-12 22:00:19.302331','16','rge ty - plombérie par beke ker',3,'',11,1),(33,'2025-06-12 22:00:19.302392','15','rge ty - plombérie par baka@gmail.com',3,'',11,1),(34,'2025-06-12 22:00:19.302459','14','rogatat - Entretien piscine par baka@gmail.com',3,'',11,1),(35,'2025-06-12 22:00:19.302522','13','rge ty - Entretien piscine par baka@gmail.com',3,'',11,1),(36,'2025-06-12 22:00:40.467608','30','Notification pour Amy kara - Le client a confirmé la nouvelle date pour la réservation du service Babysitting.',3,'',12,1),(37,'2025-06-12 22:00:40.467708','29','Notification pour rogatat - Votre réservation pour Babysitting a été acceptée.',3,'',12,1),(38,'2025-06-12 22:00:40.467773','28','Notification pour rge ty - Le prestataire a confirmé la nouvelle date pour votre réservation du service Babysitting.',3,'',12,1),(39,'2025-06-12 22:00:40.467837','27','Notification pour Amy kara - Nouvelle demande de réservation pour votre service Babysitting.',3,'',12,1),(40,'2025-06-12 22:00:40.467895','26','Notification pour rge ty - Votre réservation pour Babysitting a été acceptée.',3,'',12,1),(41,'2025-06-12 22:00:40.467947','25','Notification pour Amy kara - Nouvelle demande de réservation pour votre service Babysitting.',3,'',12,1),(42,'2025-06-12 22:00:40.467994','24','Notification pour rge ty - Votre réservation pour Assistant virtuel a été acceptée.',3,'',12,1),(43,'2025-06-12 22:00:40.468043','23','Notification pour Inza Gui - Nouvelle demande de réservation pour votre service Assistant virtuel.',3,'',12,1),(44,'2025-06-12 22:00:40.468098','22','Notification pour rge ty - Le prestataire a confirmé la nouvelle date pour votre réservation du service plombérie.',3,'',12,1),(45,'2025-06-12 22:00:40.468146','21','Notification pour rge ty - Votre réservation pour plombérie a été acceptée.',3,'',12,1),(46,'2025-06-12 22:00:40.468194','20','Notification pour baka@gmail.com - Nouvelle demande de réservation pour votre service plombérie.',3,'',12,1),(47,'2025-06-12 22:00:40.468239','19','Notification pour beke ker - La réservation du 2025-06-11 à 15:04:00 pour votre service plombérie a été automatiquement marquée comme terminée.',3,'',12,1),(48,'2025-06-12 22:00:40.468286','18','Notification pour rge ty - Votre réservation du 2025-06-11 à 15:04:00 pour le service plombérie a été automatiquement marquée comme terminée.',3,'',12,1),(49,'2025-06-12 22:00:40.468334','17','Notification pour rge ty - Votre réservation pour plombérie a été acceptée.',3,'',12,1),(50,'2025-06-12 22:00:40.468387','16','Notification pour beke ker - Nouvelle demande de réservation pour votre service plombérie.',3,'',12,1),(51,'2025-06-12 22:00:40.468456','15','Notification pour rge ty - Le prestataire a confirmé la nouvelle date pour votre réservation du service plombérie.',3,'',12,1),(52,'2025-06-12 22:00:40.468508','13','Notification pour baka@gmail.com - Nouvelle demande de réservation pour votre service plombérie.',3,'',12,1),(53,'2025-06-12 22:00:40.468575','12','Notification pour baka@gmail.com - Le client a confirmé la nouvelle date pour la réservation du service Entretien piscine.',3,'',12,1),(54,'2025-06-12 22:00:40.468622','11','Notification pour baka@gmail.com - Nouvelle demande de réservation pour votre service Entretien piscine.',3,'',12,1),(55,'2025-06-12 22:00:40.468681','9','Notification pour baka@gmail.com - Nouvelle demande de réservation pour votre service Entretien piscine.',3,'',12,1),(56,'2025-06-12 22:00:54.414199','4','Avis de rge ty - 3/5',3,'',9,1),(57,'2025-06-12 22:00:54.414277','3','Avis de rge ty - 3/5',3,'',9,1),(58,'2025-06-16 23:18:57.572024','10','uz o (Abidjan et environs)',3,'',8,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (14,'accounts','contactutilisateur'),(6,'accounts','customuser'),(13,'accounts','typecontact'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(9,'reservation','avis'),(15,'reservation','message'),(18,'reservation','newsletteremail'),(12,'reservation','notification'),(8,'reservation','prestataire'),(16,'reservation','prestatairebanni'),(11,'reservation','reservation'),(7,'reservation','service'),(10,'reservation','serviceoffert'),(17,'reservation','signalement'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-06-05 21:56:32.212397'),(2,'contenttypes','0002_remove_content_type_name','2025-06-05 21:56:37.628181'),(3,'auth','0001_initial','2025-06-05 21:56:54.420404'),(4,'auth','0002_alter_permission_name_max_length','2025-06-05 21:56:57.911787'),(5,'auth','0003_alter_user_email_max_length','2025-06-05 21:56:58.299677'),(6,'auth','0004_alter_user_username_opts','2025-06-05 21:56:58.574640'),(7,'auth','0005_alter_user_last_login_null','2025-06-05 21:56:58.865302'),(8,'auth','0006_require_contenttypes_0002','2025-06-05 21:56:59.087820'),(9,'auth','0007_alter_validators_add_error_messages','2025-06-05 21:56:59.331827'),(10,'auth','0008_alter_user_username_max_length','2025-06-05 21:56:59.704737'),(11,'auth','0009_alter_user_last_name_max_length','2025-06-05 21:57:00.082286'),(12,'auth','0010_alter_group_name_max_length','2025-06-05 21:57:00.971701'),(13,'auth','0011_update_proxy_permissions','2025-06-05 21:57:01.275497'),(14,'auth','0012_alter_user_first_name_max_length','2025-06-05 21:57:01.424501'),(15,'accounts','0001_initial','2025-06-05 21:57:35.075498'),(16,'admin','0001_initial','2025-06-05 21:57:47.107199'),(17,'admin','0002_logentry_remove_auto_add','2025-06-05 21:57:47.307260'),(18,'admin','0003_logentry_add_action_flag_choices','2025-06-05 21:57:47.547496'),(19,'reservation','0001_initial','2025-06-05 21:58:26.971929'),(20,'sessions','0001_initial','2025-06-05 21:58:29.346019'),(21,'reservation','0002_reservation_nouvelle_date_reservation_nouvelle_heure_and_more','2025-06-10 21:12:27.531110'),(22,'reservation','0003_reservation_reporteur','2025-06-10 21:52:49.644526'),(23,'reservation','0004_alter_reservation_statut','2025-06-10 22:26:56.736588'),(24,'reservation','0005_alter_avis_date_alter_avis_note_and_more','2025-06-11 09:14:55.386968'),(25,'reservation','0006_notification','2025-06-11 10:43:22.833115'),(26,'reservation','0007_notification_auto_alter_reservation_statut','2025-06-11 18:10:49.007086'),(27,'accounts','0002_typecontact_contactutilisateur','2025-06-11 18:59:57.080883'),(28,'accounts','0003_alter_customuser_role','2025-06-11 22:28:22.014033'),(29,'reservation','0008_message','2025-06-12 08:10:55.026870'),(30,'reservation','0009_prestatairebanni_signalement','2025-06-13 00:45:22.508229'),(31,'reservation','0010_remove_message_is_read_message_signalement_and_more','2025-06-13 01:48:48.321881'),(32,'reservation','0011_message_is_read','2025-06-13 02:22:51.171131'),(33,'reservation','0012_newsletteremail','2025-06-13 02:59:59.305271'),(34,'reservation','0013_alter_avis_options_alter_message_options_and_more','2025-06-13 16:24:55.502341'),(35,'accounts','0004_alter_customuser_options','2025-06-14 22:36:44.819057'),(36,'accounts','0005_customuser_photo','2025-06-15 03:18:22.059367'),(37,'accounts','0006_alter_contactutilisateur_options_and_more','2025-06-16 03:32:14.899744'),(38,'accounts','0007_alter_contactutilisateur_options_and_more','2025-06-16 04:12:44.376103'),(39,'reservation','0014_alter_prestataire_utilisateur','2025-06-16 14:24:02.245035'),(40,'accounts','0006_rename_valeur_contactutilisateur_contact','2025-06-16 15:27:56.249847');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_general_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('3gecva4ftlt2gg7a9j3dlqdnys0xtwbr','.eJxVjDsOwjAQBe_iGlmO17-lpM8ZLK_X4ABypDipEHeHSCmgfTPzXiKmba1x62WJE4uzGMTpd6OUH6XtgO-p3WaZ57YuE8ldkQftcpy5PC-H-3dQU6_fGpz1mYoKpphsDVvSwNoxk796A5wdhmAwASElDAw5KNZqUOAMagTx_gDiCTdR:1uRJd2:Hl0gNMH-CD-SJD4D5C0NfYnedcw0tZo703O7Ov3eV7I','2025-06-30 23:52:40.940882'),('76mtk25cc40c8qpb2bb9hjuikvqnh1qw','.eJxVjDsOwjAQBe_iGlmO17-lpM8ZLK_X4ABypDipEHeHSCmgfTPzXiKmba1x62WJE4uzGMTpd6OUH6XtgO-p3WaZ57YuE8ldkQftcpy5PC-H-3dQU6_fGpz1mYoKpphsDVvSwNoxk796A5wdhmAwASElDAw5KNZqUOAMagTx_gDiCTdR:1uPHW3:Z4_nNXJYVbYuVXqtiLd__UwWTThJnIxkwgf6fAXG9v4','2025-06-25 09:13:03.042691');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservation_avis`
--

DROP TABLE IF EXISTS `reservation_avis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservation_avis` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `note` smallint unsigned NOT NULL,
  `commentaire` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `date` date NOT NULL,
  `client_id` bigint NOT NULL,
  `prestataire_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `reservation_avis_client_id_prestataire_id_5acd6469_uniq` (`client_id`,`prestataire_id`),
  KEY `reservation_avis_prestataire_id_5591bb40_fk_reservati` (`prestataire_id`),
  CONSTRAINT `reservation_avis_client_id_639493fa_fk_accounts_customuser_id` FOREIGN KEY (`client_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `reservation_avis_prestataire_id_5591bb40_fk_reservati` FOREIGN KEY (`prestataire_id`) REFERENCES `reservation_prestataire` (`id`),
  CONSTRAINT `reservation_avis_note_b96c7bc6_check` CHECK ((`note` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservation_avis`
--

LOCK TABLES `reservation_avis` WRITE;
/*!40000 ALTER TABLE `reservation_avis` DISABLE KEYS */;
INSERT INTO `reservation_avis` VALUES (5,3,'Il fut à la hauteur du service et j\'ai été satisfais','2025-06-12',4,4),(7,3,'pas mal mais peut s\'améliorer','2025-06-15',11,5),(8,4,'C\'était un bon prestataire et ile maitrise son travail','2025-06-15',5,1),(9,2,'pas bon et  travail mal','2025-06-16',22,2);
/*!40000 ALTER TABLE `reservation_avis` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservation_message`
--

DROP TABLE IF EXISTS `reservation_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservation_message` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `content` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `recipient_id` bigint NOT NULL,
  `reservation_id` bigint DEFAULT NULL,
  `sender_id` bigint NOT NULL,
  `signalement_id` bigint DEFAULT NULL,
  `is_read` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `reservation_message_recipient_id_7a6e9936_fk_accounts_` (`recipient_id`),
  KEY `reservation_message_reservation_id_f52bfb01_fk_reservati` (`reservation_id`),
  KEY `reservation_message_sender_id_9ec68a46_fk_accounts_customuser_id` (`sender_id`),
  KEY `reservation_message_signalement_id_97df9e80_fk_reservati` (`signalement_id`),
  CONSTRAINT `reservation_message_recipient_id_7a6e9936_fk_accounts_` FOREIGN KEY (`recipient_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `reservation_message_reservation_id_f52bfb01_fk_reservati` FOREIGN KEY (`reservation_id`) REFERENCES `reservation_reservation` (`id`),
  CONSTRAINT `reservation_message_sender_id_9ec68a46_fk_accounts_customuser_id` FOREIGN KEY (`sender_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `reservation_message_signalement_id_97df9e80_fk_reservati` FOREIGN KEY (`signalement_id`) REFERENCES `reservation_signalement` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservation_message`
--

LOCK TABLES `reservation_message` WRITE;
/*!40000 ALTER TABLE `reservation_message` DISABLE KEYS */;
INSERT INTO `reservation_message` VALUES (1,'salut','2025-06-12 08:16:15.048350',5,NULL,4,NULL,0),(2,'sali','2025-06-12 08:17:29.074056',2,NULL,4,NULL,0),(3,'que voulez vous','2025-06-12 08:18:43.553120',5,NULL,2,NULL,0),(4,'je ne reçoit pas','2025-06-12 08:20:26.596109',2,NULL,4,NULL,0),(5,'c\'est bizare','2025-06-12 08:21:20.498153',4,NULL,2,NULL,0),(6,'Salut','2025-06-12 19:06:16.985375',1,NULL,4,NULL,0),(7,'c\'est bon merci','2025-06-14 01:37:43.976398',4,NULL,4,NULL,0),(8,'Merci pour votre confiance','2025-06-14 02:00:11.507850',4,NULL,8,NULL,0),(9,'Salaut','2025-06-14 23:26:58.605078',4,22,3,NULL,1),(10,'Merci pour votre honnêteté','2025-06-14 23:28:32.160034',3,22,4,NULL,1),(11,'hshdozosjkq','2025-06-14 23:28:59.885350',3,22,4,NULL,1),(12,'Salut','2025-06-14 23:30:08.097984',13,NULL,1,NULL,0),(13,'oui salut un problème','2025-06-15 00:13:30.315659',1,NULL,13,NULL,0),(15,'monsieur','2025-06-15 06:37:12.940501',7,NULL,1,NULL,0),(16,'pourquoi me signalez vous?','2025-06-15 06:38:39.289291',4,21,7,NULL,1),(17,'désolé mais il le fallait','2025-06-15 06:39:47.622833',7,21,4,NULL,0),(18,'Salut','2025-06-15 18:01:55.726616',8,27,11,NULL,1),(19,'c\'est','2025-06-15 19:40:09.224810',5,28,2,NULL,0),(20,'Je ne comprend riend','2025-06-16 03:47:42.401969',4,22,3,NULL,1),(21,'Merci pour votre confiance je ferai de mon mieux','2025-06-16 04:22:27.687036',22,29,3,NULL,0);
/*!40000 ALTER TABLE `reservation_message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservation_newsletteremail`
--

DROP TABLE IF EXISTS `reservation_newsletteremail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservation_newsletteremail` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(254) COLLATE utf8mb4_general_ci NOT NULL,
  `date_inscription` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservation_newsletteremail`
--

LOCK TABLES `reservation_newsletteremail` WRITE;
/*!40000 ALTER TABLE `reservation_newsletteremail` DISABLE KEYS */;
INSERT INTO `reservation_newsletteremail` VALUES (1,'baka@gmail.com','2025-06-13 03:12:25.902427');
/*!40000 ALTER TABLE `reservation_newsletteremail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservation_notification`
--

DROP TABLE IF EXISTS `reservation_notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservation_notification` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `date` datetime(6) NOT NULL,
  `lu` tinyint(1) NOT NULL,
  `utilisateur_id` bigint NOT NULL,
  `auto` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `reservation_notifica_utilisateur_id_09ac762f_fk_accounts_` (`utilisateur_id`),
  CONSTRAINT `reservation_notifica_utilisateur_id_09ac762f_fk_accounts_` FOREIGN KEY (`utilisateur_id`) REFERENCES `accounts_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservation_notification`
--

LOCK TABLES `reservation_notification` WRITE;
/*!40000 ALTER TABLE `reservation_notification` DISABLE KEYS */;
INSERT INTO `reservation_notification` VALUES (31,'Nouvelle demande de réservation pour votre service Assistant virtuel.','2025-06-12 22:13:09.137297',1,7,0),(32,'Nouvelle demande de réservation pour votre service plombérie.','2025-06-13 02:40:45.866799',1,3,0),(33,'Vous avez été signalé pour travail mal fait. Vous pouvez vous défendre.','2025-06-13 03:22:35.407851',1,7,1),(34,'Vous avez été signalé pour travail mal fait. Vous pouvez vous défendre.','2025-06-13 03:43:38.580178',1,7,1),(35,'Vous avez été averti suite à un signalement pour : travail mal fait.','2025-06-13 03:47:54.670696',1,7,1),(36,'Vous avez été averti suite à un signalement pour : travail mal fait.','2025-06-13 03:48:59.270281',1,7,1),(38,'Votre réservation pour Ménage a été acceptée.','2025-06-14 01:34:23.166845',1,4,0),(39,'Le prestataire a confirmé la nouvelle date pour votre réservation du service plombérie.','2025-06-14 01:36:22.617980',1,4,0),(48,'Nouvelle demande de réservation pour votre service Peinture.','2025-06-14 03:34:01.679926',1,13,0),(49,'Votre réservation pour Peinture a été acceptée.','2025-06-14 03:34:40.939013',1,4,0),(50,'Vous avez été signalé pour Arnaque. Vous pouvez vous défendre.','2025-06-14 03:35:55.306097',1,13,1),(51,'Vous avez été averti suite à un signalement pour : Arnaque.','2025-06-14 03:37:50.493976',1,13,1),(52,'Vous avez été signalé pour Arnaque. Vous pouvez vous défendre.','2025-06-14 04:12:16.073044',1,13,1),(53,'Vous avez été averti suite à un signalement pour : Arnaque.','2025-06-14 04:13:50.486168',1,13,1),(54,'Nouveau message de beke ker concernant la réservation.','2025-06-14 23:26:58.782011',1,4,1),(55,'Nouveau message de rge ty concernant la réservation.','2025-06-14 23:28:32.506305',1,3,1),(56,'Nouveau message de rge ty concernant la réservation.','2025-06-14 23:29:00.202344',1,3,1),(57,'Nouveau message de rge ty concernant la réservation.','2025-06-15 00:17:13.882238',1,13,1),(60,'Nouvelle demande de réservation pour votre service plombérie.','2025-06-15 06:12:30.508975',1,2,0),(61,'Votre réservation pour plombérie a été acceptée.','2025-06-15 06:13:36.773814',1,5,0),(62,'Vous avez été signalé pour Arnaque. Vous pouvez vous défendre.','2025-06-15 06:34:06.095389',1,2,1),(63,'Nouveau message de Inza Gui concernant la réservation.','2025-06-15 06:38:39.543389',1,4,1),(64,'Nouveau message de rge ty concernant la réservation.','2025-06-15 06:39:47.884634',0,7,1),(66,'Vous avez été averti suite à un signalement pour : Arnaque.','2025-06-15 18:05:15.907200',1,2,1),(67,'Nouveau message de baka@gmail.com concernant la réservation.','2025-06-15 19:40:09.603044',0,5,1),(68,'Nouveau message de beke ker concernant la réservation.','2025-06-16 03:47:43.182427',1,4,1),(69,'Nouvelle demande de réservation pour votre service plombérie.','2025-06-16 04:21:14.615237',1,3,0),(70,'Votre réservation pour plombérie a été acceptée.','2025-06-16 04:21:59.686359',1,22,0),(71,'Nouveau message de beke ker concernant la réservation.','2025-06-16 04:22:28.043565',1,22,1),(72,'Vous avez été signalé pour travail mal fait. Vous pouvez vous défendre.','2025-06-16 04:26:11.597537',1,3,1);
/*!40000 ALTER TABLE `reservation_notification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservation_prestataire`
--

DROP TABLE IF EXISTS `reservation_prestataire`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservation_prestataire` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `zone` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `photo` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `evaluation_moyenne` double NOT NULL,
  `utilisateur_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `utilisateur_id` (`utilisateur_id`),
  CONSTRAINT `reservation_prestata_utilisateur_id_8d4edd18_fk_accounts_` FOREIGN KEY (`utilisateur_id`) REFERENCES `accounts_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservation_prestataire`
--

LOCK TABLES `reservation_prestataire` WRITE;
/*!40000 ALTER TABLE `reservation_prestataire` DISABLE KEYS */;
INSERT INTO `reservation_prestataire` VALUES (1,'yopuogon','prestataires/photos/IMG-20220501-WA0097_E8CJCHh.jpg',0,2),(2,'Abidjan et environs','prestataires/photos/Screenshot_2022-10-17-06-22-34_xfUreSI.png',0,3),(3,'Région de béré','prestataires/photos/Capture_décran_2025-06-11_080955.png',0,6),(4,'Abidjan et environs','prestataires/photos/WhatsApp_Image_2025-06-11_à_08.16.12_e0b83eba.jpg',0,7),(5,'Abobo et Mankono','prestataires/photos/WhatsApp_Image_2025-06-11_à_20.05.12_eeae0438.jpg',0,8),(6,'Sans pédro','prestataires/photos/WhatsApp_Image_2025-06-11_à_20.04.39_dc025159.jpg',0,9),(9,'bouaké et yamoussoukro','prestataires/photos/c1_3d9iAVj.png',0,13),(11,'bouaké et yamoussoukro','prestataires/photos/Capture_décran_2025-06-16_011555.png',0,23),(12,'bouaké et yamoussoukro','prestataires/photos/Capture_décran_2025-05-24_215831.png',0,27),(13,'Abidjan et environs','prestataires/photos/Capture_décran_2025-06-09_180914.png',0,14);
/*!40000 ALTER TABLE `reservation_prestataire` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservation_prestatairebanni`
--

DROP TABLE IF EXISTS `reservation_prestatairebanni`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservation_prestatairebanni` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(254) COLLATE utf8mb4_general_ci NOT NULL,
  `telephone` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `nom` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `date_bannissement` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservation_prestatairebanni`
--

LOCK TABLES `reservation_prestatairebanni` WRITE;
/*!40000 ALTER TABLE `reservation_prestatairebanni` DISABLE KEYS */;
INSERT INTO `reservation_prestatairebanni` VALUES (1,'her@gmail.com','Inconnu','he re','2025-06-14 03:15:14.476670');
/*!40000 ALTER TABLE `reservation_prestatairebanni` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservation_reservation`
--

DROP TABLE IF EXISTS `reservation_reservation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservation_reservation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `heure` time(6) NOT NULL,
  `statut` varchar(60) COLLATE utf8mb4_general_ci NOT NULL,
  `mode_paiement` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `client_id` bigint NOT NULL,
  `service_offert_id` bigint NOT NULL,
  `nouvelle_date` date DEFAULT NULL,
  `nouvelle_heure` time(6) DEFAULT NULL,
  `report_en_attente` tinyint(1) NOT NULL,
  `reporteur_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `reservation_reservat_client_id_929ea86a_fk_accounts_` (`client_id`),
  KEY `reservation_reservat_service_offert_id_5d131877_fk_reservati` (`service_offert_id`),
  KEY `reservation_reservat_reporteur_id_786123e4_fk_accounts_` (`reporteur_id`),
  CONSTRAINT `reservation_reservat_client_id_929ea86a_fk_accounts_` FOREIGN KEY (`client_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `reservation_reservat_reporteur_id_786123e4_fk_accounts_` FOREIGN KEY (`reporteur_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `reservation_reservat_service_offert_id_5d131877_fk_reservati` FOREIGN KEY (`service_offert_id`) REFERENCES `reservation_serviceoffert` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservation_reservation`
--

LOCK TABLES `reservation_reservation` WRITE;
/*!40000 ALTER TABLE `reservation_reservation` DISABLE KEYS */;
INSERT INTO `reservation_reservation` VALUES (21,'2025-06-19','10:13:00.000000','terminée','',4,6,NULL,NULL,0,7),(22,'2025-06-19','05:33:00.000000','reportée','',4,1,NULL,NULL,0,NULL),(23,'2025-06-18','06:32:00.000000','terminée','',4,9,NULL,NULL,0,NULL),(26,'2025-06-26','08:33:00.000000','terminée','',4,12,NULL,NULL,0,NULL),(27,'2025-06-18','07:42:00.000000','terminée','',11,9,NULL,NULL,0,NULL),(28,'2025-06-18','11:12:00.000000','terminée','',5,4,NULL,NULL,0,NULL),(29,'2025-06-24','09:21:00.000000','terminée','',22,1,NULL,NULL,0,NULL);
/*!40000 ALTER TABLE `reservation_reservation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservation_service`
--

DROP TABLE IF EXISTS `reservation_service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservation_service` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nom` (`nom`)
) ENGINE=InnoDB AUTO_INCREMENT=292 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservation_service`
--

LOCK TABLES `reservation_service` WRITE;
/*!40000 ALTER TABLE `reservation_service` DISABLE KEYS */;
INSERT INTO `reservation_service` VALUES (83,'Acupuncteur'),(100,'Agent de sécurité'),(46,'Aide aux personnes âgées'),(47,'Aide aux personnes handicapées'),(124,'Animation'),(68,'Animation enfants'),(72,'Architecte d’intérieur'),(23,'Assistance administrative'),(95,'Assistant virtuel'),(104,'Baby-sitting'),(18,'Babysitting'),(134,'Boucherie'),(132,'Boulangerie'),(109,'Bricolage'),(80,'Bronzage'),(127,'Chanteur'),(133,'Charcuterie'),(32,'Chauffage'),(101,'Chauffeur privé'),(63,'Chef à domicile'),(33,'Climatisation'),(70,'Clown à domicile'),(36,'Coach sportif'),(7,'Coiffure'),(94,'Community manager'),(114,'Comptabilité'),(73,'Conseiller en image'),(96,'Conseiller fiscal'),(97,'Conseiller juridique'),(90,'Correcteur'),(21,'Cours de cuisine'),(19,'Cours de musique'),(20,'Cours de sport'),(111,'Cours particuliers'),(98,'Courtier en assurance'),(99,'Courtier immobilier'),(17,'Couture'),(108,'Cuisine'),(29,'Débarras'),(129,'Décoration'),(71,'Décoration intérieure'),(15,'Déménagement'),(56,'Dépannage internet'),(28,'Dératisation'),(27,'Désinsectisation'),(93,'Développeur web'),(37,'Diététicien'),(125,'DJ'),(67,'DJ à domicile'),(50,'Dressage d’animaux'),(3,'Électricité'),(60,'Entretien moto'),(26,'Entretien piscine'),(79,'Epilation'),(42,'Ergothérapeute'),(8,'Esthétique'),(130,'Fleuriste'),(51,'Garde d’animaux'),(10,'Garde d’enfants'),(123,'Gardiennage'),(115,'Gestion administrative'),(91,'Graphiste'),(45,'Infirmier à domicile'),(12,'Informatique'),(52,'Installation alarme'),(53,'Installation domotique'),(58,'Installation parabole'),(57,'Installation TV'),(88,'Interprète'),(6,'Jardinage'),(44,'Kinésithérapeute'),(116,'Livraison'),(22,'Livraison de courses'),(62,'Livraison repas'),(121,'Location matériel'),(120,'Location utilitaire'),(119,'Location voiture'),(106,'Maçonnerie'),(69,'Magicien à domicile'),(76,'Manucure'),(78,'Maquillage'),(9,'Massage'),(81,'Massage bébé'),(2,'Mécanique'),(4,'Ménage'),(107,'Menuiserie'),(16,'Montage de meubles'),(126,'Musicien'),(102,'Nettoyage'),(25,'Nettoyage de tapis'),(24,'Nettoyage de vitres'),(59,'Nettoyage voiture'),(38,'Nutritionniste'),(66,'Organisation d’événements'),(128,'Organisation événement'),(41,'Orthophoniste'),(43,'Ostéopathe'),(131,'Pâtisserie'),(64,'Pâtissier à domicile'),(77,'Pédicure'),(14,'Peinture'),(74,'Personal shopper'),(30,'Petits travaux'),(34,'Photographie'),(1,'plombérie'),(135,'Poissonnerie'),(85,'Professeur de danse'),(86,'Professeur de langues'),(84,'Professeur de yoga'),(48,'Promenade d’animaux'),(40,'Psychologue'),(89,'Rédacteur'),(113,'Rédaction'),(82,'Réflexologue'),(13,'Réparation électroménager'),(55,'Réparation ordinateur'),(54,'Réparation smartphone'),(110,'Réparation téléphone'),(61,'Réparation vélo'),(5,'Repassage'),(122,'Sécurité'),(31,'Serrurerie'),(39,'Sophrologue'),(11,'Soutien scolaire'),(75,'Styliste'),(117,'Taxi'),(49,'Toilettage d’animaux'),(87,'Traducteur'),(112,'Traduction'),(65,'Traiteur'),(283,'Vente abris de jardin'),(139,'Vente accessoires'),(167,'Vente accessoires animaux'),(188,'Vente accessoires jeux'),(204,'Vente adaptateurs'),(212,'Vente alarmes'),(199,'Vente ampoules'),(166,'Vente animaux'),(174,'Vente antiquités'),(105,'Vente appareils photo'),(242,'Vente ardoises'),(249,'Vente arrosage'),(173,'Vente art'),(254,'Vente baignoires'),(282,'Vente barbecues'),(201,'Vente batteries'),(273,'Vente batteries solaires'),(144,'Vente bijoux'),(184,'Vente bijoux fantaisie'),(266,'Vente bois'),(239,'Vente briques'),(257,'Vente broyeurs'),(203,'Vente câbles'),(276,'Vente câbles solaires'),(217,'Vente cadenas'),(191,'Vente caméras'),(213,'Vente caméras surveillance'),(227,'Vente carrelage'),(195,'Vente cartouches'),(182,'Vente ceintures'),(181,'Vente chapeaux'),(268,'Vente charbon'),(202,'Vente chargeurs'),(263,'Vente chaudières'),(138,'Vente chaussures'),(265,'Vente cheminées'),(244,'Vente chéneaux'),(236,'Vente ciment'),(247,'Vente citernes'),(218,'Vente clés'),(260,'Vente climatiseurs'),(211,'Vente coffrets'),(233,'Vente colles'),(186,'Vente consoles jeux'),(246,'Vente cuves'),(245,'Vente descentes eaux'),(215,'Vente détecteurs fumée'),(209,'Vente disjoncteurs'),(255,'Vente douches'),(192,'Vente drones'),(143,'Vente électroménager'),(234,'Vente enduits'),(272,'Vente éoliennes'),(162,'Vente équipements sportifs'),(253,'Vente éviers'),(214,'Vente extincteurs'),(228,'Vente faïence'),(220,'Vente fenêtres'),(259,'Vente filtres'),(270,'Vente fioul'),(290,'Vente fontaines'),(258,'Vente fosses septiques'),(196,'Vente fournitures bureau'),(151,'Vente fournitures scolaires'),(136,'Vente fruits et légumes'),(269,'Vente gaz'),(243,'Vente gouttières'),(165,'Vente graines'),(267,'Vente granulés'),(238,'Vente gravier'),(193,'Vente imprimantes'),(163,'Vente instruments musique'),(207,'Vente interrupteurs'),(187,'Vente jeux vidéo'),(149,'Vente jouets'),(198,'Vente lampes'),(252,'Vente lavabos'),(230,'Vente lino'),(150,'Vente livres'),(146,'Vente lunettes'),(159,'Vente matériaux construction'),(152,'Vente matériel informatique'),(153,'Vente matériel médical'),(142,'Vente meubles'),(197,'Vente mobilier bureau'),(145,'Vente montres'),(226,'Vente moquettes'),(155,'Vente motos'),(205,'Vente multiprises'),(172,'Vente objets déco'),(274,'Vente onduleurs'),(141,'Vente ordinateurs'),(161,'Vente outils'),(103,'Vente panneaux clôture'),(271,'Vente panneaux solaires'),(232,'Vente papier peint'),(180,'Vente parapluies'),(240,'Vente parpaings'),(229,'Vente parquet'),(160,'Vente peinture'),(231,'Vente peinture murale'),(288,'Vente pergolas'),(154,'Vente pièces auto'),(158,'Vente pièces détachées'),(200,'Vente piles'),(278,'Vente piscines'),(164,'Vente plantes'),(235,'Vente plâtre'),(264,'Vente poêles'),(248,'Vente pompes'),(286,'Vente portails'),(183,'Vente portefeuilles'),(219,'Vente portes'),(208,'Vente prises'),(277,'Vente prises solaires'),(168,'Vente produits agricoles'),(169,'Vente produits artisanaux'),(147,'Vente produits beauté'),(185,'Vente produits électroniques'),(170,'Vente produits locaux'),(148,'Vente produits ménagers'),(262,'Vente radiateurs'),(190,'Vente radios'),(206,'Vente rallonges'),(275,'Vente régulateurs'),(223,'Vente rideaux'),(251,'Vente robinets'),(237,'Vente sable'),(178,'Vente sacs'),(280,'Vente saunas'),(194,'Vente scanners'),(157,'Vente scooters'),(284,'Vente serres'),(216,'Vente serrures'),(171,'Vente souvenirs'),(279,'Vente spas'),(222,'Vente stores'),(210,'Vente tableaux électriques'),(225,'Vente tapis'),(140,'Vente téléphones'),(189,'Vente télévisions'),(224,'Vente tringles'),(241,'Vente tuiles'),(250,'Vente tuyaux'),(179,'Vente valises'),(156,'Vente vélos'),(261,'Vente ventilateurs'),(137,'Vente vêtements'),(175,'Vente vêtements enfants'),(176,'Vente vêtements femmes'),(177,'Vente vêtements hommes'),(221,'Vente volets'),(256,'Vente WC'),(35,'Vidéaste'),(118,'VTC'),(92,'Webdesigner');
/*!40000 ALTER TABLE `reservation_service` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservation_serviceoffert`
--

DROP TABLE IF EXISTS `reservation_serviceoffert`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservation_serviceoffert` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `prix` decimal(8,2) NOT NULL,
  `description` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `prestataire_id` bigint NOT NULL,
  `service_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `reservation_serviceoffer_prestataire_id_service_i_c0f097aa_uniq` (`prestataire_id`,`service_id`),
  KEY `reservation_serviceo_service_id_afc8c130_fk_reservati` (`service_id`),
  CONSTRAINT `reservation_serviceo_prestataire_id_8d27a7a0_fk_reservati` FOREIGN KEY (`prestataire_id`) REFERENCES `reservation_prestataire` (`id`),
  CONSTRAINT `reservation_serviceo_service_id_afc8c130_fk_reservati` FOREIGN KEY (`service_id`) REFERENCES `reservation_service` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservation_serviceoffert`
--

LOCK TABLES `reservation_serviceoffert` WRITE;
/*!40000 ALTER TABLE `reservation_serviceoffert` DISABLE KEYS */;
INSERT INTO `reservation_serviceoffert` VALUES (1,7000.00,'réparation rapide, je m\'occupe de tout ce qui est réparation et la plombérie',2,1),(3,2348.00,'Je nettoie proprement la piscine, j\'ai des produits désinfectant',1,26),(4,5000.00,'Réparation rapide et plomberie  générale',1,1),(5,5000.00,'Plomberie générale, installation et réparation de canalisations des maison.',3,1),(6,10000.00,'Aide des personnes incapable d\'assurer les services en ligne d\'eux mêmes. Je  les assiste pas à pas et leurs offre un service de qualité',4,95),(9,555.00,'Je nettoie bien les maisons',5,15),(12,600.00,'è\'è\"rijiiei',9,14),(13,4889.00,'hdjdhjdjhqj;kqdkj',1,55),(16,1000.00,'yzuzjhz',2,103),(17,500.00,'677',2,15),(18,600.00,'4hdudsjsf',5,104),(19,788.00,'8duhjzjk',5,105),(20,600.00,'tcdekhefhk',5,34),(21,7000.00,'hslkjet suufbj',5,8),(22,500.00,'ijzkkoieeoajkjkakk',2,8),(23,5000.00,'sjlfzjkkjcs',3,8),(26,6000.00,'hdjkjdjk',3,102),(29,700.00,'hhdjdkfklf',5,149),(30,6000.00,'sJe construit des  maison et fait des plansjdhadaad',11,106),(31,4000.00,'uuidkjdllzklmlc:s,fzkl,fekfk:ef,;:s,fkscsljkejfjekgjek  cnvcq,x,zaqfkdfkklfksdnklzenklz',2,14);
/*!40000 ALTER TABLE `reservation_serviceoffert` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservation_signalement`
--

DROP TABLE IF EXISTS `reservation_signalement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservation_signalement` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `motif` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `preuve` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `date_signalement` datetime(6) NOT NULL,
  `traite` tinyint(1) NOT NULL,
  `defense` longtext COLLATE utf8mb4_general_ci,
  `preuve_defense` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `statut` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `client_id` bigint NOT NULL,
  `prestataire_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `reservation_signalem_client_id_0b546c9f_fk_accounts_` (`client_id`),
  KEY `reservation_signalem_prestataire_id_68074897_fk_reservati` (`prestataire_id`),
  CONSTRAINT `reservation_signalem_client_id_0b546c9f_fk_accounts_` FOREIGN KEY (`client_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `reservation_signalem_prestataire_id_68074897_fk_reservati` FOREIGN KEY (`prestataire_id`) REFERENCES `reservation_prestataire` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservation_signalement`
--

LOCK TABLES `reservation_signalement` WRITE;
/*!40000 ALTER TABLE `reservation_signalement` DISABLE KEYS */;
INSERT INTO `reservation_signalement` VALUES (1,'travail mal fait','duuduifhdfkl','','2025-06-13 03:22:35.074103',1,NULL,'','averti',4,4),(2,'travail mal fait','uhhshjjzjz','preuves_signalement/c4.png','2025-06-13 03:43:36.446485',1,NULL,'','averti',4,4),(5,'Arnaque','uzuzjhsddhj','','2025-06-14 03:35:55.032865',1,NULL,'','averti',4,9),(6,'Arnaque','jejejfj','preuves_signalement/c4_ZfEW6E1.png','2025-06-14 04:12:15.729504',1,'None','','averti',4,9),(7,'Arnaque','malpoli','preuves_signalement/Capture001.png','2025-06-15 06:34:05.841684',1,'je suis innocent','','averti',5,1),(8,'travail mal fait','il n\'a pas bien','','2025-06-16 04:26:10.537238',0,'Je suis innocent','preuves_defense/c4.png','en_attente',22,2);
/*!40000 ALTER TABLE `reservation_signalement` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-17  0:24:20
