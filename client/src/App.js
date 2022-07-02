import React, { useEffect, useState } from "react";
import countryService from "./services/country.service";
import Header from "./components/header";
import List from "./components/list";

function App() {
  const [data, setData] = useState([]);
  const [countries, setCountries] = useState([]);
  const [reload, setReload] = useState(false);
  const [selected, setSelected] = useState("");
  const [total, setTotal] = useState(0);
  const [country, setCountry] = useState("");
  const [list, setList] = useState([]);

  function dataReload() {
    setReload(!reload);
  }

  function selectedValue(value) {
    setSelected(value);
  }

  useEffect(() => {
    const countriesFilteredData = data?.filter((c) => {
      return c.name.toLowerCase() === selected.toLowerCase();
    });
    setCountry(countriesFilteredData[0]?.name);
    const users = countriesFilteredData[0]?.users;
    setTotal(users?.length);
    setList(users);
  }, [selected, data]);

  useEffect(() => {
    async function getData() {
      const data = await countryService.getCountriesData();
      const countriesData = data.countries.map((c) => {
        return c.name;
      });
      setData(data.countries);
      setCountries(countriesData);
    }
    getData();
  }, [reload]);
  return (
    <>
      <Header
        countries={countries}
        reload={dataReload}
        selected={selectedValue}
        value={selected}
      />
      {total && <List list={list} total={total} country={country} />}
    </>
  );
}

export default App;
