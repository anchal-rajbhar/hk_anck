class EmailValidation:
    def __init__(self,email):
        self.email=email
    def validate(self):
        if "@"  in self.email and "."  in self.email:
            print("valid")
        else :
            print("invalid")
        return
    def domainName(self):
        d=self.email.split("@")
        print("The domain name of given email is :-",d[0])
p=EmailValidation("abc@gmail.com")
p.validate()
p.domainName()
