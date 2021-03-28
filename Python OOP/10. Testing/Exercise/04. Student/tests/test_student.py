from project.student import Student

import unittest

class TestStudent(unittest.TestCase):
    def setUp(self):
        self.st = Student("Kalin")

    def test_init(self):
        self.assertEqual(self.st.name, "Kalin")
        self.assertEqual(self.st.courses, {})

    def test_add_non_existing_course_with_notes(self):
        self.st.courses = {}
        new_notes = self.st.enroll("Pyp", ["add those notes"])
        self.assertEqual(self.st.courses, {"Pyp": ["add those notes"]})
        self.assertEqual(new_notes, "Course and course notes have been added.")

    def test_add_non_existing_course_with_notes_and_y(self):
        self.st.courses = {}
        new_notes = self.st.enroll("Pyp", ["add those notes"], "Y")
        self.assertEqual(new_notes, "Course and course notes have been added.")

    def test_add_notes_to_existing_course(self):
        self.st.courses = {"Python": ["old notes"]}
        new_notes = self.st.enroll("Python", ["new notes"], "")
        self.assertEqual(self.st.courses, {"Python": ["new notes"]})
        self.assertEqual(new_notes, "Course already added. Notes have been updated.")

    def test_add_notes_to_existing_course_with_y(self):
        self.st.courses = {"Python": ["old notes"]}
        new_notes = self.st.enroll("Python", ["new notes"], "Y")
        self.assertEqual(self.st.courses, {"Python": ["new notes"]})
        self.assertEqual(new_notes, "Course already added. Notes have been updated.")

    def test_add_new_course(self):
        self.st.courses = {}
        new = self.st.enroll("Python", ["notes"], "Python")
        self.assertEqual(self.st.courses, {'Python': []})
        self.assertEqual(new, "Course has been added.")

    def test_add_new_notes(self):
        self.st.courses = {'Python': []}
        new = self.st.add_notes("Python", "notes")
        self.assertEqual(self.st.courses, {'Python': ["notes"]})
        self.assertEqual(new, "Notes have been updated")

    def test_add_notes_to_non_existing_course(self):
        self.st.courses = {"Python": ["no notes"]}
        with self.assertRaises(Exception) as ex:
            self.st.add_notes("Math", "adding this note")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_existing_course(self):
        self.st.courses = {"Python": "no notes"}
        leave = self.st.leave_course("Python")
        self.assertEqual(self.st.courses, {})
        self.assertEqual(leave, "Course has been removed")

    def test_leave_non_existing_course(self):
        self.st.courses = {"Python": "no notes"}
        with self.assertRaises(Exception) as ex:
            self.st.leave_course("Math")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

if __name__ == "__main__":
    unittest.main()