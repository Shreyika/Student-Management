-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 20, 2019 at 06:13 AM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `project`
--

-- --------------------------------------------------------

--
-- Table structure for table `sample4`
--

CREATE TABLE `sample4` (
  `firstname` varchar(20) NOT NULL,
  `lastname` varchar(20) NOT NULL,
  `studentId` int(11) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `date` int(11) NOT NULL,
  `month` int(11) NOT NULL,
  `year` int(11) NOT NULL,
  `contact` int(11) NOT NULL,
  `emailid` varchar(30) NOT NULL,
  `rollno` int(11) NOT NULL,
  `address` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sample4`
--

INSERT INTO `sample4` (`firstname`, `lastname`, `studentId`, `gender`, `date`, `month`, `year`, `contact`, `emailid`, `rollno`, `address`) VALUES
('fgh', '', 0, 'select', 1, 1, 1972, 0, '', 0, ''),
('hhh', '', 0, 'select', 1, 1, 1972, 523644, '', 0, ''),
('shreyka', 'dsvfdk', 6, 'Female', 1, 1, 1972, 0, 'shrey@gmail.com', 3, 'shrehx'),
('fvhgjfdv', 'kvksvf', 4, 'Female', 3, 4, 1982, 1234567891, 'shrey@gmail.com', 4, 'gvjsgv'),
('fvhgjfdv', 'kvksvf', 4, 'Female', 3, 4, 1982, 1234567891, 'shrey@gmail.com', 4, 'gvjsgv'),
('fnjf', 'gr', 0, 'select', 1, 1, 1972, 2147483647, '', 0, ''),
('fnjf', 'gr', 0, 'select', 1, 1, 1972, 2147483647, '', 0, ''),
('shreyika', 'mandale', 5, 'Female', 5, 5, 1978, 45678923, 'shrey@gmail.com', 3, 'dhfifiuwfksaf'),
('kartik', 'rane', 4, 'Male', 1, 1, 1972, 12345, 'asdfg@', 6, ''),
('hvkfsx', 'zckhzc', 5, 'select', 1, 1, 1972, 0, '', 0, ''),
('hvkfsx', 'zckhzc', 5, 'select', 1, 1, 1972, 4563, '', 0, ''),
('kabir', 'jaiswal', 5, 'Female', 6, 7, 2000, 1234567891, 'kabir@gmial.com', 5, '201 A wing vasudev b');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
