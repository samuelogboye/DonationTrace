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
import React, { useState } from "react";
import { useFormik } from "formik";
import * as Yup from "yup";
import { Link, useNavigate } from "react-router-dom";
import { showToast } from "../components/toaster";
import { resgisterUser } from "../config/api";

const Signup = () => {
  const validationSchema = Yup.object({
    first_name: Yup.string().required("First Name is required"),
    last_name: Yup.string().required("Second Name is required"),
    email: Yup.string()
      .email("Invalid email address")
      .required("Email is required"),
    password: Yup.string()
      .min(8, "Password must be at least 8 characters")
      .required("Password is required"),
    password2: Yup.string()
      .oneOf([Yup.ref("password"), null], "Passwords must match")
      .required("Confirm Password is required"),
    terms: Yup.boolean()
      .required("You must accept the terms and conditions")
      .oneOf([true], "You must accept the terms and conditions"),
  });

  const [loading, setLoading] = useState(false);
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);
  const togglePasswordVisibility = () => {
    setShowPassword(!showPassword);
  };

  const toggleConfirmPasswordVisibility = () => {
    setShowConfirmPassword(!showConfirmPassword);
  };

  const navigate = useNavigate();

  const formik = useFormik({
    initialValues: {
      first_name: "",
      last_name: "",
      email: "",
      password: "",
      password2: "",
      terms: false,
    },
    validationSchema,

    onSubmit: async (values) => {
      setLoading(true);
      try {
        await resgisterUser(values);
        showToast(
          "Registration successful. Please login to continue.",
          "success"
        );
        navigate("/login");
      } catch (error) {
        console.error("Registration failed:", error.message);
        showToast("Registration failed. " + error.message, "error"); // Show error message to the user
      } finally {
        setLoading(false);
      }
    },
  });

  return (
    <div className="flex justify-center items-center h-screen">
      <Card color="transparent" shadow={false}>
        <Typography variant="h4" color="blue-gray">
          Sign Up
        </Typography>
        <Typography color="gray" className="mt-1 font-normal">
          Create Account
        </Typography>
        <form
          onSubmit={formik.handleSubmit}
          className="mt-8 mb-2 w-80 max-w-screen-lg sm:w-96"
        >
          <div className="mb-1 flex flex-col gap-6">
            <Typography variant="h6" color="blue-gray" className="-mb-3">
              First Name
            </Typography>
            <Input
              name="first_name"
              size="lg"
              placeholder="John"
              value={formik.values.first_name}
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
              className={`!border-t-blue-gray-200 focus:!border-t-gray-900 ${
                formik.touched.first_name && formik.errors.first_name
                  ? "border-red-500"
                  : ""
              }`}
            />
            {formik.touched.first_name && formik.errors.first_name && (
              <div className="text-red-500 text-sm">
                {formik.errors.first_name}
              </div>
            )}
            <Typography variant="h6" color="blue-gray" className="-mb-3">
              Last Name
            </Typography>
            <Input
              name="last_name"
              size="lg"
              placeholder="Doe"
              value={formik.values.last_name}
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
              className={`!border-t-blue-gray-200 focus:!border-t-gray-900 ${
                formik.touched.first_name && formik.errors.first_name
                  ? "border-red-500"
                  : ""
              }`}
            />
            {formik.touched.last_name && formik.errors.last_name && (
              <div className="text-red-500 text-sm">
                {formik.errors.last_name}
              </div>
            )}
            <Typography variant="h6" color="blue-gray" className="-mb-3">
              Email
            </Typography>
            <Input
              name="email"
              size="lg"
              placeholder="John"
              value={formik.values.email}
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
              className={`!border-t-blue-gray-200 focus:!border-t-gray-900 ${
                formik.touched.email && formik.errors.email
                  ? "border-red-500"
                  : ""
              }`}
            />
            {formik.touched.email && formik.errors.email && (
              <div className="text-red-500 text-sm">{formik.errors.email}</div>
            )}
            <Typography variant="h6" color="blue-gray" className="-mb-3">
              Password
            </Typography>
            <div className="relative">
              <Input
                type={showPassword ? "text" : "password"}
                name="password"
                size="lg"
                placeholder="John"
                value={formik.values.password}
                onChange={formik.handleChange}
                onBlur={formik.handleBlur}
                className={`!border-t-blue-gray-200 focus:!border-t-gray-900 ${
                  formik.touched.password && formik.errors.password
                    ? "border-red-500"
                    : ""
                }`}
              />
              <span
                className="absolute inset-y-0 right-0 flex items-center pr-3 cursor-pointer"
                onClick={togglePasswordVisibility}
              >
                {showPassword ? (
                  <i className="material-icons">visibility_off</i> // Icon when the password is visible
                ) : (
                  <i className="material-icons">visibility</i> // Icon when the password is hidden
                )}
              </span>
            </div>
            {formik.touched.password && formik.errors.password && (
              <div className="text-red-500 text-sm">
                {formik.errors.password}
              </div>
            )}
            <Typography variant="h6" color="blue-gray" className="-mb-3">
              Confirm Password
            </Typography>
            <div className="relative">
              <Input
                type={showConfirmPassword ? "text" : "password"}
                name="password2"
                size="lg"
                placeholder="Confirm Password"
                value={formik.values.password2}
                onChange={formik.handleChange}
                onBlur={formik.handleBlur}
                className={`!border-t-blue-gray-200 focus:!border-t-gray-900 ${
                  formik.touched.password2 && formik.errors.password2
                    ? "border-red-500"
                    : ""
                }`}
              />
              <span
                className="absolute inset-y-0 right-0 flex items-center pr-3 cursor-pointer"
                onClick={toggleConfirmPasswordVisibility}
              >
                {showConfirmPassword ? (
                  <i className="material-icons">visibility_off</i> // Icon when the password is visible
                ) : (
                  <i className="material-icons">visibility</i> // Icon when the password is hidden
                )}
              </span>
            </div>
            {formik.touched.password2 && formik.errors.password2 && (
              <div className="text-red-500 text-sm">
                {formik.errors.password2}
              </div>
            )}
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
            name="terms"
            checked={formik.values.terms}
            onChange={formik.handleChange}
            containerProps={{ className: "-ml-2.5" }}
          />
          {formik.touched.terms && formik.errors.terms && (
            <div className="text-red-500 text-sm">{formik.errors.terms}</div>
          )}

          <Button
            type="submit"
            className="mt-6 bg-primary-50 rounded-full"
            fullWidth
            disabled={
              !formik.isValid || !formik.values.terms || formik.isSubmitting
            }
          >
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
          <Typography color="gray" className="mt-5 text-center font-normal">
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
};

export default Signup;
