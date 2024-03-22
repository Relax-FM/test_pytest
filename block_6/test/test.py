import pytest
import requests as req

from block_6.src.main import *


class Test_PetSwaggerApi:
    baseUrl = 'https://petstore.swagger.io/v2/pet'
    baseId = 5556665565
    basePet = base_pet
    baseHeader = base_header
    baseJson = base_json
    baseStatus = base_status


    @pytest.mark.create
    def test_PostPet(self):
        response = req.post(url=self.baseUrl, json=self.basePet.dict(), headers=self.baseHeader)
        assert response.status_code == 200
        assert response.json() == self.basePet.dict()


    @pytest.mark.update
    def test_PutPet(self):
        self.basePet.name = 'nedoggie'
        self.basePet.status = 'sold'
        response = req.put(url=self.baseUrl, json=self.basePet.dict(), headers=self.baseHeader)
        assert response.status_code == 200
        assert response.json()["name"] == "nedoggie"
        assert response.json()['status'] == 'sold'


    @pytest.mark.findstatus
    def test_GetByStatus(self):
        url = self.baseUrl + '/findByStatus'
        response = req.get(url, data=self.baseStatus.dict())
        assert response.status_code == 200
        for pet in response.json():
            assert pet['status'] == self.baseStatus.status


    @pytest.mark.findbyid
    def test_GetById(self):
        url = self.baseUrl + '/' + str(self.baseId)
        response = req.get(url)
        print(response.json())
        assert response.status_code == 200
        assert response.json()['id'] == self.baseId


    @pytest.mark.updatebyid
    def test_PostById(self):
        url = self.baseUrl + '/' + str(self.baseId)
        body = {
            'name': 'TudaSuda',
            'status': 'sold'
        }
        response = req.post(url, data=body)
        assert response.status_code == 200


    @pytest.mark.deletebyid
    def test_DeleteById(self):
        url = self.baseUrl + '/' + str(self.baseId)
        response = req.delete(url)
        assert response.status_code == 200