
/* Movies */
INSERT INTO movie (name, image_path, trailer_link, description, duration_hours, duration_min, director, cast) VALUES ('Black Panther', 'img/1.jpg','https://www.youtube.com/embed/dxWvtMOGAhw', ' it is�the 18th film�in the�Marvel Cinematic Universe�(MCU). The film was directed by�Ryan Coogler', 2, 5, 'Ryan Coogler', 'Do not know');
INSERT INTO movie (name, image_path, trailer_link, description, duration_hours, duration_min, director, cast) VALUES ('After', 'img/2.jpg', 'https://www.youtube.com/embed/95BKJA2QhCc', ' based on the 2014�new adult fiction�novel�of the same name�by�Anna Todd', 2, 0, 'Anna Todd', 'Marie James');
INSERT INTO movie (name, image_path, trailer_link, description, duration_hours, duration_min, director, cast) VALUES ('Star wars: The Empire strikes back', 'img/3.jpg', 'https://www.youtube.com/embed/JNwNXF9Y6kY', 'The Empire Strikes Back (also known as Star Wars: Episode V � The Empire Strikes Back) is a 1980 American epic space opera film directed by Irvin Kershner and written by Leigh Brackett and Lawrence Kasdan, based on a story by George Lucas. The sequel to Star Wars (1977),[b] it is the second film in the Star Wars film series and the fifth chronological chapter of the "Skywalker Saga". Set three years after the events of Star Wars, the film recounts the battle between the malevolent Galactic Empire, led by the Emperor and the Rebel Alliance led by Princess Leia. Luke Skywalker trains to master the Force so he can confront the powerful Sith lord, Darth Vader. The ensemble cast includes Mark Hamill, Harrison Ford, Carrie Fisher, Billy Dee Williams, Anthony Daniels, David Prowse, Kenny Baker, Peter Mayhew, and Frank Oz.', 2, 10, 'Harrison Ford', ' David Prowse, Kenny Baker, Peter Mayhew, and Frank Oz.');
INSERT INTO movie (name, image_path, trailer_link, description, duration_hours, duration_min, director, cast) VALUES ("Zack Snyder's Justice league", 'img/4.jpg', 'https://www.youtube.com/embed/QGnXv7vJkJY', "Zack Snyder's Justice League, often referred to as the, is the 2021�director's cut�of the 2017 American�superhero film�Justice League.�It presents�Justice League�the fifth film of the�DC Extended Universe�(DCEU) and the sequel to�Batman v Superman: Dawn of Justice�(2016)�as director�Zack Snyder�intended it before he left the production. Like the theatrical release,�Zack Snyder's Justice League�follows�DC Comics'�Justice League�Batman�(Ben Affleck),�Superman�(Henry Cavill),�Wonder Woman�(Gal Gadot),�Cyborg�(Ray Fisher),�Aquaman�(Jason Momoa), and the�Flash�(Ezra Miller)�as they attempt to save the world from the catastrophic threat of�Darkseid�(Ray Porter),�Steppenwolf�(Ciar�n Hinds), and their army of�Parademons.", 1, 50, 'Tomas M.', 'Not destacated');
INSERT INTO movie (name, image_path, trailer_link, description, duration_hours, duration_min, director, cast)  VALUES ('Jaws', 'img/5.jpg', 'https://www.youtube.com/embed/4pxkU9GVAoA', ' based on�the 1974 novel�by�Peter Benchley. In the film', 2, 0, 'Terry L.', 'Marilie Smith');
INSERT INTO movie (name, image_path, trailer_link, description, duration_hours, duration_min, director, cast)  VALUES ('Joker', 'img/6.jpg', 'https://www.youtube.com/embed/zAGVQLHvwOY', ' who co-wrote the screenplay with Scott Silver. The film', 3, 1, 'Scott Silver', 'Noting to commit');


/* Users */
INSERT INTO user (email, name, password, admin) VALUES ('yolo@yolo.com', 'Yolo Y.', 'yolo', TRUE);
INSERT INTO user (email, name, password, admin) VALUES ('yolo2@yolo.com', 'Yolo the Second', 'yolo', TRUE);

/* Screens */
INSERT INTO screen (seats) VALUES (25);
INSERT INTO screen (seats) VALUES (40);
INSERT INTO screen (seats) VALUES (38);

/* Projections */
INSERT INTO projection (screen_id, movie_id, date) VALUES (1,1, '2021-11-30 14:55');

/* Reservations */
INSERT INTO reservation (projection_id, user_id, seats, date) VALUE (1, 1, 2, '2021-11-29 14:55');