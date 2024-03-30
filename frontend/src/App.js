import { Route, Router, Routes } from "react-router-dom";
import Signup, { SignUp } from "./auth/Signup";
import OnboardingConnectStep from "./onboarding/OnboardingConnectStep";
import OnboardingIntroStep from "./onboarding/OnboardingIntroStep";
import OnboardingMain from "./onboarding/OnboardingMain";
import OnboardingScheduleAppointment from "./onboarding/OnboardingScheduleAppointment";
import OnboardingStayInformed from "./onboarding/OnboardingStayInformed";
import OnboardingWelcomeStep from "./onboarding/OnboardingWelcomeStep";
import { SignIn } from "./auth/Signin";
import Home from "./dashboard/Home";

function App() {
  return (
    <>
      <Home />
      {/* <OnboardingMain />  */}
    </>
  );
}

export default App;
