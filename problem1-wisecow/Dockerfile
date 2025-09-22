# STAGE 1: Build the Go application in a dedicated build environment
FROM golang:1.21-alpine AS builder

WORKDIR /app

COPY go.mod ./
RUN go mod download

COPY . .

# Build the Go application as a static binary
RUN CGO_ENABLED=0 go build -o wisecow .

# STAGE 2: Create the final, small production image
# Use alpine as the base, which includes a shell and common tools
FROM alpine:latest

WORKDIR /app

# Copy only the compiled binary from the 'builder' stage
COPY --from=builder /app/wisecow .

# Expose port 8080
EXPOSE 8080

# The command to run when the container starts
CMD ["./wisecow"]
