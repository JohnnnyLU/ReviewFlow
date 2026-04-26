# ReviewFlow

ReviewFlow is a small B2B SaaS project that helps small local businesses collect more positive reviews from their customers and handle negative feedback privately.

## Problem

Many local businesses (barbershops, clinics, cafes, salons, etc.) lose potential customers because:
- happy customers often do not leave reviews
- unhappy customers leave public negative reviews

This leads to lower ratings and fewer new clients.

## Solution

ReviewFlow automates the review process after a customer visit:

1. A business adds a customer to the system
2. The customer automatically receives a review request (link via email/SMS/Telegram)
3. The customer leaves a rating (1–5 stars)
4. If rating is positive (4–5):
   - customer is redirected to Google Reviews or similar platform
5. If rating is negative (1–3):
   - feedback is sent privately to the business for follow-up

## MVP Features

- Business authentication
- Add / manage customers
- Send review requests
- Public review page (rating flow)
- Private feedback form for negative reviews
- Simple dashboard with statistics

## Tech Stack

Backend:
- Python
- FastAPI
- PostgreSQL
- JWT authentication

Frontend:
- Next.js
- TypeScript
- Tailwind CSS

## Goal

The goal of this project is to build a working MVP in a small team, get real users, and validate the idea with local businesses.

## Status

Early stage (MVP in development)