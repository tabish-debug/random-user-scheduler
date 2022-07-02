from abc import ABC, abstractmethod
import requests

from web.models import User, Country
from web import db

class AbstractConnector(ABC):
    @abstractmethod
    def request(self):
        pass

class AbstractAddData(ABC):
    @abstractmethod
    def validate_data(self):
        pass

    @abstractmethod
    def save_data(self):
        pass

class Connector(AbstractConnector):
    def __init__(self) -> None:
        self.url = "https://randomuser.me/api"
        self.include = ['name', 'gender', 'email', 'location']

    def request(self) -> dict:
        inc: str = ','.join(self.include)
        params: dict = {"inc": inc}
        data = requests.get(url=self.url, params=params)
        return data.json()

class AddData(AbstractAddData):
    def __init__(self, connector: AbstractConnector) -> None:
        self.connector = connector

    def save_user(self, name: str, gender: str, email: str, country_id: int) -> User:
        user: User = User.query.filter_by(name=name, email=email, country_id=country_id).first()
        if not user:
            user = User(
                name=name,
                gender=gender,
                email=email,
                country_id=country_id
            )
            db.session.add(user)
            db.session.commit()
        return user

    def save_country(self, name: str) -> Country:
        country: Country = Country.query.filter_by(name=name).first()
        if not country:
            country = Country(
                name=name
            )
            db.session.add(country)
            db.session.commit()
        return country

    def validate_data(self, data) -> dict:
        result: dict = data['results'][0]
        gender: str = result['gender'] if 'gender' in result else ''
        name_dict: dict = result['name'] if 'name' in result else ''
        name: str = ' '.join(name_dict.values()) if name_dict else ''
        location: dict = result['location'] if 'location' in result else ''
        country: str = location['country'] if location and 'country' in location else ''
        email: str = result['email'] if 'email' in result else ''
        return {
            'name': name,
            'email': email,
            'gender': gender,
            'country': country
        } 
    
    def save_data(self):
        data: dict = self.connector.request()
        validated_data: dict = self.validate_data(data=data)
        country: Country = self.save_country(
            name=validated_data['country'])
        self.save_user(
            name=validated_data['name'],
            gender=validated_data['gender'],
            email=validated_data['email'],
            country_id=country.id
        )

connector = Connector()
add_data = AddData(connector=connector)
