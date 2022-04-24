from usercredentials import User
import random, string

class Credentials:
    """
    Credentials class to create new credentials 
    """

    credentials_list = []
    
    def __init__(self, site_name, user_name, password):
        """
        __init__ to define properties of new Credentials
        Args:
            site_name: Website in which the credentials belong to
            user_name: username for website's account
            password: password for said account
        """

