class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
text = input()
while text != "Stop":
    sender, receiver, content = text.split(" ")
    email = Email(sender, receiver, content)
    emails.append(email)
    text = input()


numbers = list(map(lambda x: int(x), input().split(", ")))

for each in numbers:
    emails[each].send()

for anys in emails:
    print(anys.get_info())

