from .test_setup import TestSetUp

class TestViews(TestSetUp):
    # POST - New Admin 

    def test_authenticated_admin_can_register_new_admins(self):
        self.client.force_authenticate(user=self.global_test_admin)
        res = self.client.post(self.new_admin_url,self.admin_data,format="json")
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data['email'],self.admin_data['email'])

    def test_unauthenticated_user_cannot_add_admins(self):
        res = self.client.post(self.new_admin_url,self.admin_data,format="json")
        self.assertEqual(res.status_code, 401)

    def test_authenticated_other_users_cannot_register_new_admins(self):
        self.client.force_authenticate(user=self.global_test_lab_manager)
        res = self.client.post(self.new_admin_url,self.admin_data,format="json")
        self.assertEqual(res.status_code, 403)

    def test_cannot_add_admin_with_no_email(self):
        self.client.force_authenticate(user=self.global_test_admin)
        data = self.admin_data.copy()
        data["email"]=""
        res = self.client.post(self.new_admin_url,data,format="json")
        self.assertEqual(res.status_code, 400)

    def test_cannot_add_admin_with_invalid_email(self):
        self.client.force_authenticate(user=self.global_test_admin)
        data = self.admin_data.copy()
        data["email"]="test"
        res = self.client.post(self.new_admin_url,data,format="json")
        self.assertEqual(res.status_code, 400)