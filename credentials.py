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
            site_name: Website where the credentials belong to
            user_name: username for website's account
            password: Account Password
        """
        self.site_name = site_name
        self.user_name = user_name
        self.password = password
    
    def save_credentials(self):
        """
        save_credentials saves new instances to credentials_list array
        """
        Credentials.credentials_list.append(self)
        
    def delete_credentials(self):
        """
        delete_credentials removes existing instances from credentials_list array
        """
        Credentials.credentials_list.remove(self)
        
    @classmethod
    def find_by_site_name(cls, site_name):
        """
        This method takes in the site_name and returns the credentials to match the site_name
        Args:
            site_name: site name to search for
        Returns:
            login credentials of the website
        """
        for credential in cls.credentials_list:
            if credential.site_name == site_name:
                return credential

    @classmethod
    def list_credentials(cls, user_name):
        """
        This method takes in the credentials_list and returns the credentials array
        Args:
            credentials_list: list to display
        Returns:
            credentials_list array
        """
        user_credentials_list = []
        for credential in cls.credentials_list:
            if credential.user_name == user_name:
                user_credentials_list.append(credential)
        return user_credentials_list

    @classmethod
    def confirm_user(cls, user_name, password):
        """
        Method to check whether the user is in the user_list
        """
        confirmed_user = ""
        for user in User.user_list:
            if user.user_name == user_name and user.password == password:
                confirmed_user = user.user_name
            return confirmed_user

    def password_buidler(
        size=8, char=string.ascii_uppercase + string.ascii_lowercase + string.digits
    ):
        """
        Method to generarate user passwords
        """
        password = "".join(random.choice(char) for _ in range(size))
        return password
