<div align="center">
  <h1>Django FAQ</h1>
  
  <p>
    Django FAQ is an FAQ application build with Django and Django REST Framework of Python programming language.
  </p>

</div>

<br />

<!-- Table of Contents -->

# Table of Contents

- [About the Project](#about-the-project)
  - [Tech Stack](#tech-stack)
  - [Features](#features)
  - [Color Reference](#color-reference)
  - [Environment Variables](#environment-variables)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Run Locally](#run-locally)
  - [Deploy on Docker](#deploy-on-docker)
- [Contact](#contact)

<!-- About the Project -->

## About the Project

<!-- TechStack -->

### Tech Stack

<details>
  <summary>Client</summary>
  <ul>
    <li><a href="https://www.djangoproject.com/">Django</a></li>
    <li><a href="https://getbootstrap.com/">Bootstrap</a></li>
  </ul>
</details>

<details>
  <summary>Server</summary>
  <ul>
    <li><a href="https://www.djangoproject.com/">Django</a></li>
    <li><a href="https://www.django-rest-framework.org/">Django REST framework</a></li>
  </ul>
</details>

<details>
<summary>Database</summary>
  <ul>
    <li><a href="https://www.sqlite.org/">SQLite</a></li>
    <li><a href="https://www.postgresql.org/">PostgreSQL</a></li>
  </ul>
</details>

<details>
<summary>DevOps</summary>
    <li><a href="https://www.docker.com/">Docker</a></li>
    <li><a href="https://docs.gitlab.com/ee/ci/">Gitlab CI/CD</a></li>
  </ul>
</details>

<!-- Features -->

### Features

- Post question
- Answering
- View FAQ's

<!-- Color Reference -->

### Color Reference

| Color           | Hex                                                              |
| --------------- | ---------------------------------------------------------------- |
| Primary Color   | ![#222831](https://via.placeholder.com/10/ff008b?text=+) #ff008b |
| Secondary Color | ![#393E46](https://via.placeholder.com/10/31bfb1?text=+) #31bfb1 |
| Accent Color    | ![#00ADB5](https://via.placeholder.com/10/0069d9?text=+) #0069d9 |
| Text Color      | ![#EEEEEE](https://via.placeholder.com/10/212529?text=+) #212529 |

<!-- Env Variables -->

### Environment Variables

To run this project, you will need to add the following environment variable to your environment

`DJANGO_SETTINGS_MODULE`

Run the following command

```bash
 export DJANGO_SETTINGS_MODULE=django_faq.settings.dev
```

<!-- Getting Started -->

## Getting Started

<!-- Prerequisites -->

### Prerequisites

This project uses python3.10 and venv module

Run these commands

```bash
 sudo apt install python3.10

 python3 -m pip install venv
```

<!-- Installation -->

### Installation

Install the project by creating virtual environment

```bash
  python3 -m venv your/env/path

  source your/env/path/bin/activate
```

<!-- Run Locally -->

### Run Locally

Clone the project

```bash
  git clone https://gitlab.com/FansRan/django-faq.git
```

Go to the project directory

```bash
  cd django-faq
```

Install dependencies

```bash
  pip3 install -r requirements/dev.txt
```

Run the migration process

```bash
  python3 src/manage.py migrate
```

Start the development server

```bash
  python3 src/manage.py runserver
```

<!-- Running Tests -->
### Running Tests

To run tests, run the following command

```bash
  coverage run src/manage.py test src/ -v [0, 1, 2, 3]
```

<!-- Deploy -->
### Deploy on docker

To deploy the app in docker,
ensure you have docker installed in your machine
and run the following command

```bash  
  sudo docker-compose up --build
```

The server listen on port 80

<!-- Contact -->

## Contact

Project Link: [https://gitlab.com/FansRan/django-faq](https://gitlab.com/FansRan/django-faq)
