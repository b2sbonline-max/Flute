# FLUTE CRM - Dynamic Form Builder

Modern full-stack CRM system replacing Classic ASP with Angular + FastAPI + PostgreSQL.

## Tech Stack

- **Frontend:** Angular 22.2.0
- **Backend:** FastAPI 0.142.2
- **Database:** PostgreSQL 18.6
- **Runtime:** Node.js 22.22.3, Python 3.14.4

## Project Structure

```
Flute/
├── backend/
│   ├── main.py                 # FastAPI entry
│   ├── database.py             # DB config
│   ├── models.py               # SQLAlchemy models
│   ├── schemas.py              # Pydantic schemas
│   ├── routes/
│   │   ├── users.py            # Auth endpoints
│   │   └── tables.py           # Table CRUD
│   ├── requirements.txt        # Dependencies
│   └── .env                    # Environment
├── frontend/ (Angular app)
├── flute_schema.sql            # PostgreSQL schema
├── .gitignore
└── README.md
```

## Setup

### Backend
```bash
cd backend
python3.14 -m venv ../venv
source ../venv/bin/activate
pip install -r requirements.txt
python main.py
```

### Frontend
```bash
cd flute-app
npm install
npm start
```

### Database
```bash
psql -U flute_user -d flute_crm -f flute_schema.sql
```

## API Endpoints

- `POST /api/users/login` - Login
- `POST /api/users/register` - Register
- `GET /api/tables` - List tables
- `POST /api/tables` - Create table
- `GET /api/tables/{name}/data` - Get data
- `POST /api/tables/{name}/data` - Add row

## Default Credentials

- Username: `admin`
- Password: `admin` (will be hashed)

## License

Proprietary
