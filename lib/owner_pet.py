class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return all pets that belong to this owner."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Assign this owner to a pet, if it's a valid Pet instance."""
        if not isinstance(pet, Pet):
            raise Exception("Only Pet instances can be added.")
        pet.owner = self

    def get_sorted_pets(self):
        """Return a list of this owner's pets sorted by pet name."""
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name

        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of: {Pet.PET_TYPES}")
        self.pet_type = pet_type

        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of the Owner class.")
        self.owner = owner

        Pet.all.append(self)