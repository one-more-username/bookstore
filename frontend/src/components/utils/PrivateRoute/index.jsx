import React from "react";
import { Route, Navigate } from "react-router-dom";
// import { connect } from "react-redux";

const PrivateRoute = ({ component: Component, ...rest }) => {
  return (
    <Route
      {...rest}
      render={(props) =>
        rest.isAuth ? (
          <Component {...props} />
        ) : (
          // <Redirect
          //   to={{
          //     pathname: "/login",
          //     state: { from: props.location },
          //   }}
          // />
          // <Navigate />
          // <Route path="/" element={<Navigate replace to="/home" />} />
          <Navigate replace to="/login" />
        )
      }
    />
  );
};

export default PrivateRoute;
