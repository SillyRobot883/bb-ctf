# Stage 1: Build the Go app
FROM golang:1.20-alpine AS builder

# Set the working directory
WORKDIR /app

# Copy the go.mod and go.sum files (if you have them)
COPY go.mod go.sum ./

# Install dependencies
RUN go mod download

# Copy the rest of the application code
COPY . .

# Build the Go application
RUN go build -o app main.go

# Stage 2: Create a minimal runtime image
FROM alpine:latest

# Set the working directory
WORKDIR /app

# Copy the compiled binary from the builder stage
COPY --from=builder /app/app .

# Copy the .env file
COPY --from=builder /app/.env .

# Expose port 8005
EXPOSE 8005

# Command to run the application
CMD ["./app"]
