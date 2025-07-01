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

INSERT INTO affirmations (text, author, category) VALUES
("I am enough just as I am.", "Jane Moore", "self-love"),
("I radiate self-love and compassion.", "Juliette Song", "self-love"),
("The future depends on what you do today.", "Mahatma Gandhi", "motivation"),
("Push yourself, because no one else is going to do it for you.", "Tyler Knox", "motivation"),
("Gratitude turns what we have into enough.", "Melody Beattie", "gratitude"),
("Every day may not be good, but there’s something good in every day.", "Alice Freeman", "gratitude"),
("Believe you can and you're halfway there.", "Theodore Roosevelt", "confidence"),
("Confidence comes not from always being right but from not fearing to be wrong.", "Peter T. McIntyre", "confidence"),
("Success is not the key to happiness. Happiness is the key to success.", "Albert Schweitzer", "success"),
("Don't watch the clock; do what it does. Keep going.", "Sam Levenson", "success"),
("You can’t heal what you don’t reveal.", "Jay-Z", "healing"),
("Healing is an art. It takes time, it takes practice, it takes love.", "Maza Dohta", "healing"),
("Abundance is not something we acquire. It is something we tune into.", "Wayne Dyer", "abundance"),
("I attract prosperity with every thought I think.", "Sophie Lin", "abundance"),
("Your mental health is a priority. Your happiness is an essential.", "Lana Cooper", "mental-health"),
("It’s okay to not be okay.", "Unknown", "mental-health"),
("You deserve to be with someone who makes you feel like the best version of yourself.", "Alexis Bloom", "relationships"),
("Love is not about possession. Love is about appreciation.", "Osho", "relationships"),
("The soul always knows what to do to heal itself.", "Caroline Myss", "spirituality"),
("I am aligned with the energy of the universe.", "Ezra Toma", "spirituality"),
("Peace comes from within. Do not seek it without.", "Buddha", "peace"),
("Breathe in peace, breathe out stress.", "Chloe Rey", "peace"),
("The only way to grow is to challenge yourself.", "Jordan Hale", "growth"),
("Be not afraid of growing slowly, be afraid only of standing still.", "Chinese Proverb", "growth"),
("She stood in the storm and when the wind did not blow her way, she adjusted her sails.", "Elizabeth Edwards", "resilience"),
("Tough times never last, but tough people do.", "Robert H. Schuller", "resilience"),
("Forgiveness is the fragrance that the violet sheds on the heel that has crushed it.", "Mark Twain", "forgiveness"),
("Forgive others, not because they deserve forgiveness, but because you deserve peace.", "Jonathan Evans", "forgiveness"),
("Keep your face always toward the sunshine—and shadows will fall behind you.", "Walt Whitman", "positivity"),
("Positive anything is better than negative nothing.", "Elbert Hubbard", "positivity");




SELECT *
FROM affirmations;