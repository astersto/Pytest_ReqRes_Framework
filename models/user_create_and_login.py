from dataclasses import dataclass

@dataclass
class User_Create_And_Login:
    email: str = ""
    password: str = ""

    def to_dict(self):
        return {
            "email" : self.email,
            "password" : self.password
        }
