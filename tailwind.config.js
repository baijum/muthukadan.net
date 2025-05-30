/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./pages/**/*.{html,md}",
    "./posts/**/*.{html,md}"
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#e07a5f',
          dark: '#c25e40',
          light: '#f2a990',
        },
        secondary: {
          DEFAULT: '#81b29a',
          dark: '#5f9279',
        },
        accent: '#f2cc8f',
        background: '#faf6f2',
        surface: '#ffffff',
        text: {
          DEFAULT: '#3d405b',
          muted: '#6d6875',
        },
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      },
      boxShadow: {
        'sm': '0 2px 8px rgba(0,0,0,0.08)',
        'md': '0 4px 12px rgba(0,0,0,0.10)',
        'lg': '0 8px 20px rgba(0,0,0,0.12)',
        'xl': '0 12px 24px rgba(0,0,0,0.14)',
        '2xl': '0 16px 32px rgba(0,0,0,0.16)',
      },
      borderRadius: {
        'DEFAULT': '0.75rem',
      },
    },
  },
  plugins: [],
}
