import React, { useEffect, useState } from "react";
import OnboardingWelcomeStep from "./OnboardingWelcomeStep";
import OnboardingIntroStep from "./OnboardingIntroStep";
import OnboardingConnectStep from "./OnboardingConnectStep";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import OnboardingScheduleAppointment from "./OnboardingScheduleAppointment";
import OnboardingStayInformed from "./OnboardingStayInformed";
import { SignUp } from "../auth/Signup";
import { SignIn } from "../auth/Signin";

const OnboardingMain = () => {
  const [showSplash, setShowSplash] = useState(true);
  const [showOnboarding, setShowOnboarding] = useState(false);

  useEffect(() => {
    const timer = setTimeout(() => {
      setShowSplash(false);
      setShowOnboarding(true);
    }, 3000);

    return () => clearTimeout(timer);
  }, []);

  return (
    <>
      {showSplash ? (
        <OnboardingIntroStep />
      ) : showOnboarding ? (
        <>
          <Router>
            <Routes>
              <Route path="/" Component={OnboardingWelcomeStep}></Route>
              <Route path="/connect-data" Component={OnboardingConnectStep}>
                {" "}
              </Route>
              <Route
                path="/schedule-appointment"
                Component={OnboardingScheduleAppointment}
              ></Route>
              <Route path="/stay-informed" Component={OnboardingStayInformed} />
              <Route path="/sign-up" Component={SignUp} />
              <Route path="/login" Component={SignIn}/>
            </Routes>
          </Router>
        </>
      ) : null}
    </>
  );
};

export default OnboardingMain;
