import React from "react";

export default function Header({ countries, reload, selected, value }) {
  return (
    <div className="container">
      <div className="row mt-3">
        <div className="col-md-1"></div>
        <div className="col-md-6">
          <input
            value={value}
            list="countries"
            className="form-control"
            onChange={(e) => {
              selected(e?.target?.value);
            }}
          />
          <datalist id="countries">
            {countries.map((name, i) => {
              return <option key={i} value={name} />;
            })}
          </datalist>
        </div>
        <div className="col-md-2">
          <button className="btn btn-success" onClick={(e) => selected("")}>
            Refresh
          </button>
        </div>
        <div className="col-md-2">
          <button className="btn btn-success" onClick={reload}>
            Reload Data
          </button>
        </div>
        <div className="col-md-1"></div>
      </div>
    </div>
  );
}
