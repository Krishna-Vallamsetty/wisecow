# STAGE 1: Build the Go application in a dedicated build environment
# Using a specific version of golang on a lightweight alpine base
FROM golang:1.21-alpine AS builder

# Set the working directory inside the container
WORKDIR /app

# Copy the go.mod file and download dependencies
COPY go.mod ./
RUN go mod download

# Copy the rest of the application source code
COPY . .

# Build the Go application.
# CGO_ENABLED=0 disables CGO to create a static binary, which is great for containers.
# -o wisecow specifies the output file name.
RUN CGO_ENABLED=0 go build -o wisecow .

# STAGE 2: Create the final, minimal production image
# Start from a scratch image, which is the smallest possible image, containing nothing.
FROM scratch

# Set the working directory
WORKDIR /app

# Copy only the compiled binary from the 'builder' stage. Nothing else is needed.
COPY --from=builder /app/wisecow .

# Expose port 8080 to allow traffic to the application
EXPOSE 8080

# The command to run when the container starts
CMD ["./wisecow"]
