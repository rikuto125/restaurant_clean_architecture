#bin/bash

# docker build
docker build -t fastapi-clean-arc:latest .

# docker run and mount
docker run -it -p 8000:8000 -v $(pwd):/app fastapi-clean-arc:latest