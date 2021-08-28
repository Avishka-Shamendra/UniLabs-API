from unilabsAPI.test.global_test_setup import GlobalTestSetUp
from django.urls import reverse



class TestSetUp(GlobalTestSetUp):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.new_lab_manager_url = reverse('lab-manager-register')
        cls.lab_manager_data = {
            'email': cls.fake.email(),
            'lab': cls.global_test_lab.id,
            'department': cls.global_test_department.id
        }
        return 

    def tearDown(self):
        return super().tearDown()