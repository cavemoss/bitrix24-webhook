from bitrix24 import Bitrix24
from module.pg import cursor


class BitrixResolver:

    bx24 = Bitrix24('https://b24-2m30ah.bitrix24.ru/rest/1/qkc53uyamnc2hyga')

    def __init__(self, id: str, first_name: str, last_name: str) -> None:

        self.id = str(id) 

        self.first_name = first_name.capitalize()

        self.last_name = last_name.capitalize()

        self.ID: str

        self.NAME: str

        self.HONORIFIC: str

        for contact in self.bx24.callMethod('crm.contact.list'):
            if \
            contact.get('ID') == self.id and \
            contact.get('NAME') == self.first_name and \
            contact.get('LAST_NAME') == self.last_name:
                self.ID = self.id
                self.NAME = self.first_name
                print(contact)
            
    def define_gender(self):

        cursor.execute("SELECT * FROM names_woman")
        for name in cursor.fetchall():
            if self.NAME == name[1]:
                self.HONORIFIC = name[0]
                break

        cursor.execute("SELECT * FROM names_man")
        for name in cursor.fetchall():
            if self.NAME == name[1]:
                self.HONORIFIC = name[0]
                break

        self.bx24.callMethod('crm.contact.update', { 'id': self.ID, 'fields': {'HONORIFIC' : self.HONORIFIC} })
        return self

    def update_contact_info(self, update: dict):
        self.bx24.callMethod('crm.contact.update', { 'id': self.ID, 'fields': update })

    
"""
'HONORIFIC': 'HNR_RU_1' Mr.
'HONORIFIC': 'HNR_RU_2' Ms.
"""