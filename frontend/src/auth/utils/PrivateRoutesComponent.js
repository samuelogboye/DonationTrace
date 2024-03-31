import React from "react";
import { Routes } from "react-router-dom";
import PrivateRoute from "./PrivateRoute";
// import Dashboard from "../../pages/dashboard/page.jsx";

const PrivateRoutesComponent = () => {
  return (
    <PrivateRoute>
      <Routes>
        {/* <Route path="/dashboard" element={<Dashboard />} /> */}
      </Routes>
    </PrivateRoute>
  );
};

export default PrivateRoutesComponent;
