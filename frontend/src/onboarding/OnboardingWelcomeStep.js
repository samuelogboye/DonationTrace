import React from "react";
import onboardingImage2 from "../image_assets/undraw_welcome_re_h3d9 1.svg";
import frame from "../image_assets/Frame.svg";
import { NavLink } from "react-router-dom";

const OnboardingWelcomeStep = () => {
  return (
    <>
      <div className="flex justify-center items-center h-screen bg-white">
        <div className="flex flex-col items-center justify-center h-screen">
          <img src={onboardingImage2} alt="onboarding image" className="mb-4" />
          <div className="font-poppins text-3xl font-semibold leading-8 text-center mb-32">
            Welcome to <span className="text-primary-100">HealthSync</span> -
            Your Personal Health Companion
          </div>
          <button className="bg-primary-100 w-96 h-16 rounded-full text-white mb-4">
            Get Started
          </button>
          <NavLink to="/login">
            <div>
              Already Have an Account?{" "}
              <span className="font-bold underline cursor-pointer">
                Sign In
              </span>
            </div>
          </NavLink>
          <NavLink to="connect-data">
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

export default OnboardingWelcomeStep;
