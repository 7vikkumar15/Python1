class Dog:
    # Class variable (same for all dogs)
    species = "Canis Familiaris"

    def __init__(self, breed, name):
        # Instance variables (different for each dog)
        self.breed = breed
        self.name = name

    def display_details(self):
        print("Dog Name:", self.name)
        print("Breed:", self.breed)
        print("Species:", Dog.species)
        print("-" * 30)


# Creating objects for two different breeds
dog1 = Dog("Labrador", "Buddy")
dog2 = Dog("German Shepherd", "Max")

# Displaying details
dog1.display_details()
dog2.display_details()