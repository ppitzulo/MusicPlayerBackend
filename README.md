# Music Player Backend

This is the backend repository for my music player project. The backend is built using Django and provides an API for managing and serving music-related data.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [License](#license)

## Features

- Manages and serves music-related data.
- Supports pagination for efficient data retrieval.
- Dockerized for easy deployment and development.
- Automatically extracts the runtime and thumbnail from the metadata of the MP3 for later retrieval.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/music-player-backend.git
   cd music-player-backend
   ```
2. Create a `.env` file in the project root and set `DJANGO_SECRET_KEY_DEMO` as well as `DJANGO_SECRET_KEY_DEV` to a random key
3. Now build and run the docker container
   ``` bash
   docker-compose up --build
   ```

The API can be accessed at:
* For local development:
  - `http://localhost:8000` (non-SSL)
  - `https://localhost:8000` (SSL with a self-signed certificate)

- For production:
  - `https://your-domain.com` (replace `your-domain.com` with your actual domain)
## Docker Setup

This project uses Docker Compose to manage several services.
* **db**: A PostgreSQL database service
* **web**: The Django application being served through gunicorn.
* **nginx**: A Nginx service acting as a reverse proxy.
* **certbot**: A Certbot service for managing SSL certificates.
   
## API Endpoints

* GET /api/list-songs/?page
  * Retrieve a paginated list of songs.
  * supports pagination through the page query parameter
* GET /api/audio/<song-id>
  * Fetch song file
* Get /api/search/<keyword>
  * Searches for song based off title and artist

## License

This project is licensed under the terms of the [GNU General Public License (GPL)](LICENSE).
