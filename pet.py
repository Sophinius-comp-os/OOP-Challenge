class Pet:
    def __init__(self, name):
        """
        Initializes a new Pet object.

        Args:
            name (str): The name of the pet.
        """
        self.name = name
        self.hunger = 5  # Start with a moderate hunger level
        self.energy = 5  # Start with a moderate energy level
        self.happiness = 5 # Start with a moderate happiness
        self.tricks = []   # Initialize an empty list to store tricks

    def eat(self):
        """
        Reduces hunger and increases happiness.
        """
        self.hunger = max(0, self.hunger - 3)  # Hunger cannot be negative
        self.happiness = min(10, self.happiness + 1) # happiness cannot be more than 10
        print(f"{self.name} ate something! Hunger reduced, happiness increased.")

    def sleep(self):
        """
        Increases energy.
        """
        self.energy = min(10, self.energy + 5)  # Energy cannot exceed 10
        print(f"{self.name} took a nap! Energy restored.")

    def play(self):
        """
        Decreases energy, increases happiness and increases hunger
        """
        self.energy = max(0, self.energy - 2)  # Energy cannot be negative
        self.happiness = min(10, self.happiness + 2) # happiness cannot be more than 10
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} played! Energy decreased, happiness increased, hunger increased.")

    def get_status(self):
        """
        Prints the current status of the pet.
        """
        print(f"\n{self.name}'s Status:")
        print(f"  Hunger: {self.hunger}/10")
        print(f"  Energy: {self.energy}/10")
        print(f"  Happiness: {self.happiness}/10")

    def train(self, trick):
        """
        Teaches the pet a new trick.

        Args:
            trick (str): The name of the trick.
        """
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        """
        Prints all learned tricks.
        """
        if self.tricks:
            print(f"\n{self.name}'s Tricks:")
            for trick in self.tricks:
                print(f"- {trick}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")


# Example Usage
if __name__ == "__main__":
    my_pet = Pet("Buddy")

    my_pet.get_status()

    my_pet.eat()
    my_pet.play()
    my_pet.sleep()

    my_pet.get_status()

    my_pet.train("Sit")
    my_pet.train("Fetch")
    my_pet.show_tricks()

    my_pet.play()
    my_pet.get_status()
