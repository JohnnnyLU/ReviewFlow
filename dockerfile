FROM python:3.13.13-bookworm

WORKDIR /app

# installation uv
RUN pip install --no-cache-dir uv

# copy dependencies files
COPY pyproject.toml uv.lock ./

# installation dependencies
RUN uv sync --frozen --no-dev

# copy app code
COPY Backend/app ./app

ENV PATH="/app/.venv/bin:$PATH"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]