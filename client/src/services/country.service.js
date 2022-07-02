import axios from "axios";

class CountryService {
  async getCountriesData() {
    const response = await axios.get("http://127.0.0.1:8080/api/getcountries");
    return response.data;
  }
}

export default new CountryService();
