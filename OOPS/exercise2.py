
class TestEnvironment:
    def __init__ (self, id, name, platform):
        self.id = id
        self.name = name
        self.platform = platform
        self.status = "AVAILABLE"

    def show_details(self):
        return f"ID: {self.id}  ||  Platform: {self.platform} ||  Name: {self.name} || Status: {self.status}"
    
    def change_status(self, new_status):
        self.status = new_status

class MobileEnvironment(TestEnvironment):
    def __init__(self, id, name, platform, device_model, os_version):
        super().__init__(id, name, platform)
        self.device_model = device_model
        self.os_version = os_version
    
    def show_details(self):
        parent_data = super().show_details()
        return f"{parent_data}  ||  Device: {self.device_model}  ||  OS: {self.os_version}"
    

class TestSuite:
    def __init__(self, suite_id, suite_name):
        self.suite_id = suite_id
        self.suite_name = suite_name
        self.env_assigned = None
        self.status = "AVAILABLE"

    def suite_assign_env(self, a = TestEnvironment):
        if self.status == "AVAILABLE" and a.status == "AVAILABLE":
            self.env_assigned = a
            self.status = "ALLOCATED"
            a.change_status("ALLOCATED")
            return True
        else:
            return False
    
    def show_details(self):
        env_info = (
            f"{self.env_assigned.name} >> {self.env_assigned.id}"
            if self.env_assigned else "None"
        )
        return f"Suite_id:{self.suite_id}  ||  Suite_name: {self.suite_name}   ||  Suite_status:{self.status}    ||  Environment Assigned: {env_info}"

        
    
pc_env = TestEnvironment("WEB","Web Application","Staging")
mob_env = MobileEnvironment("ANDR","Android Application","Production","Oneplus 7","Ver.69")

print("===Environments===")
print(pc_env.show_details())
print(mob_env.show_details())
print("==========================================================================================================")

t_suite = TestSuite("Suite_009","Client Regression")
print("Test Suite Details Before Environement Allocation")
print(t_suite.show_details())
print("==========================================================================================================")

print("Assigning Mobile Environment to above Test suite")
#assigned = t_suite.suite_assign_env(mob_env)
print("Assigned? : ",t_suite.suite_assign_env(mob_env))
print("Test Suite Details After Environement Allocation")
print(t_suite.show_details())
print("\nMobile Environment After Environement Allocation")
print(mob_env.show_details())
print("==========================================================================================================")


print("Re-Assigning PC Environment to above Test suite which is already assigned to Mobile")
#assigned2 = t_suite.suite_assign_env(pc_env)
print("Assigned again? : ",t_suite.suite_assign_env(pc_env))
print(t_suite.show_details())
print("PC Environment")
print(pc_env.show_details())
print("==========================================================================================================")


print("Freeing up mobile environment from the test suite")
t_suite.env_assigned = None
t_suite.status = "AVAILABLE"
mob_env.change_status("AVAILABLE")
print("Test Suite Details after freeing up")
print(t_suite.show_details())
print("Mobile Environment Details after freeing up")
print(mob_env.show_details())
















    
