# Technical Notes

## Phase 1 — FastAPI + Groq

### Why FastAPI over Flask/Bottle
I chose FastAPI over Flask/Bottle (which I already use in production) because I wanted to demonstrate proficiency with a modern framework and its built-in Pydantic validation. For a pure backend service returning JSON, FastAPI is also a natural fit.
### Why Groq over OpenAI
I chose Groq over OpenAI because it offers a free tier with no credit card required, making it ideal for portfolio projects. It exposes the same API interface as OpenAI, so switching to a paid provider in the future would require minimal code changes.
### What I learned about Pydantic
Pydantic models feel similar to Python dataclasses, but with automatic validation built in. In Flask I used to extract and check request data manually. With FastAPI and Pydantic, I just declare the expected structure and types — if the incoming data doesn't match, FastAPI returns a clear error automatically, without any extra code.
