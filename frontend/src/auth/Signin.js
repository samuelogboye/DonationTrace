import { Card, Input, Button, Typography } from "@material-tailwind/react";
import appleLogo from "../image_assets/apple.svg";
import fbLogo from "../image_assets/fb.svg";
import googleLogo from "../image_assets/google.svg"; // Renamed for consistency
import AuthContext from "../auth/context/AuthContext";
import { NavLink, useNavigate } from "react-router-dom";
import React, { useContext, useState } from "react";
import { useFormik } from "formik";
import * as Yup from "yup";
import { showToast } from "../components/toaster";

const validationSchema = Yup.object().shape({
  email: Yup.string()
    .email("Invalid email address")
    .required("Email is required"),
  password: Yup.string().required("Password is required"),
});

const SignIn = () => {
  const { loginUser } = useContext(AuthContext);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const formik = useFormik({
    initialValues: {
      email: "",
      password: "",
    },
    validationSchema,
    onSubmit: async (values) => {
      setLoading(true);
      try {
        await loginUser(values);
        showToast("Successfully logged in. Welcome ", "success");
        navigate("/");
      } catch (error) {
        console.log(error);
        showToast(error.message, "error");
      } finally {
        setLoading(false);
      }
    },
  });

  return (
    <div className="flex justify-center items-center h-screen">
      <Card color="transparent" shadow={false}>
        <Typography variant="h4" color="blue-gray">
          Sign In
        </Typography>
        <Typography color="gray" className="mt-1 font-normal">
          Welcome Back
        </Typography>
        <form
          onSubmit={formik.handleSubmit}
          className="mt-8 mb-2 w-80 max-w-screen-lg sm:w-96"
        >
          <div className="mb-1 flex flex-col gap-6">
            <Typography variant="h6" color="blue-gray" className="-mb-3">
              Email
            </Typography>
            <Input
              name="email"
              type="email"
              size="lg"
              placeholder="name@example.com"
              value={formik.values.email}
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
              className={`!border-t-blue-gray-200 focus:!border-t-gray-900 ${
                formik.touched.email && formik.errors.email
                  ? "border-red-500"
                  : ""
              }`}
            />
            {formik.touched.email && formik.errors.email ? (
              <div className="text-red-500 text-sm">{formik.errors.email}</div>
            ) : null}
            <Typography variant="h6" color="blue-gray" className="-mb-3">
              Password
            </Typography>
            <Input
              name="password"
              type="password"
              size="lg"
              placeholder="********"
              value={formik.values.password}
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
              className={`!border-t-blue-gray-200 focus:!border-t-gray-900 ${
                formik.touched.password && formik.errors.password
                  ? "border-red-500"
                  : ""
              }`}
            />
            {formik.touched.password && formik.errors.password ? (
              <div className="text-red-500 text-sm">
                {formik.errors.password}
              </div>
            ) : null}
          </div>

          <Button
            type="submit"
            className="mt-6 bg-primary-50 rounded-full"
            fullWidth
            disabled={loading}
          >
            {loading ? "Signing In..." : "Sign In"}
          </Button>
          <div className="mt-4 flex justify-center">-Or Sign Up With-</div>
          <div className="mt-4 flex justify-center">
            <div className="flex flex-row">
              <img src={appleLogo} alt="Apple" />
              <img src={fbLogo} alt="Facebook" />
              <img src={googleLogo} alt="Google" />
            </div>
          </div>
          <Typography color="gray" className="mt-5 text-center font-normal p-8">
            Don’t Have an Account?
            <NavLink
              to="/sign-up"
              className="font-medium text-gray-900 underline ml-2"
            >
              Sign Up
            </NavLink>
          </Typography>
        </form>
      </Card>
    </div>
  );
};

export default SignIn;
