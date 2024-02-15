#!/bin/bash

# Start uvicorn server
uvicorn src.Code.App:app --reload &
uvicorn_pid=$!

# Start dotnet watch
dotnet watch run --project src/Gui
dotnet_pid=$!

# Function to handle SIGINT
function cleanup {
    echo "Caught SIGINT, stopping..."
    kill $uvicorn_pid
    kill $dotnet_pid
    exit
}

# Trap SIGINT and call the cleanup function
trap cleanup SIGINT

# Wait for both processes to finish
wait $uvicorn_pid
wait $dotnet_pid