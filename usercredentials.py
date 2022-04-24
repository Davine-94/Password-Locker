class User:
    """
    Class to generate new user instance
    """

    user_list = []
def __init__(self, first_name, sur_name, user_name, email, password):
    
        """
        __init__ method to define properties for object User
        Args:
            first_name: New user first name.
            sur_name: New user last name.
            email: New user email address.
            password: New user account password.
        """
        self.first_name = first_name
        self.sur_name = sur_name
        self.user_name = user_name
        self.email = email
        self.password = password