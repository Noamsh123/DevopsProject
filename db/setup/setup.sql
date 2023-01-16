CREATE DATABASE IF NOT EXISTS `players`;

-- --------------------------------------------------------

--
-- Table structure for table `containers-registered`
--

USE players;


CREATE TABLE IF NOT EXISTS `active_players` (
  `player_id` varchar(15) NOT NULL,
  `age` int(12) DEFAULT NULL,
  `country` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`player_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10001 ;