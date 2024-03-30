import {
  Card,
  Input,
  Checkbox,
  Button,
  Typography,
} from "@material-tailwind/react";

import appleLogo from "../image_assets/apple.svg";
import fbLogo from "../image_assets/fb.svg";
import google from "../image_assets/google.svg";
import { NavLink } from "react-router-dom";

export function SignUp() {
  return (
    <div className="flex justify-center items-center h-screen">
      <Card color="transparent" shadow={false}>
        <Typography variant="h4" color="blue-gray">
          Sign Up
        </Typography>
        <Typography color="gray" className="mt-1 font-normal">
          Create Account
        </Typography>
        <form className="mt-8 mb-2 w-80 max-w-screen-lg sm:w-96">
          <div className="mb-1 flex flex-col gap-6">
            <Typography variant="h6" color="blue-gray" className="-mb-3">
              Name
            </Typography>
            <Input
              size="lg"
              placeholder="Ex: John"
              className=" !border-t-blue-gray-200 focus:!border-t-gray-900"
              labelProps={{
                className: "before:content-none after:content-none",
              }}
            />
            <Typography variant="h6" color="blue-gray" className="-mb-3">
              Email
            </Typography>
            <Input
              size="lg"
              placeholder="name@Ex: Johndoe@gmail.com.com"
              className=" !border-t-blue-gray-200 focus:!border-t-gray-900"
              labelProps={{
                className: "before:content-none after:content-none",
              }}
            />
            <Typography variant="h6" color="blue-gray" className="-mb-3">
              Password
            </Typography>
            <Input
              type="password"
              size="lg"
              placeholder="********"
              className=" !border-t-blue-gray-200 focus:!border-t-gray-900"
              labelProps={{
                className: "before:content-none after:content-none",
              }}
            />
            <Typography variant="h6" color="blue-gray" className="-mb-3">
              Confirm Password
            </Typography>
            <Input
              type="passwrod"
              size="lg"
              placeholder="********"
              className=" !border-t-blue-gray-200 focus:!border-t-gray-900"
              labelProps={{
                className: "before:content-none after:content-none",
              }}
            />
          </div>
          <Checkbox
            label={
              <Typography
                variant="small"
                color="gray"
                className="flex items-center font-normal"
              >
                I agree the
                <a
                  href="#"
                  className="font-medium transition-colors hover:text-gray-900"
                >
                  &nbsp;Terms and Conditions
                </a>
              </Typography>
            }
            containerProps={{ className: "-ml-2.5" }}
          />
          <Button className="mt-6 bg-primary-50 rounded-full" fullWidth>
            sign up
          </Button>
          <div className="mt-4 flex justify-center">-Or Sign Up With-</div>
          <div className="mt-4 flex justify-center">
            <div className="flex flex-row">
              <img src={appleLogo} />
              <img src={fbLogo} />
              <img src={google} />
            </div>
          </div>
          <Typography color="gray" className="mt-32 text-center font-normal">
            Already have an account?{" "}
           <NavLink to="/login">
           <a href="#" className="font-medium text-gray-900">
              Sign In
            </a>
           </NavLink>
          </Typography>
        </form>
      </Card>
    </div>
  );
}
