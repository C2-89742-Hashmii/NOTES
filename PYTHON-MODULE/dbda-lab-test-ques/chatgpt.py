
class Staff:
    def __init__(self, staff_id, name, staff_type):
        self.staff_id = staff_id
        self.name = name
        self.staff_type = staff_type  # "teaching" or "nonteaching"
    
    def __str__(self):
        return f"ID: {self.staff_id}, Name: {self.name}, Type: {self.staff_type}"
    
    def print_details(self):
        print(self)

class Institute:
    def __init__(self, name="Unknown Institute"):
        self.name = name
        self.staff_list = []
    
    def add_staff(self, staff):
        if len(self.staff_list) < 5:
            self.staff_list.append(staff)
        else:
            print("Staff limit reached. Cannot add more.")
    
    def print_teaching_staff(self):
        teaching_staff = filter(lambda s: s.staff_type == "teaching", self.staff_list)
        for staff in teaching_staff:
            print(staff)
    
    def print_non_teaching_staff(self):
        non_teaching_staff = filter(lambda s: s.staff_type == "nonteaching", self.staff_list)
        for staff in non_teaching_staff:
            print(staff)
    
    def display_all_staff_sorted(self):
        for staff in sorted(self.staff_list, key=lambda s: s.name):
            print(staff)
    
    def search_staff_by_id(self, staff_id):
        result = [staff for staff in self.staff_list if staff.staff_id == staff_id]
        return result[0] if result else None

# Testing module
def test_institute():
    institute = Institute("Tech Academy")
    
    # Adding staff members
    staff1 = Staff(101, "Alice", "teaching")
    staff2 = Staff(102, "Bob", "nonteaching")
    staff3 = Staff(103, "Charlie", "teaching")
    staff4 = Staff(104, "David", "nonteaching")
    staff5 = Staff(105, "Eve", "teaching")
    
    institute.add_staff(staff1)
    institute.add_staff(staff2)
    institute.add_staff(staff3)
    institute.add_staff(staff4)
    institute.add_staff(staff5)
    
    print("\nTeaching Staff:")
    institute.print_teaching_staff()
    
    print("\nNon-Teaching Staff:")
    institute.print_non_teaching_staff()
    
    print("\nAll Staff Sorted by Name:")
    institute.display_all_staff_sorted()
    
    print("\nSearching for Staff ID 103:")
    result = institute.search_staff_by_id(103)
    print(result if result else "Staff not found.")

# Run test module
test_institute()
