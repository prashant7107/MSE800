from fish import Fish,Angelfish,Goldfish,Salmon,Shark,Tuna

class FishFactory:
    @staticmethod
    def create_fish(fish_type: str):
        """
        Factory method to instantiate the correct Fish subclass 
        based on the provided string input.
        """
        target = fish_type.strip().lower()
        if target == "goldfish":
            return Goldfish()
        elif target == "shark":
            return Shark()
        elif target == "angelfish":
            return Angelfish()
        elif target == "tuna":
            return Tuna()
        elif target == "salmon":
            return Salmon()
        else:
            return None