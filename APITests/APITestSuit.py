import unittest
import requests
from bson import ObjectId

class TestAPI(unittest.TestCase):
    DOMAIN = "http://localhost:5000"
    DATA_ENDPOINT_BASE_URL = f"{DOMAIN}/data"

    def test_create_data(self):
        new_data = {"name": "Test Item", "value": 100}
        res = requests.post(self.DATA_ENDPOINT_BASE_URL, json=new_data)
        self.assertEqual(res.status_code, 201)
        self.assertIn("id", res.json())
        self.created_id = res.json()["id"]

    def test_get_data(self):
        # First, create data to retrieve
        new_data = {"name": "Test Item", "value": 100}
        create_res = requests.post(self.DATA_ENDPOINT_BASE_URL, json=new_data)
        item_id = create_res.json()["id"]
        
        # Retrieve created data
        response = requests.get(f"{self.DATA_ENDPOINT_BASE_URL}/{item_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], new_data["name"])
        #self.assertEqual(response.json()["value"], new_data["value"])

    def test_update_data(self):
        # First, create data to update
        new_data = {"name": "Test Item", "value": 100}
        create_res = requests.post(self.DATA_ENDPOINT_BASE_URL, json=new_data)
        item_id = create_res.json()["id"]

        # Update created data
        updated_data = {"name": "Updated Item", "value": 200}
        res = requests.put(f"{self.DATA_ENDPOINT_BASE_URL}/{item_id}", json=updated_data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["message"], "Data updated")

        # Retrieve updated data to verify update
        get_res = requests.get(f"{self.DATA_ENDPOINT_BASE_URL}/{item_id}")
        self.assertEqual(get_res.status_code, 200)
        self.assertEqual(get_res.json()["name"], updated_data["name"])
        self.assertEqual(get_res.json()["value"], updated_data["value"])

    def test_delete_data(self):
        # First, create data to delete
        new_data = {"name": "Test Item", "value": 100}
        create_res = requests.post(self.DATA_ENDPOINT_BASE_URL, json=new_data)
        item_id = create_res.json()["id"]

        # Delete the created data
        res = requests.delete(f"{self.DATA_ENDPOINT_BASE_URL}/{item_id}")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["message"], "Data deleted")

        # Attempt to retrieve the deleted data to verify deletion
        get_res = requests.get(f"{self.DATA_ENDPOINT_BASE_URL}/{item_id}")
        self.assertEqual(get_res.status_code, 404)
        self.assertEqual(get_res.json()["error"], "Data not found")

    def test_invalid_endpoint(self):
        res = requests.get(self.DOMAIN)
        self.assertEqual(res.status_code, 405)
        self.assertEqual(res.json()["error"], "Not a valid API endpoint.")

    def test_invalid_data_format(self):
        res = requests.post(self.DATA_ENDPOINT_BASE_URL, data="invalid data format")
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json()["error"], "Invalid Data Format.")

    def test_get_nonexistent_data(self):
        nonexistent_id = str(ObjectId())
        res = requests.get(f"{self.DATA_ENDPOINT_BASE_URL}/{nonexistent_id}")
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.json()["error"], "Data not found")

# if __name__ == "__main__":
#     unittest.main()