-- publications_dump.sql

-- Clear existing data (if any)
DELETE FROM publications_publication_citations;
DELETE FROM publications_publication_authors;
DELETE FROM publications_publication;
DELETE FROM publications_author;
DELETE FROM publications_issue;
DELETE FROM publications_edition;
DELETE FROM publications_category;

-- Categories
INSERT INTO publications_category (id, name, description) VALUES
(1, 'Research Article', 'Original research contributions with comprehensive methodology and results'),
(2, 'Review Article', 'Critical analysis and summary of existing research on a specific topic'),
(3, 'Case Study', 'Detailed analysis of specific cases or instances'),
(4, 'Technical Note', 'Brief technical communications and methodological advances'),
(5, 'Commentary', 'Expert opinion and perspective on current topics');

-- Editions
INSERT INTO publications_edition (id, name, description) VALUES
(1, 'Journal of Computer Science', 'Peer-reviewed journal focusing on computer science research'),
(2, 'Data Science Review', 'Publication dedicated to advances in data science and analytics'),
(3, 'AI Quarterly', 'Quarterly publication on artificial intelligence developments');

-- Issues
INSERT INTO publications_issue (id, edition_id, number, date, description) VALUES
(1, 1, 1, '2023-01-15', 'January 2023 Issue'),
(2, 1, 2, '2023-04-15', 'April 2023 Issue'),
(3, 2, 1, '2023-03-01', 'Spring 2023 Issue'),
(4, 3, 1, '2023-01-01', 'Q1 2023'),
(5, 3, 2, '2023-04-01', 'Q2 2023');

-- Authors
INSERT INTO publications_author (id, name, email, affiliation, bio) VALUES
(1, 'Dr. Sarah Johnson', 'sarah.johnson@university.edu', 'University of Technology', 'Expert in machine learning and AI'),
(2, 'Prof. Michael Chen', 'mchen@research.org', 'Research Institute of Technology', 'Specialist in data mining'),
(3, 'Dr. Emily Brown', 'ebrown@sciencelab.com', 'Science Laboratory', 'Focus on algorithm development'),
(4, 'Dr. James Wilson', 'jwilson@techuni.edu', 'Tech University', 'Expert in distributed systems'),
(5, 'Prof. Lisa Anderson', 'landerson@ai.edu', 'AI Institute', 'Researcher in neural networks');

-- Publications
INSERT INTO publications_publication (
    id, title, abstract, text, pages, keywords, 
    doi, category_id, issue_id, created_at, updated_at
) VALUES
(1, 
 'Machine Learning Applications in Healthcare', 
 'This study explores the implementation of machine learning algorithms in healthcare diagnostics.',
 'Detailed text about machine learning applications in healthcare...', 
 '12-24',
 'machine learning, healthcare, AI, diagnostics',
 '10.1234/mlhealth.2023',
 1, -- Research Article
 1, -- Journal of Computer Science, Issue 1
 '2023-01-15 10:00:00', '2023-01-15 10:00:00'),

(2,
 'A Review of Deep Learning Frameworks',
 'Comprehensive review of current deep learning frameworks and their applications.',
 'Detailed comparison of various deep learning frameworks...',
 '25-42',
 'deep learning, frameworks, neural networks, AI',
 '10.1234/dlreview.2023',
 2, -- Review Article
 1, -- Journal of Computer Science, Issue 1
 '2023-01-15 11:00:00', '2023-01-15 11:00:00'),

(3,
 'Data Privacy in Cloud Computing',
 'Analysis of data privacy challenges and solutions in cloud computing environments.',
 'Detailed discussion of privacy concerns in cloud computing...',
 '43-58',
 'cloud computing, data privacy, security',
 '10.1234/privacy.2023',
 1, -- Research Article
 2, -- Journal of Computer Science, Issue 2
 '2023-04-15 10:00:00', '2023-04-15 10:00:00'),

(4,
 'Blockchain Technology in Supply Chain',
 'Case study of blockchain implementation in supply chain management.',
 'Detailed analysis of blockchain usage in supply chain...',
 '15-28',
 'blockchain, supply chain, case study',
 '10.1234/blockchain.2023',
 3, -- Case Study
 3, -- Data Science Review, Issue 1
 '2023-03-01 10:00:00', '2023-03-01 10:00:00'),

(5,
 'Future of Quantum Computing',
 'Technical perspective on quantum computing developments and challenges.',
 'Detailed technical discussion of quantum computing advances...',
 '5-11',
 'quantum computing, technology, future',
 '10.1234/quantum.2023',
 4, -- Technical Note
 4, -- AI Quarterly, Issue 1
 '2023-01-01 10:00:00', '2023-01-01 10:00:00');

-- Publication Authors
INSERT INTO publications_publication_authors (publication_id, author_id) VALUES
(1, 1), -- Sarah Johnson on ML in Healthcare
(1, 2), -- Michael Chen on ML in Healthcare
(2, 3), -- Emily Brown on Deep Learning Review
(2, 4), -- James Wilson on Deep Learning Review
(3, 5), -- Lisa Anderson on Data Privacy
(3, 1), -- Sarah Johnson on Data Privacy
(4, 2), -- Michael Chen on Blockchain
(4, 4), -- James Wilson on Blockchain
(5, 3); -- Emily Brown on Quantum Computing

-- Citations (publications citing other publications)
INSERT INTO publications_publication_citations (from_publication_id, to_publication_id) VALUES
(2, 1), -- Deep Learning Review cites ML in Healthcare
(3, 1), -- Data Privacy cites ML in Healthcare
(3, 2), -- Data Privacy cites Deep Learning Review
(4, 2), -- Blockchain cites Deep Learning Review
(5, 1); -- Quantum Computing cites ML in Healthcare
