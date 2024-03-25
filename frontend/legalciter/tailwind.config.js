/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./app.vue",
    "./error.vue",
  ],
  theme: {
    extend: {
      colors: {
        'legal': {
          '50': '#eff3ff',
          '100': '#dbe4fe',
          '200': '#bfcffe',
          '300': '#93aefd',
          '400': '#6088fa',
          '500': '#3b6bf6',
          '600': '#2558eb',
          '700': '#1d4dd8',
          '800': '#1e44af',
          '900': '#1e3a8a',
          '950': '#172754',
        },
      }
    },
  },
  plugins: [],
}

