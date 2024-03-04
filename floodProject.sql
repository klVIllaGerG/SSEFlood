-- MySQL dump 10.13  Distrib 8.0.35, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: test
-- ------------------------------------------------------
-- Server version	8.0.35

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
-- Table structure for table `db_account`
--

DROP TABLE IF EXISTS `db_account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `db_account` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(255) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `role` varchar(255) DEFAULT NULL,
  `register_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `db_account_username_IDX` (`username`) USING BTREE,
  KEY `db_account_email_IDX` (`email`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `db_account`
--

LOCK TABLES `db_account` WRITE;
/*!40000 ALTER TABLE `db_account` DISABLE KEYS */;
INSERT INTO `db_account` VALUES (3,'805094070@qq.com','admintes','$2a$10$bmf6UUANdq90rjDBys4sP.glAVUykIEER57qOT1TY89DDc4QR68oW','user','2024-01-05 16:02:25'),(5,'1872686384@qq.com','testuser','$2a$10$luuxgHzxzoytpki4ReG8guSq7hmsjhDGRvY/civVC6OZmYpJIaGCK','user','2024-01-06 15:25:14'),(6,'3414733492@qq.com','xlj','$2a$10$6ld2CdiCMa6lGHD2uvCDNO2hs8WEBBZ1VDkmLElbFV4cgJRL07T4S','user','2024-01-06 16:04:03'),(7,'3236825174@qq.com','wjw','$2a$10$1ZYUXNVZrwaOXu/D7MCzwO3ol1H5VBIVAoG2qsykaRyZo.o.DWBl.','user','2024-01-06 20:23:23');
/*!40000 ALTER TABLE `db_account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `persistent_logins`
--

DROP TABLE IF EXISTS `persistent_logins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `persistent_logins` (
  `username` varchar(64) NOT NULL,
  `series` varchar(64) NOT NULL,
  `token` varchar(64) NOT NULL,
  `last_used` timestamp NOT NULL,
  PRIMARY KEY (`series`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `persistent_logins`
--

LOCK TABLES `persistent_logins` WRITE;
/*!40000 ALTER TABLE `persistent_logins` DISABLE KEYS */;
/*!40000 ALTER TABLE `persistent_logins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suggestion`
--

DROP TABLE IF EXISTS `suggestion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suggestion` (
  `category` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `suggestions` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  PRIMARY KEY (`category`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suggestion`
--

LOCK TABLES `suggestion` WRITE;
/*!40000 ALTER TABLE `suggestion` DISABLE KEYS */;
INSERT INTO `suggestion` VALUES ('洪水不易发','本地洪水不易发，要多加关注洪水新闻，学习洪水知识，未雨绸缪！'),('洪水易发','根据敏感性测绘图可以看出：广州西南部地区洪水易发生，其余地方零零散散也有洪水发生的可能性，整体敏感性偏高。要高度重视城市周边水利工程安全，开展安全评估；加强调度管理，严格执行调度规则，减轻大坝压力；加强安全监测和险情巡查，发现问题及时处置；加强水情监测预报，在保障安全的前提下加强雨洪资源利用，防止集中弃水与暴雨叠加；严防极端情况下溃坝，加剧下游灾害。');
/*!40000 ALTER TABLE `suggestion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'test'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-10 21:52:21
