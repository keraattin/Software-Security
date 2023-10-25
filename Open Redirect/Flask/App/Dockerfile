# Use a Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Create a non-root user and group
RUN addgroup --system appgroup && adduser --system --no-create-home --ingroup appgroup appuser

# Copy only the requirements file first to leverage Docker layer caching
COPY requirements.txt .

# Upgrade the Pip
RUN pip install --upgrade pip

# Install the project's dependencies as the non-root user
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files into the container as the non-root user
COPY . .

# Set more restrictive permissions
RUN chown -R appuser:appgroup /app
RUN find /app -type f -exec chmod 0440 {} \;
RUN find /app -type d -exec chmod 0550 {} \;

# Drop privileges and run the application as the non-root user
USER appuser

# Expose port 5000 for the Flask application
EXPOSE 5000

# This is the command that will be executed when the container starts
CMD ["python", "app.py"]