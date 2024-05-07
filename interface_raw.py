from abc import ABC, abstractmethod

# Define uma regra de construção das demais classes onde ela é implementada! (uma regra de construção)
class NotificationSender(ABC):

    @abstractmethod
    def send_notification(self, message: str) -> None: pass

class SMSNotificationSender(NotificationSender):
    
    def send_notification(self, message: str) -> None:
        print(f'SMS message {message}')

class EmailNotificationSender(NotificationSender):
    def send_notification(self, message: str) -> None:
        print(f'Email message {message}')


class Notificator:

    def __init__(self, notification_sender) -> None:
        self.__notification_sender = notification_sender

    def send(self, message:str) -> None:
        #validação de dados
        self.__notification_sender.send_notification(message)


obj = Notificator()