from abc import ABC, abstractmethod
from datetime import datetime


# ===================== ABSTRACT CLASSES =====================

class UserBase(ABC):
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username

    @abstractmethod
    def get_role(self):
        pass


class ChatBase(ABC):
    def __init__(self, chat_id):
        self.chat_id = chat_id

    @abstractmethod
    def send_message(self, message):
        pass


class MessageBase(ABC):
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.time = datetime.now()

    @abstractmethod
    def display(self):
        pass


class MediaBase(ABC):
    def __init__(self, file_name, size):
        self.file_name = file_name
        self.size = size

    @abstractmethod
    def open(self):
        pass


class NotificationBase(ABC):
    @abstractmethod
    def notify(self, user, text):
        pass


# ===================== CONCRETE CLASSES =====================

class RegularUser(UserBase):
    def get_role(self):
        return "RegularUser"


class AdminUser(UserBase):
    def get_role(self):
        return "Admin"


class TextMessage(MessageBase):
    def display(self):
        return f"{self.sender.username}: {self.content}"


class MediaMessage(MessageBase):
    def __init__(self, sender, content, media):
        super().__init__(sender, content)
        self.media = media

    def display(self):
        return f"{self.sender.username} sent media: {self.media.file_name}"


class Image(MediaBase):
    def open(self):
        return f"Opening image {self.file_name}"


class Video(MediaBase):
    def open(self):
        return f"Playing video {self.file_name}"


class PushNotification(NotificationBase):
    def notify(self, user, text):
        print(f"[PUSH] To {user.username}: {text}")


class PrivateChat(ChatBase):
    def __init__(self, chat_id, user1, user2, notifier):
        super().__init__(chat_id)
        self.users = [user1, user2]
        self.messages = []
        self.notifier = notifier

    def send_message(self, message):
        self.messages.append(message)
        for u in self.users:
            if u != message.sender:
                self.notifier.notify(u, message.display())


class GroupChat(ChatBase):
    def __init__(self, chat_id, users, notifier):
        super().__init__(chat_id)
        self.users = users
        self.messages = []
        self.notifier = notifier

    def send_message(self, message):
        self.messages.append(message)
        for u in self.users:
            if u != message.sender:
                self.notifier.notify(u, message.display())


# ===================== DEMO LOGIC =====================

if __name__ == "__main__":
    notifier = PushNotification()

    u1 = RegularUser(1, "alper")
    u2 = RegularUser(2, "irina")
    admin = AdminUser(99, "admin")

    chat = PrivateChat(100, u1, u2, notifier)

    msg1 = TextMessage(u1, "selam")
    chat.send_message(msg1)

    img = Image("photo.png", 200)
    msg2 = MediaMessage(u2, "bak buna", img)
    chat.send_message(msg2)


