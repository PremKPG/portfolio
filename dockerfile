# Use a lightweight Python base
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Copy your project code
COPY . .

# Expose port 5000 (where Flask runs)
EXPOSE 5000

# Start the app using gunicorn
CMD ["python", "-m", "gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

#updated version