CREATE DATABASE affirmations_db;
USE affirmations_db;

CREATE TABLE affirmations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    text TEXT NOT NULL,
    author VARCHAR(100),
    category ENUM ('self-love', 
    'motivation', 
    'gratitude',
    'confidence',
    'success',
    'healing',
    'abundance',
    'mental-health',
	'relationships',
    'spirituality',
    'peace',
    'growth',
    'resilience',
    'forgiveness',
    'positivity') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



SELECT *
FROM affirmations;