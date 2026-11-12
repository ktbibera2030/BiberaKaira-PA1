class StudentProfile:
    def __init__(self):
        self.name = "Kaira Bibera"
        self.age = "12"
        self.favorite = "N/A"
        self.hobbies = ["Reading", "Sleeping", "Gaming", "Studying"]

    def display_profile(self):
        print("===== STUDENT PROFILE =====")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Favorite:", self.favorite)
        print("Hobbies:", ", ".join(self.hobbies))