from mailjet_rest import Client

def send_email(to_email: str, code:str):
    mailjet = Client(auth=("1d535b76980e2931fdda00ad4a7ae70f", "535cb391a0bb1fa937e29f5f79b36665"), version='v3.1')
    data = {
    'Messages': [
        {
            "From": 
                {
                    "Email": "markakbarov@gmail.com",
                    "Name": "Me"
                    },
            "To": [
                {
                    "Email": to_email,
                    "Name": "Someone"
                    }
                    ],
                            "Subject": "Verification Code",
                            "TextPart": code,
                    }
            ]
    }
    result = mailjet.send.create(data=data)
    return result.status_code

print(send_email("markakbarov@gmail.com", "434052"))