import React from "react";
import connectOnboardingImage from "../image_assets/onboarding-connect-img.svg";
import frame from "../image_assets/Frame.svg";
import { Link, NavLink } from "react-router-dom";

const OnboardingConnectStep = () => {
  return (
    <>
      <NavLink to="/">
        <button className="text-gray-500 text-sm  absolute top-0 right-0 mt-4 mr-8">
          Skip
        </button>
      </NavLink>
      <div className="flex flex-col justify-between h-screen bg-white">
        <div className="flex flex-col items-center justify-center h-screen">
          <img
            src={connectOnboardingImage}
            alt="onboarding image"
            className="mb-4"
          />
          <div className="font-poppins text-3xl font-semibold leading-8 text-center mb-4">
            Connect Your <span className="text-primary-100">Health</span>{" "}
            Records
          </div>
          <div className="text-center text-gray-500">
            Connect your medical health records from different healthcare
            providers, medical records and data syncing.
          </div>
        </div>
        <div className="flex justify-between px-4 pb-4">
          <Link to="/schedule-appointment">
            <img
              className="text-white w-11 h-11  bg-primary-100 font-semibold absolute bottom-0 right-0 mt-4 mr-8 rounded-full cursor-pointer "
              src={frame}
            />
          </Link>
        </div>
      </div>
    </>
  );
};

export default OnboardingConnectStep;
