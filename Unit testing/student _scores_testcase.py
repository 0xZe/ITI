import unittest
import student_scores_fun

class TestStudentSpeed(unittest.TestCase):

    #@classmethod
    #def beforeAll(cls):
    #    print("Test suit 1 started!")
    
    #@classmethod
    #def afterAll(cls):
    #    print("Test suit 1 completed!")

    def setUp(self) -> None:
        print("Test case is started")
    def tearDown(self) -> None:
        print("Test case is ended")
    
    def test_failed_score(self):
        self.assertEqual(student_scores_fun.student_score_level(40), "Failed!!")

    def test_passed_score(self):
        self.assertEqual(student_scores_fun.student_score_level(60), "Passed!!")

    def test_good_score(self):
        self.assertEqual(student_scores_fun.student_score_level(70), "Good!!")

    def test_vgood_score(self):
        self.assertEqual(student_scores_fun.student_score_level(80), "V.Good!!")

    def test_excellent_score(self):
        self.assertEqual(student_scores_fun.student_score_level(95), "Excellent!!")

class TestInvalidStudentSpeed(unittest.TestCase):

    def setUp(self) -> None:
        print("Invalid Test case is started")
    def tearDown(self) -> None:
        print("Invalid Test case is ended")

    def test_Invalid_speed1(self):
        self.assertEqual(student_scores_fun.student_score_level(-1), "Invalid!!")

    def test_Invalid_speed2(self):
        self.assertEqual(student_scores_fun.student_score_level(101), "Invalid!!")

    
if __name__ == '__main__':
    unittest.main()
