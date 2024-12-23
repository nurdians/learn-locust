from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task
    def get_user(self):
        # Mengakses endpoint GET /api/users/2
        response = self.client.get("/api/users/2")
        print(f"Status code: {response.status_code}, Response: {response.text}")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 3)  # Waktu tunggu antar request (1-3 detik)
    host = "https://reqres.in"  # Base URL API

