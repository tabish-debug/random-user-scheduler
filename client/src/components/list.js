import React from "react";

export default function List({ list, total, country }) {
  return (
    <>
      <div className="py-5">
        <div className="container">
          <div className="d-flex justify-content-between">
            <h2 className="mb-4">{country}</h2>
            <h2>Users ({total})</h2>
          </div>
          <div className="row">
            {list.map((user, index) => (
              <div className="col-md-4 mb-3">
                <div className="card p-3">
                  <div className="card-block">
                    <h4 className="card-title">{user.name}</h4>
                    <h6 className="card-subtitle text-muted">{user.email}</h6>
                    <p className="card-text p-y-1">{user.gender}</p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </>
  );
}
