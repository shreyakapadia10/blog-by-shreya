-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Feb 28, 2021 at 10:53 AM
-- Server version: 5.7.26
-- PHP Version: 5.6.40

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `myblog`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

DROP TABLE IF EXISTS `contact`;
CREATE TABLE IF NOT EXISTS `contact` (
  `contact_id` int(11) NOT NULL AUTO_INCREMENT,
  `contact_name` varchar(50) NOT NULL,
  `contact_email` varchar(100) NOT NULL,
  `contact_phone` varchar(12) NOT NULL,
  `contact_message` varchar(200) NOT NULL,
  `contact_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`contact_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`contact_id`, `contact_name`, `contact_email`, `contact_phone`, `contact_message`, `contact_date`) VALUES
(1, 'Shreya', 'shreya@gmail.com', '9874563210', 'Test message', '2021-02-28 16:23:29');

-- --------------------------------------------------------

--
-- Table structure for table `post`
--

DROP TABLE IF EXISTS `post`;
CREATE TABLE IF NOT EXISTS `post` (
  `post_id` int(11) NOT NULL AUTO_INCREMENT,
  `post_title` varchar(50) NOT NULL,
  `post_subtitle` varchar(20) NOT NULL,
  `post_content` varchar(1000) NOT NULL,
  `post_slug` varchar(50) NOT NULL,
  `post_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `post_author` varchar(50) NOT NULL,
  `post_img` varchar(50) NOT NULL,
  PRIMARY KEY (`post_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `post`
--

INSERT INTO `post` (`post_id`, `post_title`, `post_subtitle`, `post_content`, `post_slug`, `post_date`, `post_author`, `post_img`) VALUES
(1, 'What is Programming?', 'Learn Programming', 'In this blog post, I will decipher the term “programming” and understand its usage and many other related terms.\r\n\r\nUnderstanding Programming in layman terms\r\nProgramming is a way to “instruct the computer to perform various tasks”.\r\n\r\nConfusing? Let us understand the definition deeply.\r\n\r\n“Instruct the computer”: this basically means that you provide the computer a set of instructions that are written in a language that the computer can understand. The instructions could be of various types. For example:\r\n\r\nAdding 2 numbers,\r\nRounding off a number, etc.\r\nJust like we humans can understand a few languages (English, Spanish, Mandarin, French, etc.), so is the case with computers. Computers understand instructions that are written in a specific syntactical form called a programming language.', 'what-is-programming', '2021-02-28 15:56:04', 'Shreya Kapadia', 'programming-bg.jpg'),
(2, 'What is Flask?', 'Intro to Flask', 'Welcome to Flask’s documentation. Get started with Installation and then get an overview with the Quickstart. There is also a more detailed Tutorial that shows how to create a small but complete application with Flask. Common patterns are described in the Patterns for Flask section. The rest of the docs describe each component of Flask in detail, with a full reference in the API section.\r\n\r\nFlask depends on the Jinja template engine and the Werkzeug WSGI toolkit. The documentation for these libraries can be found at:', 'what-is-flask', '2021-02-28 16:15:07', 'Shreya Kapadia', 'flask.png'),
(3, 'What is Jinja?', 'Intro to Jinja', 'Jinja is a modern and designer-friendly templating language for Python, modelled after Django’s templates. It is fast, widely used and secure with the optional sandboxed template execution environment:\r\nFeatures:\r\n\r\nsandboxed execution\r\n\r\npowerful automatic HTML escaping system for XSS prevention\r\n\r\ntemplate inheritance\r\n\r\ncompiles down to the optimal python code just in time\r\n\r\noptional ahead-of-time template compilation\r\n\r\neasy to debug. Line numbers of exceptions directly point to the correct line in the template.\r\n\r\nconfigurable syntax', 'what-is-jinja', '2021-02-28 16:18:37', 'Shreya Kapadia', 'jinja.png'),
(4, 'What is Python?', 'Learn to Python', 'Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python\'s simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.', 'intro-to-python', '2021-02-28 16:20:16', 'Shreya Kapadia', 'python.png'),
(5, 'What is ReactJS?', 'Intro to ReactJS', 'React is a declarative, efficient, and flexible JavaScript library for building user interfaces. It lets you compose complex UIs from small and isolated pieces of code called “components”.\r\n\r\nReact has a few different kinds of components, but we’ll start with React.Component subclasses:\r\nWe’ll get to the funny XML-like tags soon. We use components to tell React what we want to see on the screen. When our data changes, React will efficiently update and re-render our components.', 'intro-to-reactjs', '2021-02-28 16:20:52', 'Shreya Kapadia', 'react.jfif'),
(7, 'What is GitHub?', 'Intro to GitHub', 'GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.\r\n\r\nThis tutorial teaches you GitHub essentials like repositories, branches, commits, and Pull Requests. You’ll create your own Hello World repository and learn GitHub’s Pull Request workflow, a popular way to create and review code.', 'intro-to-github', '2021-02-28 15:58:48', 'Shreya Kapadia', 'github.jpg');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
