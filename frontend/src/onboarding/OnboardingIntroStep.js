import React from "react";
import logo from "../image_assets/logo.svg";

const OnboardingIntroStep = () => {
  return (
    <div className="flex justify-center items-center h-screen bg-primary-100">
      <img src={logo} alt="onboarding logo" />
    </div>
  );
};

export default OnboardingIntroStep;
