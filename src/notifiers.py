"""
โมดูลสำหรับระบบแจ้งเตือน (Observer & Factory Pattern)
"""
from abc import ABC, abstractmethod
from typing import Dict, Any

class Notifier(ABC):
    """Abstract Base Class / Interface สำหรับผู้รับการแจ้งเตือน (Observer)"""

    @abstractmethod
    def send(self, message: str, metadata: Dict[str, Any]) -> bool:
        """
        ส่งข้อความแจ้งเตือนไปยังปลายทาง
        
        Args:
            message: เนื้อหาข้อความแจ้งเตือน
            metadata: ข้อมูลประกอบ เช่น product_id, product_name, current_stock, threshold
        """
        pass

class EmailNotifier(Notifier):
    """ส่งการแจ้งเตือนทาง Email (จำลองด้วย print)"""

    def __init__(self, recipient_email: str):
        self.recipient_email = recipient_email

    def send(self, message: str, metadata: Dict[str, Any]) -> bool:
        print(f"[Email to {self.recipient_email}] {message} (Product: {metadata.get('product_name')}, Stock: {metadata.get('current_stock')}/{metadata.get('threshold')})")
        return True

class SMSNotifier(Notifier):
    """ส่งการแจ้งเตือนทาง SMS (จำลองด้วย print)"""

    def __init__(self, phone_number: str):
        self.phone_number = phone_number

    def send(self, message: str, metadata: Dict[str, Any]) -> bool:
        print(f"[SMS to {self.phone_number}] {message} - {metadata.get('product_name')} remaining {metadata.get('current_stock')}")
        return True

class NotifierFactory:
    """Factory Class สำหรับสร้าง Notifier Instance ตามประเภทที่ระบุ"""

    @staticmethod
    def create(channel_type: str, destination: str) -> Notifier:
        """
        สร้าง Notifier ตาม Channel Type
        
        Args:
            channel_type: ประเภทช่องทาง เช่น "email", "sms"
            destination: ที่อยู่อีเมล หรือเบอร์โทรศัพท์
        """
        channel = channel_type.lower()
        if channel == "email":
            return EmailNotifier(recipient_email=destination)
        elif channel == "sms":
            return SMSNotifier(phone_number=destination)
        else:
            raise ValueError(f"ไม่รองรับช่องทางการแจ้งเตือน: {channel_type}")
