CREATE TABLE IF NOT EXISTS schools (
id integer PRIMARY KEY,
name text NOT NULL
);
CREATE TABLE IF NOT EXISTS classes (
id integer PRIMARY KEY,
name text NOT NULL,
school_id integer NOT NULL,
FOREIGN KEY (school_id) REFERENCES schools(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS students (
id integer PRIMARY KEY,
first_name text NOT NULL,
second_name text NOT NULL,
patronym text,
class_id integer NOT NULL,
FOREIGN KEY (class_id) REFERENCES classes (id)
);
CREATE TABLE IF NOT EXISTS teachers (
id integer PRIMARY KEY,
first_name text NOT NULL,
second_name text NOT NULL,
patronym text,
school_id integer NOT NULL,
FOREIGN KEY (school_id) REFERENCES schools (id)
);
CREATE TABLE IF NOT EXISTS subjects (
id integer PRIMARY KEY,
name text NOT NULL
);
CREATE TABLE IF NOT EXISTS teacher_to_subject (
id integer PRIMARY KEY,
teacher_id integer NOT NULL,
subject_id integer NOT NULL,
FOREIGN KEY (teacher_id) REFERENCES teachers (id) ON DELETE CASCADE,
FOREIGN KEY (subject_id) REFERENCES subjects (id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS grades (
id integer PRIMARY KEY,
grade integer NOT NULL,
grade_date date NOT NULL,
teacher_id integer NOT NULL,
subject_id integer NOT NULL,
student_id integer NOT NULL,
FOREIGN KEY (teacher_id) REFERENCES teachers (id),
FOREIGN KEY (subject_id) REFERENCES subjects (id) ON DELETE CASCADE,
FOREIGN KEY (student_id) REFERENCES students (id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS teacher_to_class (
id integer PRIMARY KEY,
teacher_id integer NOT NULL,
class_id integer NOT NULL,
FOREIGN KEY (teacher_id) REFERENCES teachers (id) ON DELETE CASCADE,
FOREIGN KEY (class_id) REFERENCES classes (id) ON DELETE CASCADE
);