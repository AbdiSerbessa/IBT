# day06/practice.py
from abc import ABC, abstractmethod


# =====================================================================
# 1. SINGLE RESPONSIBILITY PRINCIPLE (SRP)
# =====================================================================
# Problem Statement: A User class shouldn't contain its own DB saving logic.

class User:
    """Responsible ONLY for representing the user's data profile."""
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

    def get_profile(self) -> str:
        return f"User: {self.username} | Contact: {self.email}"


class UserStorage:
    """Responsible ONLY for data persistence operations."""
    def __init__(self):
        self.database = {}  # Simulated in-memory database

    def save(self, user: User) -> None:
        self.database[user.username] = user.email
        print(f"💾 [SRP] Saved '{user.username}' successfully to storage.")


# =====================================================================
# 2. OPEN/CLOSED PRINCIPLE (OCP)
# =====================================================================
# Problem Statement: Adding a new discount should not require modifying existing classes.

class DiscountStrategy(ABC):
    """Abstract base strategy representing the open-ended discount concept."""
    @abstractmethod
    def calculate(self, price: float) -> float:
        pass


class RegularDiscount(DiscountStrategy):
    def calculate(self, price: float) -> float:
        return price * 0.95  # 5% Discount


class SeasonalDiscount(DiscountStrategy):
    def calculate(self, price: float) -> float:
        return price * 0.85  # 15% Discount


class DiscountCalculator:
    """Closed for modification: This class never changes when a new discount type is introduced."""
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def get_final_price(self, original_price: float) -> float:
        return self.strategy.calculate(original_price)


# =====================================================================
# 3. LISKOV SUBSTITUTION PRINCIPLE (LSP)
# =====================================================================
# Problem Statement: Avoid inheritance chains that break expectations of the base class.

class Shape(ABC):
    """Abstract base contract for geometric shapes."""
    @abstractmethod
    def area(self) -> float:
        pass


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class Square(Shape):
    """
    Subtype of Shape, NOT Rectangle. 
    LSP Check: We don't inherit from Rectangle to avoid mutating independent height/width.
    """
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side ** 2


# =====================================================================
# 4. DEPENDENCY INVERSION PRINCIPLE (DIP)
# =====================================================================
# Problem Statement: High-level modules must depend on abstract interfaces.

class MessageSender(ABC):
    """Abstract interface for messaging channels."""
    @abstractmethod
    def send(self, recipient: str, message: str) -> None:
        pass


class EmailSender(MessageSender):
    def send(self, recipient: str, message: str) -> None:
        print(f"📧 [DIP] Email sent to {recipient}: '{message}'")


class SMSSender(MessageSender):
    def send(self, recipient: str, message: str) -> None:
        print(f"💬 [DIP] SMS sent to {recipient}: '{message}'")


class NotificationService:
    """
    High-level module depending only on the abstract interface 'MessageSender'.
    The actual sender is injected via constructor injection.
    """
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def broadcast(self, recipient: str, alert: str) -> None:
        formatted_alert = f"SYSTEM ALERT: {alert}"
        self.sender.send(recipient, formatted_alert)


# =====================================================================
# 5. CREATIONAL PATTERN: FACTORY METHOD
# =====================================================================
# Problem Statement: Let a factory class handle dynamic object instantiation.

class AppNotification(ABC):
    """Product interface."""
    @abstractmethod
    def notify(self, message: str) -> None:
        pass


class PushNotification(AppNotification):
    def notify(self, message: str) -> None:
        print(f"📱 [Factory] PUSH Notification popped up: {message}")


class InAppNotification(AppNotification):
    def notify(self, message: str) -> None:
        print(f"ℹ️ [Factory] In-App alert rendered: {message}")


class NotificationFactory:
    """Creator class featuring the Factory Method."""
    @staticmethod
    def create_notifier(notif_type: str) -> AppNotification:
        mapping = {
            "push": PushNotification,
            "inapp": InAppNotification
        }
        creator = mapping.get(notif_type.lower())
        if not creator:
            raise ValueError(f"Unknown notification service type: {notif_type}")
        return creator()


# =====================================================================
# ⚡ EXECUTION RUNNER (Polymorphism & Integration Verification)
# =====================================================================
def run_exercises():
    print("=" * 60)
    print("🌟             RUNNING DAY 06 SOLID & PATTERNS            🌟")
    print("=" * 60)

    # 1. SRP Verification
    print("\n--- 1. Single Responsibility Principle ---")
    user = User("Abdisa", "abdisa@domain.com")
    print(user.get_profile())
    storage = UserStorage()
    storage.save(user)

    # 2. OCP Verification
    print("\n--- 2. Open/Closed Principle ---")
    price = 1000.0
    calc_regular = DiscountCalculator(RegularDiscount())
    calc_seasonal = DiscountCalculator(SeasonalDiscount())
    print(f"Original Price: {price} ETB")
    print(f"With 5% Regular Discount:  {calc_regular.get_final_price(price):.2f} ETB")
    print(f"With 15% Seasonal Discount: {calc_seasonal.get_final_price(price):.2f} ETB")

    # 3. LSP Verification
    print("\n--- 3. Liskov Substitution Principle ---")
    shapes: list[Shape] = [Rectangle(10, 5), Square(5)]
    for idx, shape in enumerate(shapes, 1):
        print(f"Shape {idx} calculated Area: {shape.area():.2f}")

    # 4. DIP Verification
    print("\n--- 4. Dependency Inversion Principle ---")
    email_notifier = NotificationService(EmailSender())
    sms_notifier = NotificationService(SMSSender())
    email_notifier.broadcast("Sifan", "Monthly report is ready!")
    sms_notifier.broadcast("+251911XXXXXX", "Verification Code: 5821")

    # 5. Factory Method Verification
    print("\n--- 5. Creational Factory Pattern ---")
    notifier_one = NotificationFactory.create_notifier("push")
    notifier_two = NotificationFactory.create_notifier("inapp")
    notifier_one.notify("You have 3 unread messages!")
    notifier_two.notify("Welcome back online!")

    print("\n" + "=" * 60)
    print("🚀           ALL DAY 06 EXERCISES COMPLETED!            🚀")
    print("=" * 60)


if __name__ == "__main__":
    run_exercises()