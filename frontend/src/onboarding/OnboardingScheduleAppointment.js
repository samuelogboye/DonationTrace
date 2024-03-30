import React from "react";
import onboardingImage from "../image_assets/onboardingImage4.svg";
import frame from "../image_assets/Frame.svg";
import { NavLink } from "react-router-dom";

const OnboardingScheduleAppointment = () => {
  return (
    <>
      <NavLink to="/">
        <button className="text-gray-500 text-sm  absolute top-0 right-0 mt-4 mr-8">
          Skip
        </button>
      </NavLink>

      <div className="flex flex-col justify-between h-screen bg-white">
        <div className="flex flex-col items-center justify-center h-screen">
          <img src={onboardingImage} alt="onboarding image" className="mb-4" />
          <div className="font-poppins text-3xl font-semibold leading-8 text-center mb-4">
            Schedule Appointment With{" "}
            <span className="text-primary-100">Ease</span>{" "}
          </div>
          <div className="text-center text-gray-500">
            Book appointments with healthcare providers hassle free.
          </div>
        </div>
        <div className="flex justify-between px-4 pb-4">
          <NavLink to="/stay-informed">
            <img
              className="text-white w-11 h-11  bg-primary-100 font-semibold absolute bottom-0 right-0 mt-4 mr-8 rounded-full cursor-pointer "
              src={frame}
            />
          </NavLink>
        </div>
      </div>
    </>
  );
};

export default OnboardingScheduleAppointment;
