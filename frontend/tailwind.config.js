/** @type {import('tailwindcss').Config} */
const withMT = require("@material-tailwind/react/utils/withMT");
module.exports = withMT({
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: {
          50: "#009281",
          100: "#009281",
          200: "#66beb3",
          300: "#99d3cd",
          400: "#99d3cd",
        },
        secondary: {
          50: "#99d3cd",
          100: "#3eaeff",
          200: "#3eaeff",
          300: "#fb4f4f",
        },
      },
    },
  },
  plugins: [],
});
